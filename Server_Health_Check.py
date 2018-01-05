#Author: Ajin Abraham
import requests
import os
import threading
import time
import datetime

SELLRATE = 128000
OKBLUE = '\033[94m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

def health_check():
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    url = "https://google.com"
    try:
        r = requests.get(url) 
        if r.status_code != 200:
            print BOLD + FAIL + "["+st+"] Server Down"
            #os.system('echo "Server Down!"|espeak') # Linux , install espeak
            os.system("say Server Down!") #Mac
        else:
            print BOLD + OKBLUE + "Server Health Good!"
    except:
        pass
    threading.Timer(180, health_check).start()
health_check()
