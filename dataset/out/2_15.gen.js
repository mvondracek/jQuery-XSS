// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_2_15 = {
    "prepend": function(x) {
        return x;
    }
};
$foo_2_15["prepend"](xss);
