#coding=utf-8 
import os,sys,time,logging

#配置路径model到环境
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains import log
from modules.mains.browser import browser
from modules.yancloud.login.element_login import username_css,password_css,login_xpath\
,rember_css,logout_css,quxiao_xpath,queding_xpath


brc=browser

testurl="https://10.10.11.3:9004"
testname="quanju"
testwd="P@ssw0rd"

def login(testname,testwd,remb=""):    
    brc.open_url(testurl)
    brc.olwt(10)
    brc.by_css(username_css)
    brc.clear()
    brc.input(testname)

    brc.by_css(password_css)
    brc.clear()
    brc.input(testwd)
    time.sleep(2)
    if remb=="T":     
            zz=brc.by_css(rember_css)
            brc.click()
    
    login=brc.by_xpath(login_xpath)
    brc.click()  
    
def logout(confirm=""):
    time.sleep(2)
    brc.by_css(logout_css)
    brc.click()
    time.sleep(2)
    if confirm:
        cfm=confirm
        quxiao=brc.by_xpath(quxiao_xpath)
        brc.click()
    else:
        queding=brc.by_xpath(queding_xpath)
        brc.click()
def xinxi():
    brc.olwt(10)
    time.sleep(2)
    brc.by_xpath('/html/body/div[2]/div/div/div[1]/div/span')
    a=brc.text()
    return a
    print(a)

       
if __name__ == "__main__":
    try:
        testname="superadmin"
        testwd="P@ssw0rd"
        login(testname,testwd,"T")

        logout()
    except:
        log.logger.exception('666')
