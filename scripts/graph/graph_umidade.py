import matplotlib
matplotlib.use('Agg')
import mysql.connector
import matplotlib.pyplot as plt

x = []
y = []
my_xticks = []
aux = 1

try:
	conn = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='embeddedpi')
	if conn is not None:
		print "Conectado"
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM umidade")
		results = cursor.fetchall()
		for row in results:
			y.append(row[2])
			x.append(aux)
			my_xticks.append(row[1])
			aux += 1
		cursor.close()
		conn.close()
		
except Exception as e:
	print e


plt.xticks(x, my_xticks,rotation=45, rotation_mode="anchor",ha="right")
plt.plot(x,y,'bo-') 
plt.xlabel("Hora") 
plt.ylabel("Umidade")
plt.savefig('/home/pi/EmbeddedPi/scripts/graph/umidade.png')
