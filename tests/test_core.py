from unittest import TestCase

from jqueryxss.core import analyse, InvalidInput


# noinspection PyPep8Naming
class Test_analyse(TestCase):
    def test_array_access_html(self):
        detections = analyse('$("#foo")["html"](xss)')
        self.assertEqual(1, len(detections))
        self.assertTupleEqual((1, 1), list(detections.keys())[0])

    def test_array_access_html_getter(self):
        detections = analyse('$("#foo")["html"]()')
        self.assertEqual(0, len(detections))

    def test_array_access_multiline(self):
        detections = analyse("$(\n'\\\nh1\\\n'\n)\n[\n'\\\nhtml\\\n'\n]\n(\nxss\n)")
        self.assertEqual(1, len(detections))
        self.assertTupleEqual((1, 1), list(detections.keys())[0])

    def test_function_call_html(self):
        detections = analyse('$("#foo").html(xss)')
        self.assertEqual(1, len(detections))
        self.assertTupleEqual((1, 1), list(detections.keys())[0])

    def test_function_call_html_getter(self):
        detections = analyse('$("#foo").html()')
        self.assertEqual(0, len(detections))

    def test_function_call_multiline(self):
        detections = analyse("$(\n'\\\nh1\\\n'\n)\n.\nhtml\n(\nxss\n)")
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

    def test_unsafe_basic(self):
        def assert_detection(code):
            detections = analyse(code)
            self.assertEqual(1, len(detections))
            self.assertTupleEqual((1, 1), list(detections.keys())[0])

        # https://api.jquery.com/html/#html2
        assert_detection('$("#foo")["html"](xss)')
        assert_detection('$("#foo").html(xss)')

        # https://api.jquery.com/prepend/
        assert_detection('$("#foo")["prepend"](xss)')
        assert_detection('$("#foo").prepend(xss)')

        # https://api.jquery.com/prependTo/
        assert_detection('$(xss)["prependTo"](target)')
        assert_detection('$(xss).prependTo(target)')

        # https://api.jquery.com/append/
        assert_detection('$("#foo")["append"](xss)')
        assert_detection('$("#foo").append(xss)')

        # https://api.jquery.com/appendTo/
        assert_detection('$(xss)["appendTo"](target)')
        assert_detection('$(xss).appendTo(target)')

        # https://api.jquery.com/before/
        assert_detection('$("#foo")["before"](xss)')
        assert_detection('$("#foo").before(xss)')

        # https://api.jquery.com/after/
        assert_detection('$("#foo")["after"](xss)')
        assert_detection('$("#foo").after(xss)')

        # https://api.jquery.com/insertBefore/
        assert_detection('$(xss)["insertBefore"](target)')
        assert_detection('$(xss).insertBefore(target)')

        # https://api.jquery.com/insertAfter/
        assert_detection('$(xss)["insertAfter"](target)')
        assert_detection('$(xss).insertAfter(target)')

        # https://api.jquery.com/wrapInner/
        assert_detection('$("#foo")["wrapInner"](xss)')
        assert_detection('$("#foo").wrapInner(xss)')

        # https://api.jquery.com/wrap/
        assert_detection('$("#foo")["wrap"](xss)')
        assert_detection('$("#foo").wrap(xss)')

        # https://api.jquery.com/wrapAll/
        assert_detection('$("#foo")["wrapAll"](xss)')
        assert_detection('$("#foo").wrapAll(xss)')

    def test_multiple_lines(self):
        detections = analyse('\nvar a = 1;\n$("#foo").html(xss)\nvar b=2;$("#foo").html(xss)')
        self.assertEqual(2, len(detections))
        self.assertListEqual([(3, 1), (4, 9)], list(detections.keys()))
