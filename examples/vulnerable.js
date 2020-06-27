var xss = '<script>alert("xss")</script>';
// ----------------------------------------------------------------------------
$("#foo1").html(xss); // vulnerable
$(
'h1')
[
'html']
(xss); // vulnerable
$("#foo2").before(xss); // vulnerable, `prepend`, `after`, `appendTo`, ...
var text = 'context aware $("#foo1").html(xss);';  // safe
$("#foo3").html();  // safe
$("#foo4").bar(baz); // safe
