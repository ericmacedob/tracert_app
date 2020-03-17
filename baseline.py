from traceroute import Traceroute
import sys
import os
from list import baselineArr

for i in baselineArr:
	os.system("sudo python traceroute.py --country='LO' --ip_address=" + i + " -n | grep -v ""rtt"" > ./baseline/" + i)

	#sudo python traceroute.py --country='LO' --ip_address=199.232.37.67 -n | grep -v "rtt"  > ./baseline/199.232.37.67


	#print("python traceroute.py --country='LO' --ip_address= " + i + " --tmp_dir=./baselines -n | grep -v ""rtt""")
