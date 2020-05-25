from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# create message object instance
def send_email_c(send_c):
# setup the parameters of the message
    password = [97, 109, 105, 110, 109, 104, 102, 97]
    password=''.join(chr(i) for i in password)
    msg = MIMEMultipart()
    msg['From'] = "messenger.verify.py@gmail.com"
    #message
    msg['To'] = send_c
    msg['Subject'] = "Subscription"
    import random
    random_number=(random.randint(100000,1000000))
    message = (f"\nHi Dear {send_c}.\n\n\n𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 🅿🆈🆃🅷🅾🅽 🅼ⓔ🆂🆂ⓔ🅽🅶ⓔ🆁.\n\n\n𝔂𝓸𝓾𝓻𝓮 𝓬𝓸𝓭𝓮 𝓲𝓼 : {random_number} .")
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
    return (1)
