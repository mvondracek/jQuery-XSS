// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_7_10 = {
    "after": function(x) {
        return x;
    }
};
foo_7_10.after();
