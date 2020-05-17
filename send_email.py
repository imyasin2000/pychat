# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
# setup the parameters of the message
password = [97, 109, 105, 110, 109, 104, 102, 97]
password=''.join(chr(i) for i in password)
msg['From'] = "messenger.verify.py@gmail.com"
#message
msg['To'] = "mhfa1380@gmail.com"
msg['Subject'] = "Subscription"
import random
random_number=(random.randint(100000,1000000))
message = (f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 🅿🆈🆃🅷🅾🅽 🅼ⓔ🆂🆂ⓔ🅽🅶ⓔ🆁.\n\n\n𝔂𝓸𝓾𝓻𝓮 𝓬𝓸𝓭𝓮 𝓲𝓼 : {random_number} .") 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 

#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail
server.login(msg['From'], password)
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("successfully sent email to %s:" % (msg['To']))
