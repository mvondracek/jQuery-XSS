// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_2_31 = $;
var foo_2_31 = baz_2_31("#foo");
// data flow analysis required
foo_2_31.prepend(xss);
