// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_12_31 = $;
var foo_12_31 = baz_12_31("#foo");
// data flow analysis required
foo_12_31.wrapAll(xss);
