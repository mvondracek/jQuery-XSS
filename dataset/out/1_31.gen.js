// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_1_31 = $;
var foo_1_31 = baz_1_31("#foo");
// data flow analysis required
foo_1_31.html(xss);
