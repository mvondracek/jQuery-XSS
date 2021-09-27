// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_11_31 = $;
var foo_11_31 = baz_11_31("#foo");
// data flow analysis required
foo_11_31.wrapInner(xss);
