// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_12_16 = {
    "wrapAll": function(x) {
        return x;
    }
};
$foo_12_16["wrapAll"]();
