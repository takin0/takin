#coding=utf-8 

import unittest,os,sys,time

path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains import log
from modules.mains.browser import chrome

testurl="https://10.10.11.3:9004"

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome
        chrome.open_url(testurl)

    @classmethod
    def tearDownClass(cls):
        chrome.quit()
    
