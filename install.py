import os

d = os.path.dirname(os.path.abspath(__file__))

os.system("chmod +x "+d+"/bru")
if os.path.exists("/usr/local/bin/brute"):
 print("Updating Folder.....")
else:
  os.system("sudo mkdir /usr/local/bin/brute")

os.system("sudo mv "+d+"/bru /usr/local/bin")
os.system("sudo mv "+d+"/psw.txt /usr/local/bin/brute")
os.system("sudo ln -s /usr/local/bin/brute/psw.txt "+d)
os.system("sudo ln -s /usr/local/bin/brute/bru "+d)
print "BruteForce Installation Successfull.\nYou can access the file by typing bru from any directory"
