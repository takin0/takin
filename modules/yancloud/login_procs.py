# -*-coding:utf-8-*-

from selenium import webdriver
#import os
import sys
sys.path.append("..\..")#配置路径
from modules.mains import browser as br
from modules.yancloud.login.element_login import username_css,password_css,login_xpath
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys

testbrowser="chrome"
testurl="https://10.10.11.5:9004"
testname="quanju"
testwd="P@ssw0rd"
#br=eval("browser."+testbrowser)

def login(testname,testwd,remb=""):
    

    br.chrome.open_browser()
    br.chrome.open_url(testurl)

    #br.max()

    br.chrome.olwt(10)
    br.chrome.by_css(username_css)
    br.chrome.clear()
    br.chrome.input(testname)

    br.chrome.by_css(password_css)
    br.chrome.clear()
    br.chrome.input(testwd)
    time.sleep(2)
    if remb=="T":     
            zz=br.chrome.by_css(".ivu-checkbox-input")
            br.chrome.click()
    
    login=br.chrome.by_xpath(login_xpath)
    br.chrome.click()  
    
def logout(confirm=""):
   # br=eval("browser."+testbrowser)
    time.sleep(2)
    #geren=br.by_xpath("/html/body/div/div[1]/header/div/nav/div/ul[2]/li/a/span")
    br.click()
    time.sleep(2)
    dengchu=br.by_xpath("/html/body/div/div[1]/header/div/nav/div/ul[2]/li/ul/li[3]/a")
    br.click()
    time.sleep(2)
    if confirm:
        cfm=confirm
        quxiao=br.by_xpath("//*[@id=\"gxjh-modal-btn-default\"]")
        br.click()
    else:
        queding=br.by_xpath("//*[@id=\"gxjh-modal-btn-primary\"]")
        br.click()
def xinxi():
    #try:
    br.chrome.olwt(10)
    br.chrome.by_xpath("/html/body/div[2]/span")
    a=br.chrome.text()
    print(a)
    #except:
       # print('shibei')
        #time.sleep(2)
       
if __name__ == "__main__":
    testname="superadmin"
    testwd="P@ssw0rd"
    login(testname,testwd,"T")

    xinxi()
