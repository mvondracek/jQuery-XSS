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


def is_jquery_selector_expression(node) -> bool:
    """
    Check whether provided AST `node` is jQuery selector expression (`$("#foo")`).
    """
    return \
        isinstance(node, ast.FunctionCall) \
        and isinstance(node.identifier, ast.Identifier) \
        and node.identifier.value == '$'


def analyse(source_code: str) -> Dict[Tuple[int, int], str]:
    """
    Analyse JavaScript code for a potential jQuery XSS.
    :param source_code: obfuscated code in Array Ref obfuscation format.
    :return: deobfuscated code.

    :raises InvalidInput: on syntax error in provided JavaScript source code
    """
    unsafe_methods = ['html', 'prepend', 'prependTo', 'append', 'appendTo',
                      'before', 'after', 'insertBefore', 'insertAfter',
                      'wrap', 'wrapInner', 'wrapAll']
    detections = {}
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
                detections[(node.lex_line, node.lex_column)] = node.to_ecma()
                print('unsafe method call ({},{})=`{}`'.format(
                    node.lex_line, node.lex_column, node.to_ecma()))
    return detections


def analyse_file(input_: TextIO) -> None:
    """
    Analyse JavaScript code in input file for a potential jQuery XSS.
    :param input_: Input text file with JavaScript code.

    :raises InvalidInput: on syntax error in provided JavaScript source code
    """
    analyse(input_.read())
