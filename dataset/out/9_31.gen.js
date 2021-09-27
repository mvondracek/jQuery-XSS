// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_9_31 = $;
var foo_9_31 = baz_9_31("#foo");
// data flow analysis required
foo_9_31.insertAfter(xss);
