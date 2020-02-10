from ftplib import FTP
import sys
import os 
import threading
import time
from termcolor import colored

print (colored('hello', 'red'), colored('world', 'green'))

if len(sys.argv) == 2:
	filename = sys.argv[1]
	if not os.path.isfile(filename):
		print ('[-] ' + filename + ' does not exist.')
		exit(0)
		if not os.access(filename, os.R_OK):
			print ('[-] ' + filename + ' access denied.')
			exit(0)
print ('[+] Reading-------------[+]: ' + filename)

count = len(open(filename).readlines( ))
print(count)
print_lock = threading.Lock()

f =open(filename);

def anonlogin():
	for i in f.readlines():
		s = i.strip('\n')
		#print(s)
		#print(s)
		try:
			print("[+] trying host " +s )
			ftp = FTP(s)
			
			ftp.login('anonymous','anonymous')
			ENDC = '\033[m' # reset to the defaults
			with print_lock:
				#print (colored('hello', 'red')
				print(colored("[+]"+ s+"  " +" anonymous login suceesful",'green'))
				ftp.quit()
		except Exception as e:
			with print_lock:
				print (colored('\n[-] ' + str(s) +' FTP Anonymous Logon Failed.',"red"))
				pass


for i in range(count):

	t= threading.Thread(target= anonlogin)
	
	
	t.start()

	

