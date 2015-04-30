###Leaking OAuth Tokens via Unsanitised Redirection Bugs

It is possible to steal the OAuth token for authentication flows, where the redirection URL can be controlled by the user. Many OAuth implementations do not do strong check on the redirection URL and hence it may be possible to redirect the user to a maliciously controlled host. This may lead to token disclosure.

Some tricks to bypass weak redirection filters include:

http://victim.com/something?next=http://victim.com.evil.com

http://victim.com/something?next=http://victim.com_.evil.com

http://victim.com/something?next=http://evil.com/victim.com

Whilst this particular trick is not well documented in this specific document, I would advise looking at:

[OAuth Security by Sakurity](http://www.oauthsecurity.com/)
[Common OAuth2 Bugs](http://homakov.blogspot.com.au/2012/07/saferweb-most-common-oauth2.html)
[Bugcollector Trick #1](http://bugscollector.com/tricks/1/)