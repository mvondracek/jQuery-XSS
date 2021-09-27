// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_11_17 = 'context aware \
$("#foo1").wrapInner(xss); \
';
