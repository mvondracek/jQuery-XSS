// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_10_14 = {
    "wrap": function(x) {
        return x;
    }
};
$foo_10_14.wrap();
