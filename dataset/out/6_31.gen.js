// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_6_31 = $;
var foo_6_31 = baz_6_31("#foo");
// data flow analysis required
foo_6_31.before(xss);
