import urllib.request, urllib.error
import time
import math

def query(url):
        res = urllib.request.urlopen(url)
        return res.read()

def Base_10_to_4(X):
    if (int(X/4)):
        return Base_10_to_4(int(X/4))+str(X%4)
    return str(X%4)

token = "5hIWHGFgjSrBsC2lXzyldrdtgdTjQnvz"


for k in range(32819, 4**8):
        num = Base_10_to_4(k).zfill(8)
        first = int(num[0]) 
        second = int(num[1])
        third = int(num[2]) 
        fourth = int(num[3])
        fifth = int(num[4]) 
        sixth = int(num[5])
        seventh = int(num[6]) 
        eighth = int(num[7])
        word = chr(65 + first)+ chr(65 + second) + chr(65 + third) + chr(65 + fourth) + chr(65 + fifth) + chr(65 + sixth) + chr(65 + seventh) + chr(65 + eighth)
        print(word)
        url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, word)
        result = query(url)
        print(result)
        time.sleep(0.2)
        
        
