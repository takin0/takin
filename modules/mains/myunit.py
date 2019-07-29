#-*_coding:utf-8-*-
import unittest
from selenium import webdriver
from driver import browser

class MyTest(unittest.TestCase):
    def setUp(self):
        br=browser()
        br.implicitly_wait(10)
        br.maximize_window()

def tearDown(self):
    driver.quit()

if __name__=='__main__':
    unittest.main()
    
