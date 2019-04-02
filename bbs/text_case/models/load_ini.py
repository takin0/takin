#读取加载配置文件global.ini
from configparser import ConfigParser

import os

#读取配置文件的路径
path_load_ini = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('.'))))


cfgp = ConfigParser()
cfgp.read(path_load_ini+"/global.ini")
'''
#全部章节
section = cfgp.sections()
print(section)

#某一章节的全部字段
options=cfgp.options(section[0:1])
print(options)

#某一章节的字段
option=cfgp.options("webdriver_path")
print(options)
'''
#某一字段的值
path_chrome=cfgp.get("webdriver_path","chrome")
path_firefox=cfgp.get("webdriver_path","firefox")
path_ie=cfgp.get("webdriver_path","ie")
path_ide=cfgp.get("webdriver_path","ide")
path_qq=cfgp.get("webdriver_path","qq")

mgmt_host=cfgp.get("mgmt","host")
mgmt_port=cfgp.get("mgmt","port")
mgmt_user=cfgp.get("mgmt","user")
mgmt_password=cfgp.get("mgmt","password")

kong_IP=cfgp.get("kong","IP")
kong_EndPoint=cfgp.get("kong","EndPoint")
kong_apikey=cfgp.get("kong","apikey")

cloud1_IP=cfgp.get("cloud_1","IP")
cloud1_EndPoint=cfgp.get("cloud_1","EndPoint")
cloud1_user=cfgp.get("cloud_1","user")
cloud1_password=cfgp.get("cloud_1","password")

cloud2_IP=cfgp.get("cloud_2","IP")
cloud2_EndPoint=cfgp.get("cloud_2","EndPoint")
cloud2_user=cfgp.get("cloud_2","user")
cloud2_password=cfgp.get("cloud_2","password")

cloud3_IP=cfgp.get("cloud_3","IP")
cloud3_EndPoint=cfgp.get("cloud_3","EndPoint")
cloud3_user=cfgp.get("cloud_3","user")
cloud3_password=cfgp.get("cloud_3","password")

email_host=cfgp.get("email","host")
email_address=cfgp.get("email","address")
email_password=cfgp.get("email","password")


def main():
    
    if __name__ =='__main__':
        main()
