import os

d = os.path.dirname(os.path.abspath(__file__))
p = Path("/usr/local/bin/brute")

os.system("chmod +x bru")
if p.is_file():
 print("Writing.....")
else:
  os.system("sudo mkdir /usr/local/bin/brute")

os.system("sudo mv bru /usr/local/bin")
os.system("sudo mv psw.txt /usr/local/bin/brute")
os.system("sudo ln -s /usr/local/bin/brute/psw.txt "+d)
os.system("sudo ln -s /usr/local/bin/brute/bru "+d)
print "Installation Successfull.\nYou can access the file by typing bru"
