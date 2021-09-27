// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_9_9 = {
    "insertAfter": function(x) {
        return x;
    }
};
foo_9_9.insertAfter(xss);
