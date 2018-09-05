import smtplib
import os

from email.message import Message
import email.message

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.message import MIMEMessage

fromaddr = "piembedded@gmail.com"
toaddr = "robertcabral@alu.ufc.br"
passwd = "raspberry0w"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, passwd)

msg = MIMEMultipart()
#msg = email.message.Message()
msg['From'] = "EmbeddedPi"
msg['To'] = toaddr
msg['Subject'] = "Embedded Pi - Features"

msg.add_header('Content-Type', 'text/html')

init = """
<html><head><meta name="viewport" content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no"><title>Embedded Pi - Features</title><style type="text/css"> a {color: #d80a3e;}body, #header h1, #header h2, p {margin: 0; padding: 0;} #main {border: 1px solid #cfcece;} img {display: block;} #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; } #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; } #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  } h5 {margin: 0 0 0.8em 0;} h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }h2 {color: #000000 !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0;} p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}</style></head>
"""

msg.attach(MIMEText(init, 'html'))

meio = """
<body><table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td><table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff"><tr><td><table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9"><tr><td width="570" align="center"  bgcolor="#00000000"><h1>Embedded Pi - Features</h1></td></tr></table></td></tr><tr><td><table id="content-3" cellpadding="0" cellspacing="0" align="center"><tr><h2>Historico de Temperatura</h2><img src="cid:temp" />
"""

msg.attach(MIMEText(meio, 'html'))

img = open('/home/pi/EmbeddedPi/scripts/graph/temp.png', 'rb').read()
msgImg = MIMEImage(img, 'png')
msgImg.add_header('Content-ID', '<temp>')
msgImg.add_header('Content-Disposition', 'inline', filename='temp.png')
msg.attach(msgImg)

meio2 = """
<h2>Historico de Umidade</h2><img src="cid:umidade" />
"""

msg.attach(MIMEText(meio2, 'html'))

img = open('/home/pi/EmbeddedPi/scripts/graph/umidade.png', 'rb').read()
msgImg = MIMEImage(img, 'png')
msgImg.add_header('Content-ID', '<umidade>')
msgImg.add_header('Content-Disposition', 'inline', filename='temp.png')
msg.attach(msgImg)

fim = """
</tr></table></td></tr></table><table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center"><tr><td align="center"><p>Embedded Pi - 2018</p></td></tr></table><!-- top message --></td></tr></table><!-- wrapper --></body></html>
"""

msg.attach(MIMEText(fim, 'html'))

print("sending mail...")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
print("mail sent!")
