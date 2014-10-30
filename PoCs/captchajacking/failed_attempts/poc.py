import requests
import cherrypy
import re
from random import choice
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *

  
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  
  
url = 'http://www.reddit.com/register'  
r = Render(url)  
html = r.frame.toHtml()
ualist= [line.rstrip() for line in open('useragents.txt')]
headers = {
    'User-Agent': '{0}'.format(choice(ualist)),
}
cap_recomp = re.compile(r'captcha/[a-zA-Z0-9.png]*')
cap_iden = re.compile(r'value="[A-Za-z0-9]{32}')
captchaf = cap_recomp.search(html)
captchai = cap_iden.search(html)
cident = captchai.group()
cident = cident.replace("value=\"", "")
print cident
cfilename = captchaf.group()
cfilename1 = captchaf.group()
cap_file = cfilename1.replace("/","")
captchaURL = "http://www.reddit.com/" + cfilename
s = requests.Session()
print captchaURL
with open(str(cap_file), 'wb') as handle:
    request = s.get(captchaURL, headers=headers, stream=True)

    for block in request.iter_content(1024):
        if not block:
            break

        handle.write(block)
# class poc:
#     def index(self):
#         return "Hello world!"
#     index.exposed = True

# cherrypy.quickstart(poc())