// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_11_10 = {
    "wrapInner": function(x) {
        return x;
    }
};
foo_11_10.wrapInner();
