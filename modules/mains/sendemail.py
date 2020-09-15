#coding=utf-8 
import os,sys,smtplib,zipfile
from email.utils import formataddr
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep

path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)
from modules.mains import log
from modules.mains.new_report import newreport
from modules.mains.load_ini import email_smtpserver,email_username,email_password,\
email_from_addr,email_to_addr

def send_mail():
    source_dir=newreport()#查找最新报告的路径
    source_dir=source_dir[0]#打包报告的路径 
    output_filename=source_dir+'.zip'#打包后的存放路径
    #打包测试报告
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()
    #寄件邮箱
    smtpserver = email_smtpserver
    from_addr = email_username
    password = email_password
    port=587

    #附件路径及文件名
    report=newreport()#再次调用查找打包好的文件
    file_name=report[1]#打包后的文件名
    file=report[0]#打包后的路径
    #print(file_name)
    #print(file)
    #邮件主题
    subject = '测试报告'
    #收件人
    to_addr = email_to_addr
    #创建附件实例
    mg = MIMEMultipart()
    mg['Subject'] = subject
    mg['From'] = formataddr(["自动化测试程序",from_addr])
    mg.attach(MIMEText('您好，本次自动化测试已结束，测试报告以附件形式发送，请查阅！', 'plain', 'utf-8'))
    fj= MIMEApplication(open(file,'rb').read())
    fj.add_header('Content-Disposition','attachment',filename=file_name)
    mg.attach(fj)

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
        os.remove(report[0])#将打包的文件删除
    except smtplib.SMTPException:
        print ("发送邮件失败")

if __name__=='__main__':
        send_mail()
