###XSS vectors in file names
####Sneaky!

Many web application developers seem to forget to sanitise user uploaded file names. This is because, XSS attacks via file names are not well known and, to be honest, unexpected. On linux, it is easy to create a file which contains the special characters needed in order to trigger XSS on a page. On windows, the file system will restrict you from such creations and hence, it is easier to merely edit the file name when intercepting the file upload request.

on Linux:

`touch '<img src = x onerror=alert(1)>.jpeg'`

On Windows (when intercepting requests):

`Content-Disposition: form-data; name="upload[0]"; filename=""><img src = x onerror=alert(1)>"`

Further Reading:
[Bugscollector Link](http://bugscollector.com/tricks/4/)
[Google Adwords Stored XSS Link](http://c0rni3sm.blogspot.ru/2013/12/google-adwords-stored-xss-from-nay-to.html)