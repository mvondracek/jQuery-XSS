import logging
from typing import TextIO, Dict, Tuple

from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

LOGGER = logging.getLogger(__name__)


# noinspection SpellCheckingInspection
class JQueryXssError(Exception):
    pass


class InvalidInput(JQueryXssError):
    pass


Position = Tuple[int, int]


class Detection:
    def __init__(self, line: int, column: int, method_call: str) -> None:
        """
        Detection of unsafe method call in source code.
        :param line:
        :param column:
        :param method_call:
        """
        self.line: int = line
        self.column: int = column
        self.method_call: str = method_call

    @property
    def position(self) -> Position:
        return self.line, self.column


def is_jquery_selector_expression(node) -> bool:
    """
    Check whether provided AST `node` is jQuery selector expression (`$("#foo")`).
    """
    return \
        isinstance(node, ast.FunctionCall) \
        and isinstance(node.identifier, ast.Identifier) \
        and node.identifier.value == '$'


def analyse(source_code: str) -> Dict[Position, Detection]:
    """
    Analyse JavaScript code for a potential jQuery XSS.
    :param source_code: string with JavaScript code for analysis
    :return: detected unsafe uses of jQuery methods

    :raises InvalidInput: on syntax error in provided JavaScript source code
    """
    unsafe_methods = ['html', 'prepend', 'prependTo', 'append', 'appendTo',
                      'before', 'after', 'insertBefore', 'insertAfter',
                      'wrap', 'wrapInner', 'wrapAll']
    detections: Dict[Tuple[int, int], Detection] = {}
    parser = Parser()
    try:
        tree = parser.parse(source_code, tracking=True)
    except SyntaxError as e:
        LOGGER.critical(e)
        raise InvalidInput from e
    for node in nodevisitor.visit(tree):
        if isinstance(node, ast.FunctionCall) and len(node.args) != 0:
            # function call with at least one parameter
            hit = False
            # following conditions are separated for better readability
            if isinstance(node.identifier, ast.BracketAccessor) \
                    and is_jquery_selector_expression(node.identifier.node) \
                    and isinstance(node.identifier.expr, ast.String) \
                    and node.identifier.expr.value[1:-1] in unsafe_methods:
                hit = True
            elif isinstance(node.identifier, ast.DotAccessor) \
                    and is_jquery_selector_expression(node.identifier.node) \
                    and isinstance(node.identifier.identifier, ast.Identifier) \
                    and node.identifier.identifier.value in unsafe_methods:
                hit = True
            # conditions above are separated for better readability
            if hit:
                detection = Detection(node.lex_line, node.lex_column, node.to_ecma())
                detections[detection.position] = detection
                LOGGER.debug('unsafe method call {}=`{}`'.format(
                    detection.position, detection.method_call))
    return detections


def analyse_file(input_: TextIO) -> Dict[Position, Detection]:
    """
    Analyse JavaScript code in input file for a potential jQuery XSS.
    :param input_: Input text file with JavaScript code.

    :raises InvalidInput: on syntax error in provided JavaScript source code
    """
    return analyse(input_.read())
