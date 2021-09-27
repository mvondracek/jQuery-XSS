// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_6_13 = {
    "before": function(x) {
        return x;
    }
};
$foo_6_13.before(xss);
