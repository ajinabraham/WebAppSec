### The `php://filter` LFD Method
####LFD as it allows for an attacker to view raw source, not include the files

By using the php://filter vector `php://filter/convert.base64-encode/resource=resource.php` the server will return to us, the base64 encoding of the file resource.php.

By returning the base64 instead of the raw contents, resource.php is not included, but rather, its source can be obtained by decoding the base64.

This trick is especially useful when traditional PHP Local File Inclusion methods are blocked off by WAFs or blacklisted.

Further Reading:

[Interesting LFI Method](http://diablohorn.wordpress.com/2010/01/16/interesting-local-file-inclusion-method/)
[LFI and RFI Cheatsheet](http://websec.wordpress.com/2010/02/22/exploiting-php-file-inclusion-overview/)