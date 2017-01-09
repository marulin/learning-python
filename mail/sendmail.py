import smtplib

from email.mime.text import MIMEText
from email.header import Header

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.gmail.com"
mail_user="rollin.r.ma@gmail.com"
mail_pass="xxxxxx"
# port 465 for send
# imap.exmail.qq.com(993)

sender = 'rollin.r.ma@gmail.com'
receivers = ['rollin.r.ma@gmail.com']

message = MIMEText('Python ...', 'plain', 'utf-8')
message['From'] = Header("", 'utf-8')
message['To'] = Header("", 'utf-8')

subject = 'Python SMTP'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "sed"
except smtplib.SMTPException:
    print "Error"



