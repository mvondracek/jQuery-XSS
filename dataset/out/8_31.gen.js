// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_8_31 = $;
var foo_8_31 = baz_8_31("#foo");
// data flow analysis required
foo_8_31.insertBefore(xss);
