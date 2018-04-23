import RPi.GPIO as GPIO
import sys

if(len(sys.argv) != 3):
	print "Erro, digite todos os argumentos";
	exit()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]),GPIO.OUT)

if int(sys.argv[2]) == 0:
	GPIO.output(int(sys.argv[1]),GPIO.LOW)
else:
	GPIO.output(int(sys.argv[1]),GPIO.HIGH)
