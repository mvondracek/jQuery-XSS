// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var foo_3_12 = {
    "prependTo": function(x) {
        return x;
    }
};
foo_3_12["prependTo"]();
