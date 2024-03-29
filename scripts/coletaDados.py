import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import mysql.connector
import time
from datetime import datetime

sensor = Adafruit_DHT.DHT22 
GPIO.setmode(GPIO.BOARD)
pino_sensor = 23

def inserir(valor,tabela,cursor):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
 
	if tabela == "valores":
		cursor.execute("INSERT INTO valores (hora,valor) values ('" + dt_string + "','" + str("%.1f" % valor) + "');")
	elif tabela == "umidade":
		cursor.execute("INSERT INTO umidade (hora,valor) values ('" + dt_string + "','" + str("%.1f" % valor) + "');")

def delete(tabela,cursor):
	if tabela == "valores":
		cursor.execute("SELECT MIN(id) FROM valores;")
		idv = cursor.fetchone()[0]
		cursor.execute("DELETE FROM valores where id = %s;" % (idv))
	elif tabela == "valores2":
		cursor.execute("SELECT MIN(id) FROM valores2;")
		idv = cursor.fetchone()[0]
		cursor.execute("DELETE FROM valores2 where id = %s;" % (idv))
	elif tabela == "umidade":
		cursor.execute("SELECT MIN(id) FROM umidade;")
		idu = cursor.fetchone()[0]
		cursor.execute("DELETE FROM umidade where id = %s;" % (idu))
		#cursor.execute("DELETE FROM umidade where id = (SELECT MIN(id) FROM umidade);")

def ler():
	aux = 0
	while aux == 0:
		umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
		if umid is not None and temp is not None:
			if umid > 100:
				print "Falha ao ler"
			else:
				print "Temperatura = ",temp,  " Umidade = ", umid; 
				aux = 1;
		else:
			print("Falha ao ler dados do DHT11 !!!")

	try:
		conn = mysql.connector.connect(user='robertc', password='9346',host='127.0.0.1',database='embeddedpi')
		if conn is not None:
			print "Conectado!!"
		    	cursor = conn.cursor()
#                        inserir(temp, "valores2",cursor)

			cursor.execute("SELECT COUNT(*) FROM valores")
			if cursor.fetchone()[0] == 15:
				delete("valores",cursor)
				delete("umidade",cursor)
				inserir(temp,"valores",cursor)
				inserir(umid,"umidade",cursor)
				print time.strftime('%H:%M') 
			else:
				inserir(temp,"valores",cursor)
				inserir(umid,"umidade",cursor)
				print time.strftime('%H:%M') 

			conn.commit()
			cursor.close()
			conn.close()
	except Exception as e:
		print e


ler()
print "Fim da execucao!"
