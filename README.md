# jQuery XSS Static Analyser 

[![Python version](https://img.shields.io/badge/Python-3-blue.svg?style=flat-square)](https://www.python.org/)
![Python package](https://github.com/mvondracek/jQuery-XSS/workflows/Python%20package/badge.svg)

Static analyser for JavaScript which can detect use of unsafe jQuery methods
which are vulnerable to XSS attack.

> By design, any jQuery constructor or method that accepts an HTML
> string — jQuery(), .append(), .after(), etc. — can potentially execute code.
> This can occur by injection of script tags or use of HTML attributes that
> execute code (for example, <img onload="">). Do not use these methods to
> insert strings obtained from untrusted sources such as URL query parameters,
> cookies, or form inputs. Doing so can introduce cross-site-scripting (XSS)
> vulnerabilities. Remove or escape any user input before adding content to
> the document.
>
> [jQuery API Documentation](https://api.jquery.com/html) 

## Example

For example, the analyser can parse following JavaScript code:
~~~js
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
~~~

and report unsafe use of jQuery methods as follows:

~~~shell script
$ ./jqueryxsscli.py --input ./examples/vulnerable.js
unsafe jQuery method call (5, 5)=`$("#foo1").html(xss)`
unsafe jQuery method call (6, 5)=`$('h2')['html'](xss)`
unsafe jQuery method call (11, 5)=`$("#foo2").before(xss)`
~~~

For more short examples, please see implemented unit tests ([`/tests`](/tests)).

## Help

~~~shell script
$ ./jqueryxsscli.py --help
~~~

# Coala Bear

This analyser is also available as a plugin for [Coala static analysis system](https://coala.io/).
Plugins for Coala are called [bears](https://github.com/coala/coala-bears)
and this *jQuery XSS Static Analyser* is released as `JSjQueryXssUnsafeBear`.

You can run Coala integrated in your favourite IDE or from CLI as follows:
~~~shell script
$ coala -I --flush-cache -f examples/vulnerable.js -d . -b JSjQueryXssUnsafeBear
Executing section cli...

examples\vulnerable.js
|   5| ····$("#foo1").html(xss);·//·vulnerable
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$("#foo1").html(xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0

examples\vulnerable.js
|   6| ····$(
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$('h2')['html'](xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0

examples\vulnerable.js
|  11| ····$("#foo2").before(xss);·//·vulnerable,·`prepend`,·`after`,·`appendTo`,·...
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$("#foo2").before(xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0
~~~

## Publication

This software was developed during research on ***TBA***.
Please see the paper for more details.

## Links

* OWASP Foundation. *Cheat Sheet Series: DOM based XSS Prevention Cheat Sheet*. 2020.
  Online. https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html

* OWASP Foundation. *DOM Based XSS*. 2020. Online.
  https://owasp.org/www-community/attacks/DOM_Based_XSS

* Röthlisberger, Thomas. *Risks of DOM Based XSS due to “unsafe” JavaScript
  functions*. 2013. Online. https://blog.compass-security.com/2013/01/dom-based-xss-unsafe-javascript-functions/

* Yuen Ho Wong, Jimmy. *Safe vs Unsafe jQuery Methods*. 2019. Online.
  https://coderwall.com/p/h5lqla/safe-vs-unsafe-jquery-methods 
 
