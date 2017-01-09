__author__ = 'rollin'

import smtplib
import time
import os

from email.mime.text import MIMEText
from email.header import Header

class SendMail:

	def send_mail(file_new):
		f = open(file_new, 'rb')
		mail_body = f.read()
		f.close()

		msg =  MIMEText(mail_body, 'html', 'utf-8')
		msg['Subject'] = Header("auto test report", 'utf-8')

		sender = 'rollin.r.ma@gmail.com'
		receivers = ['rollin.r.ma@gmail.com']

		mail_host="smtp.gmail.com"
		mail_user="rollin.r.ma"
		mail_pass="xxxxxx"

		try:
		    smtpObj = smtplib.SMTP()
		    smtpObj.connect(mail_host, 587)
		    smtpObj.login(mail_user,mail_pass)
		    smtpObj.sendmail(sender, receivers, msg.as_string())
		    print "sed"
		except smtplib.SMTPException:
		    print "Error"
