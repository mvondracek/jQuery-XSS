// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_1_14 = {
    "html": function(x) {
        return x;
    }
};
$foo_1_14.html();
