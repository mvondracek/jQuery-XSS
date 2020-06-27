from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.results.SourceRange import SourceRange
from dependency_management.requirements.PipRequirement import PipRequirement

from jqueryxss import __author__ as jqueryxss_author
from jqueryxss.core import analyse


class JSjQueryXssUnsafeBear(LocalBear):
    LANGUAGES = {'JavaScript'}

    AUTHORS = {jqueryxss_author}
    CAN_DETECT = {'Security'}

    REQUIREMENTS = {PipRequirement('slimit', '0.11.0-mv')}

    def run(self, filename, file, **kwargs):
        """
        jQuery XSS Static Analyser

        Static analyser for JavaScript which can detect use of unsafe jQuery
        methods which are vulnerable to XSS attack.
        """
        bear_results = []
        file_content = ''.join(file)
        # raises InvalidInput: on syntax error in provided JavaScript source code
        detections = analyse(file_content)
        for detection in detections.values():
            bear_results.append(Result(
                self,
                'unsafe jQuery method call `{method_call}`',
                (
                    SourceRange.from_values(filename, detection.line, detection.column),
                ),
                message_arguments={'method_call': detection.method_call},
            ))
        return bear_results
