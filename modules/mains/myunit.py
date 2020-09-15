#coding=utf-8 

import unittest,os,sys,time

path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains import log
from modules.mains.browser import browser

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser

    @classmethod
    def tearDownClass(cls):
        browser.quit()
    
