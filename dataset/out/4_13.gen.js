// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get("foo");

// ----------------------------------------------------------------------------

var $foo_4_13 = {
    "append": function(x) {
        return x;
    }
};
$foo_4_13.append(xss);
