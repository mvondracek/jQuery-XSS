# jQuery XSS Static Analyser

[![Python version](https://img.shields.io/badge/Python-3-blue.svg?style=flat-square)](https://www.python.org/)
[![Python application](https://github.com/mvondracek/jQuery-XSS/actions/workflows/python-app.yml/badge.svg)](https://github.com/mvondracek/jQuery-XSS/actions/workflows/python-app.yml)

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

For more short examples, please see implemented unit tests ([`/tests`](/tests))
and [our dataset of unsafe jQuery method calls](/dataset).

## Help

~~~shell script
$ ./jqueryxsscli.py --help
~~~

## Coala Bear

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

## Dataset

To evaluate abilities of our analyser and to compare it with other tools,
we created [our dataset of unsafe jQuery method calls](/dataset).

## Publication

This software was developed during research on
[Rise of the Metaverse's Immersive Virtual Reality Malware and the Man-in-the-Room Attack & Defenses](https://www.sciencedirect.com/science/article/pii/S0167404822003157).
Please see the paper for more details and use following citation.

~~~BibTeX
@article{Vondracek-2023-102923,
    title = {Rise of the Metaverse’s Immersive Virtual Reality Malware and the Man-in-the-Room Attack & Defenses},
    journal = {Computers \& Security},
    volume = {127},
    pages = {102923},
    year = {2023},
    issn = {0167-4048},
    doi = {https://doi.org/10.1016/j.cose.2022.102923},
    url = {https://www.sciencedirect.com/science/article/pii/S0167404822003157},
    author = {Martin Vondráček and Ibrahim Baggili and Peter Casey and Mehdi Mekni}
}
~~~

## License

- [MIT](./LICENSE-MIT) for `jqueryxss`,
- [AGPL-3.0](./LICENSE-AGPL-3.0) for `JSjQueryXssUnsafeBear.py`, because it is a plugin for [Coala](https://github.com/coala/coala) which [is available under AGPL-3.0](https://github.com/coala/coala/blob/master/LICENSE).

## Links

- OWASP Foundation. *Cheat Sheet Series: DOM based XSS Prevention Cheat Sheet*. 2020.
  Online. https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html
- OWASP Foundation. *DOM Based XSS*. 2020. Online.
  https://owasp.org/www-community/attacks/DOM_Based_XSS
- Thomas Röthlisberger. *Risks of DOM Based XSS due to “unsafe” JavaScript
  functions*. 2013. Online. https://blog.compass-security.com/2013/01/dom-based-xss-unsafe-javascript-functions/
- Jimmy Yuen Ho Wong. *Safe vs Unsafe jQuery Methods*. 2019. Online.
  https://coderwall.com/p/h5lqla/safe-vs-unsafe-jquery-methods 
- [UNHcFREG, *BigScreen and Unity Virtual Reality Attacks and the Man in The Room Attack*](https://www.unhcfreg.com/single-post/2019/02/19/bigscreen-and-unity-virtual-reality-attacks)
- [University of New Haven, *University of New Haven Researchers Discover Critical Vulnerabilities in Popular Virtual Reality Application*](https://www.newhaven.edu/news/releases/2019/discover-vulnerabilities-virtual-reality-app.php)
- Martin Vondráček, Ibrahim Baggili, Peter Casey, and Mehdi Mekni.
  *Rise of the Metaverse's Immersive Virtual Reality Malware and
  the Man-in-the-Room Attack & Defenses*. Computers \& Security.
  vol. 127. p. 102923. 2023. Online.
  https://www.sciencedirect.com/science/article/pii/S0167404822003157
