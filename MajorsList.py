import urllib
import time
import math
import itertools

def query(url):
        res = urllib.urlopen(url)
        return res.read()


token = "5hIWHGFgjSrBsC2lXzyldrdtgdTjQnvz"

comb = [
'ABACDBBB','AACDADDA','ABBDAACA','AADCACDD','CAAAADDA','ABACCDCC','ABACCBDC','DDDDDAAC','DDDDDAAB','DDDDCDCB','DDDDCBAB','DDDDBCCD',
'AADCCADB','AADCCCAD','AADCDAAA','AADCDAAB','ABABDACB','AADCDADD','AADCDBDB',
'AADCDCDB',
'AADDACDD',
'AADDBBAC',
'AADDBBAD',
'AADDBCCD',
'AADDCBAB','ABBCDBBA',
'AADDCDAD','ABBCBCDC',
'AADDDCDC','ABBCACCA',
'ABAAAADD','ABBADDBC',
'ABAABABD','ABAABBDD','ABAACBDD','ABAACCDC','ABABAABC','ABABACAA','ABABADCB','ABABBAAB',
'ABABBCDB','ABABDDDA','ABACABDD','ABACADDD','ABACBACD','ABBABBAD',
'ABACBDBD','ABACDDAD','ABADACBC','ABADADDA', 'ABADBCDB','ABADCBCC','ABADCDAD','ABBAACBD',
'ABBACAAD','ABBADADD','ABBADCAC','ABBBCDAC']

for v in itertools.permutations(comb,6):
    word = v[0]+v[1]+v[5]+v[2]+v[4]+v[3]+"CA"
    
#        num = Base_10_to_4(k).zfill(8)
#        word = chr(65 + first)+ chr(65 + second) + chr(65 + third) + chr(65 + fourth) + chr(65 + fifth) + chr(65 + sixth) + chr(65 + seventh) + chr(65 + eighth)
    url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, word)
    result = query(url)
    print(result)
    time.sleep(0.2)
        

