// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_10_31 = $;
var foo_10_31 = baz_10_31("#foo");
// data flow analysis required
foo_10_31.wrap(xss);
