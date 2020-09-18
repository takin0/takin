#coding=utf-8 
#读取加载配置文件global.ini
#读取配置文件的路径
import os,sys
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)

path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"/conf/"
path_load_ini=path_load_ini.replace('\\', '/')

from modules.mains import log
import configparser
'''
#from configparser import ConfigParser

cfgp=ConfigParser()
cfgp.read(path_load_ini+"global.ini")
#print(path_load_ini)

#全部章节
section = cfgp.sections()
#print(path_load_ini)

#某一章节的字段
option1=cfgp.options("browser")
#print(option1)

#某一字段的值
browser_path=cfgp.get("browser","browser_path")
driver_path=cfgp.get("browser","driver_path")
browser_kernel=cfgp.get("browser","browser_kernel")
#path_ide=cfgp.get("browser_path","ide")
#path_other=cfgp.get("browser_path","other")

email_smtpserver=cfgp.get("email","smtpserver")
email_username=cfgp.get("email","username")
email_password=cfgp.get("email","password")
email_from_addr=cfgp.get("email","from_addr")
email_to_addr=cfgp.get("email","to_addr")

#print(path_chrome)

'''
configpath=path_load_ini+"global.ini"
class ReadConfig:

    def __init__(self,filepath=path_load_ini+"global.ini"):
    
        self.cfgp = configparser.ConfigParser()
        self.cfgp.read(filepath)

    def get_brscf(self,param):
        value = self.cfgp.get("browser",param)
        return value

    def get_emcf(self,param):
        value = self.cfgp.get("email",param)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_brscf("browser_path")
    print(t)

