import Adafruit_DHT
import RPi.GPIO as GPIO
import time
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 23
 

aux = 0
while aux == 0:

	umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
	if umid is not None and temp is not None:
		if(not umid > 100):
			print str(int(temp)) + "|" + str(int(umid))
			aux = 1
		else:
			aux = 0
	else:
		aux = 0
