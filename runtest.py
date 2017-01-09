#!/usr/bin/python
#coding:utf-8
__author__ = 'rollin'

import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from mail.smail import SendMail

from HTMLTestRunner import HTMLTestRunner

test_dir = './'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

def send_mail(file_new):
		f = open(file_new, 'rb')
		mail_body = f.read()
		f.close()

		msg =  MIMEText(mail_body, 'html', 'utf-8')
		msg['Subject'] = Header("auto test report", 'utf-8')

		sender = 'rollin.r.ma@gmail.com'
		receivers = ['rollin.r.ma@gmail.com']

		mail_host="smtp.gmail.com"
		mail_user="username"
		mail_pass="passwd"

		try:
		    smtpObj = smtplib.SMTP()
		    smtpObj.connect(mail_host, 25)
		    smtpObj.login(mail_user,mail_pass)
		    smtpObj.sendmail(sender, receivers, msg.as_string())
		    print "sed"
		except smtplib.SMTPException:
		    print "Error"

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #filename = test_dir + "/" + now + 'result.html'
    filename =  test_dir + "/" + 'result.html'
    fp = open(filename, 'wb')
    #runner = unittest.TextTestRunner()
    #runner = HTMLTestRunner(stream=fp, title="自动巡检测试报告", description="用例测试情况")
    runner = HTMLTestRunner(stream=fp, title="auto check test report", description="test case execute")
    runner.run(discover)
    fp.close()

    file_new = filename
    print(file_new)

    #send mail
    send_mail(file_new)