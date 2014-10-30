###FTP CSRF
- Found by Maksymilian Arciemowicz: http://securityreason.com/achievement_securityalert/56
- Using long FTP URLs, it is possible to perform CSRF attacks against FTP servers 
- E.g. <img src="ftp://site///////...../////SITE %20CHMOD%20777%20FILENAME">
- Command is truncated at 500 chars, rest of URL is interpreted as extra FTP command

Extracted from: http://www.slideshare.net/kuza55/same-origin-policy-weaknesses-1728474