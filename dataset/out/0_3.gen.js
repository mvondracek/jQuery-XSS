// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_0_3 = 1;
var bar_0_3 = 2;
var baz_0_3 = foo_0_3 + bar_0_3;
foo_0_3 = baz_0_3 + 1;
