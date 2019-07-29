#coding:utf-8
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from time import sleep

from email import encoders
import os

path_report=os.path.dirname(os.path.dirname(os.path.abspath('.')))+"\\report\\123.doc"
import sys
sys.path.append("..\..")
from modules.mains.load_ini import email_smtpserver,email_username,email_password,\
email_from_addr,email_to_addr

#寄件邮箱
smtpserver = email_smtpserver
from_addr = email_username
password = email_password
port=587

#附件路径及文件名
base_dir= os.path.dirname(os.path.dirname(os.path.abspath('.')))
file_name="login.png"
file=base_dir+"\\report\\"+file_name


#邮件主题
subject = '运行平台测试报告'
#收件人
to_addr = email_to_addr

#创建附件实例
mg = MIMEMultipart()

mg['Subject'] = subject
mg['From'] = formataddr(["自动化测试程序",from_addr])#("自动化测试程序",'utf-8')
#mg['To'] = ','.join(to_addr)
#正文
mg.attach(MIMEText('您好，本次自动化测试已结束，测试报告以附件形式发送，请查阅！', 'plain', 'utf-8'))
#图片附件

fj= MIMEApplication(open(file,'rb').read())
fj.add_header('Content-Disposition','attachment',filename=file_name)
mg.attach(fj)

'''
with open(file, 'rb') as f:
    
    mime = MIMEBase('image', 'png', filename='tp.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='tp.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:

mg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
'''

try:
    smtpObj = smtplib.SMTP(smtpserver,port,timeout=20)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(from_addr,password)
    sleep(2)
    smtpObj.sendmail(from_addr, to_addr .split(","), mg.as_string())
    sleep(2)
    smtpObj.quit()
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("发送邮件失败")

