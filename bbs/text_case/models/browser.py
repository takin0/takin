#定义浏览器的类，包括浏览器打开、最大化、刷新、前进、后退、新标签、关闭等
import sys
sys.path.append("..")#配置路径
from models.load_ini import mgmt_host,mgmt_port,path_ie,path_chrome,path_firefox,path_ide,path_qq
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.ie.options import Options
from selenium.webdriver import ActionChains
class Browser():
        def __init__(self,name,kernel):
                self.name=name
                self.kernel=kernel
#启动浏览器
        def open_browser(self):
                name=self.name
                kernel=self.kernel
                __browser_url =eval("path_"+name)
                options = Options()
                options.binary_location = __browser_url
                self.dr=eval("webdriver."+kernel.title()+"(options=options)")
#最大化
        def max(self):
                dr=self.dr
                dr.maximize_window()
#打开网址 参数url可选
        def open_url(self,urls=""):
                if urls:
                        url=urls
                else:
                        url=mgmt_host+":"+mgmt_port
                dr=self.dr
                dr.get(url)
#后退
        def back(self):
                dr=self.dr
                dr.back()
#前进
        def forward(self):
                dr=self.dr
                dr.forward()
#刷新
        def refresh(self):
                dr=self.dr
                dr.refresh()
#关闭网页
        def close(self):
                dr=self.dr
                dr.back()
#关闭浏览器
        def quit(self):
                dr=self.dr
                dr.quit()
#新的tab页
        def newtable(self,url):
                dr=self.dr
                JS='window.open("{}");'.format(url)#在字符串中引用变量
                dr.execute_script(JS)
  #滑动滚动条某一像素               
        def bottom(self,pxs):
                dr=self.dr
                JS=JS="window.scrollTo({},document.body.scrollHeigh)".format(pxs)
                dr.execute_script(JS)
  #滑动滚动条到某一位置
####        def bott(self):
###                dr=self.dr
#####                ac=dr.find_element_by_css_selector("#J_SaleBd > li.item.item-4 > a.image > img")
#####                ActionChains(driver).move_to_element(ac).perform()
                
        def getcook(self,keys=""):
                if keys:
                        key=keys
                else:
                        key=""
                dr=self.dr
                cook=dr.get_cookie("{}").format(key)
                print(cook)
        def addcook(self,zidian):
                dr=self.dr
                dr.add_cookie(zidian)#添加示例 {"name":"testname_1234567890","value":"testvalue_1234567890"}
        def delcook(self):
                dr=self.dr
                dr.delete_all_cookies()
chrome=Browser("chrome","Chrome")
ide=Browser("ide","Chrome")
firefox=Browser("firefox","Firefox")
ie=Browser("ie","Ie")
qq=Browser("qq","cHrome")
#'''
class Br():
        def __init__(self,name):
                self.name=name
        def open_browser(self):
                name=self.name
                self.dr=eval("webdriver."+name.title()+"()")
        def open_url(self,urls=""):
                if urls:
                        url=urls
                else:
                        url=mgmt_host+":"+mgmt_port

                dr=self.dr
                dr.get(url)
        def max(self):
                dr=self.dr
                dr.maximize_window()
        def back(self):
                dr=self.dr
                dr.back()
        def forward(self):
                dr=self.dr
                dr.forward()
        def refresh(self):
                dr=self.dr
                dr.refresh()
        def close(self):
                dr=self.dr
                dr.back()
        def quit(self):
                dr=self.dr
                dr.quit()
        def newtable(self,url):
                dr=self.dr
                JS='window.open("{}");'.format(url)#在字符串中引用变量
                dr.execute_script(JS)
'''
chrome2=Br("Chrome")
firefox2=Br("Firefox")
ie2=Br("Ie")

#'''
