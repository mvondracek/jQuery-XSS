// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_8_9 = {
    "insertBefore": function(x) {
        return x;
    }
};
foo_8_9.insertBefore(xss);
