# -*-coding:utf-8-*-
#from selenium import webdriver
import os
import sys
sys.path.append("..\..")#配置路径 

import logging
filepath =os.path.join(os.path.abspath('../../..'), 'logging.conf')
#logging.config.fileConfig(filepath)


from modules.mains import browser as br

#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
import time
#from selenium.webdriver.common.keys import Keys
from modules.mains import log
brc=br.chrome
testbrowser="chrome"
testurl="https://passport.jd.com/new/login.aspx"
testname="18531351953"
testwd="tj19940216jd"
username_css='#loginname'
password_css='#nloginpwd'
login_xpath='//*[@id="loginsubmit"]'
#br=eval("browser."+testbrowser)
sp1='https://item.jd.com/100011621642.html'
def login(testname,testwd):
    

    brc.open_browser()
    brc.open_url(testurl)
    brc.olwt(10)
    brc.by_css(username_css)
    brc.clear()
    brc.input(testname)

    brc.by_css(password_css)
    brc.clear()
    brc.input(testwd)
    time.sleep(2)   
 
    login=brc.by_xpath(login_xpath)
    brc.click()
    

def xinxi():
    wddd='//*[@id="shortcut"]/div/ul[2]/li[3]/div/a'
    brc.olwt(10)
    brc.by_xpath('//*[@id="shortcut"]/div/ul[2]/li[3]/div/a')
    a=brc.text()
    return a
    print(a)
    #except:
       # print('shibei')
        #time.sleep(2)
def buy():
    brc.open_url(sp1)
       
if __name__ == "__main__":
    try:     
        login(testname,testwd,)

        xinxi()
            
    except:
        log.logger.exception('404')
