import matplotlib
matplotlib.use('Agg')
import mysql.connector
import matplotlib.pyplot as plt

#x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#y = [25.6,26.3,28.2,28.9,29.1,29.3,29.4,29.5,29.7,29.8,29.8,29.9,29.9,29.9,30.0]

#my_xticks = ['20:03','20:13','20:23','20:33','20:43','20:53','21:03','21:13','21:23','21:33','21:43','21:53','22:03','22:13','22:23']

x = []
y = []
my_xticks = []
aux = 1

try:
	conn = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='embeddedpi')
	if conn is not None:
		print "Conectado"
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM valores")
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
plt.ylabel("Temperatura")
plt.savefig('/home/pi/EmbeddedPi/scripts/graph/temp.png')
