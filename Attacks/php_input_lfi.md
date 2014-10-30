###php://input Local File Inclusion -> RCE Method
####Requires `allow_url_include` to be on.

Supposing that there is a local file inclusion vulnerability on a box running PHP, it may be possible to escalate the inclusion to remote command execution.

1. Locate the LFI, in this case: `http://example.com/lfi.php?file=../../../../etc/passwd%00`
2. Using a reverse proxy, or request intercepting tool, change the URL to the following: `http://example.com/lfi.php?file=php://input` and change the request to a `POST` request.
3. In the `POST` requests body, include the URL encoded command you wish to execute: e.g. `ls%20-lah`
4. Send the request, and view the source of the response for results.

Further reading:
[PHP Documentation on Wrappers](http://php.net/manual/en/wrappers.php.php)
[Exploiting PHP Local File Inclusion](http://websec.wordpress.com/2010/02/22/exploiting-php-file-inclusion-overview/)

