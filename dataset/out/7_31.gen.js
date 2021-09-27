// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_7_31 = $;
var foo_7_31 = baz_7_31("#foo");
// data flow analysis required
foo_7_31.after(xss);
