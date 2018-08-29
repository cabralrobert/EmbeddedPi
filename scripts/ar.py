import time
from datetime import datetime
import os

def verifica(now):
	if (now.hour == 7):
		os.system("sudo irsend SEND_ONCE lg_ac ac_off")
		os.system("sudo irsend SEND_ONCE lg_ac ac_off")
		os.system("sudo irsend SEND_ONCE lg_ac ac_off")
		os.system("sudo irsend SEND_ONCE lg_ac ac_off")
		print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

while True:
	now = datetime.now()
	verifica(now)
	print "Em sleep por uma hora"
	time.sleep(3600)
