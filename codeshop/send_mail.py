#-*- coding: UTF-8 -*-
#Filename = mail.py
#send_mail.send_mail(html(),"异常报警",['b.@qq.com','a@qq.com'])

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
logger = logging.getLogger()

mail_host="pointoverflow.com"
mail_user="jkant"
mail_pass="jkant520ye"



#to_list=['2433417924@qq.com','243517276@qq.com','7442104@qq.com']

def send_mail(content,sub,to):
    mess={}
    me=mail_user
    msg = MIMEText(content,_subtype='html',_charset='UTF-8')
    msg['Subject'] = Header(sub, 'UTF-8')
    msg['From'] =  Header(me, 'UTF-8')
    #msg['To'] = ";".join( to_list )
    msg['To'] = to
    try:
        #server = smtplib.SMTP()
        #server.connect(mail_host)
        server = smtplib.SMTP(mail_host,25)
        server.login(mail_user,mail_pass)
        #server.sendmail(me,msg['To'].split(','), msg.as_string())
        server.sendmail(me,to, msg.as_string())
        server.close()
        #logger.error(to)
        mess['status']=1
        mess['info']='OK'
        return mess
    except Exception as e:
        print(str(e))
        mess['status']=0
        mess['info']=str(e)
       # logger.error(e)
        return mess












