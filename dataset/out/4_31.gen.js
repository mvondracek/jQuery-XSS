// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var baz_4_31 = $;
var foo_4_31 = baz_4_31("#foo");
// data flow analysis required
foo_4_31.append(xss);
