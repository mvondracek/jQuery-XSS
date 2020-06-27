# jQuery XSS Static Analyser 

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

## Help

```bash
$ ./jqueryxsscli.py --help
```

## Links

* OWASP Foundation. *Cheat Sheet Series: DOM based XSS Prevention Cheat Sheet*. 2020.
  Online. https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html

* OWASP Foundation. *DOM Based XSS*. 2020. Online.
  https://owasp.org/www-community/attacks/DOM_Based_XSS

* Röthlisberger, Thomas. *Risks of DOM Based XSS due to “unsafe” JavaScript
  functions*. 2013. Online. https://blog.compass-security.com/2013/01/dom-based-xss-unsafe-javascript-functions/

* Yuen Ho Wong, Jimmy. *Safe vs Unsafe jQuery Methods*. 2019. Online.
  https://coderwall.com/p/h5lqla/safe-vs-unsafe-jquery-methods 
 
