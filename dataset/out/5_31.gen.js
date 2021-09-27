// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_5_31 = $;
var foo_5_31 = baz_5_31("#foo");
// data flow analysis required
foo_5_31.appendTo(xss);
