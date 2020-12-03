// vulnerable.html?foo=<script>alert("xss attack")</script>
var xss = new URLSearchParams(window.location.search).get('foo');
// ----------------------------------------------------------------------------
$( document ).ready(function() {
    $("#foo1").html(xss); // vulnerable
    $(
    'h2')
    [
    'html']
    (xss); // vulnerable
    $("#foo2").before(xss); // vulnerable, `prepend`, `after`, `appendTo`, ...
    var text = 'context aware $("#foo1").html(xss);';  // safe
    $("#foo3").html();  // safe
});
