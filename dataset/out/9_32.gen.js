// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

// taint analysis required
xss = "safe";
$("#foo").insertAfter(xss);
