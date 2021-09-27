// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_3_31 = $;
var foo_3_31 = baz_3_31("#foo");
// data flow analysis required
foo_3_31.prependTo(xss);
