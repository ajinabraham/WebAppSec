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
    url: '${user_input}',
  });

```

```
const response = await fetch(`${user_input}/api/token=1212121233`, {
  });
```

```
request.get(`${user_input}/redirect=${user_input2}`)
```

## Sensitive Data Exposure Next.js

```
// Not suitable for server side secrets
publicRuntimeConfig: {
		AWS_API: process.env.AWS_API,
    GITHUB_TOKEN: process.env.GITHUB_TOKEN ,
	}
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
