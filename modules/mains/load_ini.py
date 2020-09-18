#coding=utf-8 
#读取加载配置文件global.ini
#读取配置文件的路径
import os,sys
path_base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base = path_base.replace('\\', '/')
sys.path.append(path_base)

path_load_ini = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+"/conf/"
path_load_ini = path_load_ini.replace('\\', '/')

from modules.mains import log
import configparser

class ReadConfig:

    def __init__(self,filepath = path_load_ini + "global.ini"):
    
        self.cfgp = configparser.ConfigParser()
        self.cfgp.read(filepath)

    def get_sections(self):
        section = self.cfgp.sections()
        return section

    def get_options(self,section):
        options = self.cfgp.options(section)
        return options
        
    def get_brscf(self,param):
        value = self.cfgp.get("browser",param)
        return value

    def get_emcf(self,param):
        value = self.cfgp.get("email",param)
        return value
        
if __name__ == '__main__':
    #test = ReadConfig()
    #t = test.get_brscf("browser_path")
    print("t")

