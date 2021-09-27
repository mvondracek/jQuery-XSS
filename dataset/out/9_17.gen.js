// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_9_17 = 'context aware $("#foo1").insertAfter(xss);';
