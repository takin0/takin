#coding=utf-8 
#读取加载配置文件global.ini
#读取配置文件的路径
import os

path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"/conf/"
path_load_ini=path_load_ini.replace('\\', '/')
from modules.mains import log
from configparser import ConfigParser

cfgp=ConfigParser()
cfgp.read(path_load_ini+"global.ini")
#print(path_load_ini)

#全部章节
section = cfgp.sections()
#print(path_load_ini)

#某一章节的字段
option1=cfgp.options("browser_path")
#print(option1)

#某一字段的值
path_chrome=cfgp.get("browser_path","chrome")
path_firefox=cfgp.get("browser_path","firefox")
path_ie=cfgp.get("browser_path","ie")
path_ide=cfgp.get("browser_path","ide")
path_other=cfgp.get("browser_path","other")

email_smtpserver=cfgp.get("email","smtpserver")
email_username=cfgp.get("email","username")
email_password=cfgp.get("email","password")
email_from_addr=cfgp.get("email","from_addr")
email_to_addr=cfgp.get("email","to_addr")

#print(path_chrome)



