import time
from datetime import datetime
import os

def verifica(now):
	os.system("sudo irsend SEND_ONCE lg_ac ac_off")
	os.system("sudo irsend SEND_ONCE lg_ac ac_off")
	os.system("sudo irsend SEND_ONCE lg_ac ac_off")
	os.system("sudo irsend SEND_ONCE lg_ac ac_off")
	print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

now = datetime.now()
verifica(now)
