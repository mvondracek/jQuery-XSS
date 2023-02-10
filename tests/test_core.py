from unittest import TestCase

from jqueryxss.core import analyse, InvalidInput


# noinspection PyPep8Naming
class Test_analyse(TestCase):
    def assert_detection(self, code: str) -> None:
        detections = analyse(code)
        self.assertEqual(1, len(detections))
        self.assertTupleEqual((1, 1), list(detections.keys())[0])

    def test_false(self):
        self.assertEqual(0, len(analyse('var _0x01ff=["foo"];var a=[9,_0x01ff[0],7];')))
        self.assertEqual(0, len(analyse('$("#foo").bar(baz)')))
        self.assertEqual(0, len(analyse('foo.html(baz)')))
        self.assertEqual(0, len(analyse('foo["html"](baz)')))

    def test_syntax_error(self):
        with self.assertRaises(InvalidInput):
            analyse(')')

    def test_array_access_html(self):
        self.assert_detection('$("#foo")["html"](xss)')

    def test_array_access_html_getter(self):
        detections = analyse('$("#foo")["html"]()')
        self.assertEqual(0, len(detections))

    def test_array_access_multiline(self):
        self.assert_detection("$(\n'\\\nh1\\\n'\n)\n[\n'\\\nhtml\\\n'\n]\n(\nxss\n)")

    def test_function_call_html(self):
        self.assert_detection('$("#foo").html(xss)')

    def test_function_call_html_getter(self):
        detections = analyse('$("#foo").html()')
        self.assertEqual(0, len(detections))

    def test_function_call_multiline(self):
        self.assert_detection("$(\n'\\\nh1\\\n'\n)\n.\nhtml\n(\nxss\n)")

    def test_unsafe_basic(self):
        # https://api.jquery.com/html/#html2
        self.assert_detection('$("#foo")["html"](xss)')
        self.assert_detection('$("#foo").html(xss)')

        # https://api.jquery.com/prepend/
        self.assert_detection('$("#foo")["prepend"](xss)')
        self.assert_detection('$("#foo").prepend(xss)')

        # https://api.jquery.com/prependTo/
        self.assert_detection('$(xss)["prependTo"](target)')
        self.assert_detection('$(xss).prependTo(target)')

        # https://api.jquery.com/append/
        self.assert_detection('$("#foo")["append"](xss)')
        self.assert_detection('$("#foo").append(xss)')

        # https://api.jquery.com/appendTo/
        self.assert_detection('$(xss)["appendTo"](target)')
        self.assert_detection('$(xss).appendTo(target)')

        # https://api.jquery.com/before/
        self.assert_detection('$("#foo")["before"](xss)')
        self.assert_detection('$("#foo").before(xss)')

        # https://api.jquery.com/after/
        self.assert_detection('$("#foo")["after"](xss)')
        self.assert_detection('$("#foo").after(xss)')

        # https://api.jquery.com/insertBefore/
        self.assert_detection('$(xss)["insertBefore"](target)')
        self.assert_detection('$(xss).insertBefore(target)')

        # https://api.jquery.com/insertAfter/
        self.assert_detection('$(xss)["insertAfter"](target)')
        self.assert_detection('$(xss).insertAfter(target)')

        # https://api.jquery.com/wrapInner/
        self.assert_detection('$("#foo")["wrapInner"](xss)')
        self.assert_detection('$("#foo").wrapInner(xss)')

        # https://api.jquery.com/wrap/
        self.assert_detection('$("#foo")["wrap"](xss)')
        self.assert_detection('$("#foo").wrap(xss)')

        # https://api.jquery.com/wrapAll/
        self.assert_detection('$("#foo")["wrapAll"](xss)')
        self.assert_detection('$("#foo").wrapAll(xss)')

    def test_multiple_lines(self):
        detections = analyse('\nvar a = 1;\n$("#foo").html(xss)\nvar b=2;$("#foo").html(xss)')
        self.assertEqual(2, len(detections))
        self.assertListEqual([(3, 1), (4, 9)], list(detections.keys()))
