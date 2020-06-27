# jQuery XSS Static Analyser 

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
var xss = '<script>alert("xss")</script>';
// ----------------------------------------------------------------------------
$("#foo1").html(xss); // vulnerable
$(
'h1')
[
'html']
(xss); // vulnerable
$("#foo2").before(xss); // vulnerable, `prepend`, `after`, `appendTo`, ...
var text = 'context aware $("#foo1").html(xss);';  // safe
$("#foo3").html();  // safe
$("#foo4").bar(baz); // safe
~~~

and report unsafe use of jQuery methods as follows:

~~~shell script
$ ./jqueryxsscli.py --input ./examples/vulnerable.js
unsafe jQuery method call (3, 1)=`$("#foo1").html(xss)`
unsafe jQuery method call (4, 1)=`$('h1')['html'](xss)`
unsafe jQuery method call (9, 1)=`$("#foo2").before(xss)`
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
|   3| $("#foo1").html(xss);·//·vulnerable
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$("#foo1").html(xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0

examples\vulnerable.js
|   4| $(
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$('h1')['html'](xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0

examples\vulnerable.js
|   9| $("#foo2").before(xss);·//·vulnerable,·`prepend`,·`after`,·`appendTo`,·...
|    | [NORMAL] JSjQueryXssUnsafeBear:
|    | unsafe jQuery method call `$("#foo2").before(xss)`
|    | *0: Do nothing
|    |  1: Open file(s)
|    |  2: Add ignore comment
|    | Enter number (Ctrl-Z to exit): 0
~~~

## Links

* OWASP Foundation. *Cheat Sheet Series: DOM based XSS Prevention Cheat Sheet*. 2020.
  Online. https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html

* OWASP Foundation. *DOM Based XSS*. 2020. Online.
  https://owasp.org/www-community/attacks/DOM_Based_XSS

* Röthlisberger, Thomas. *Risks of DOM Based XSS due to “unsafe” JavaScript
  functions*. 2013. Online. https://blog.compass-security.com/2013/01/dom-based-xss-unsafe-javascript-functions/

* Yuen Ho Wong, Jimmy. *Safe vs Unsafe jQuery Methods*. 2019. Online.
  https://coderwall.com/p/h5lqla/safe-vs-unsafe-jquery-methods 
 
