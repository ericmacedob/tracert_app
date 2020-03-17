from traceroute import Traceroute
import sys
import os
import socket
from list import baselineArr

x = False
ip = ""

def ipValid(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

val = str(raw_input("Would you like to add an IP to the baseline before running the program?[y/n]: "))

while(x==False):
	if(val=="n" or val=="N"):
		x = True
	if(val=="y" or val=="Y"):
		ip = str(raw_input("Please enter new IP: "))
		x = ipValid(ip)
		if (x==False):
			print("Invalid IP, please try again.")
		if (x==True):
			baselineArr.append(ip)
			for i in baselineArr:
				os.system("sudo python traceroute.py --country='LO' --ip_address=" + i + " -n | grep -v ""rtt"" > ./baseline/" + i)

for i in baselineArr:
	os.system("sudo python traceroute.py --country='LO' --ip_address=" + i + " -n | grep -v ""rtt"" > tmp.txt")
	with open('tmp.txt','r') as tmp:
		a = tmp.read()
	with open('./baseline/%s' % i,'r') as base:
		b = base.read()
	if(a==b):
		print(i + ": same route as baseline")
	else:
		print(i + ": Warning, different route from baseline!")
