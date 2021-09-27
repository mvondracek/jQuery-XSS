// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_5_15 = {
    "appendTo": function(x) {
        return x;
    }
};
$foo_5_15["appendTo"](xss);
