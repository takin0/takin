#定义浏览器的类，包括浏览器打开、最大化、刷新、前进、后退、新标签、关闭等
import sys
sys.path.append("..\..")#配置路径
from modules.mains.load_ini import mgmt_host,mgmt_port,path_ie,path_chrome,path_firefox,path_ide,path_qq
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.ie.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Browser():
        def __init__(self,name,kernel):
                self.name=name
                self.kernel=kernel
#启动浏览器
        def open_browser(self):
                global dr
                
                name=self.name
                kernel=self.kernel
                __browser_url =eval("path_"+name)
                options = Options()
                options.binary_location = __browser_url
                try:
                    #global dr
                    self.dr=eval("webdriver."+kernel.title()+"(options=options)")
                    #return dr （会报错）
                except:
                    tishi= "加载{}浏览器失败".format(kernel)
                    print(tishi)                   
        def open_br(self):
                name=self.name
                self.dr=eval("webdriver."+name.title()+"()")
#最大化
        def max(self):
                try:
                    dr=self.dr
                    dr.maximize_window()
                except:
                    tishi="最大化窗口失败"
                    print(tishi)
#打开网址 参数url可选
        def open_url(self,urls=""):
                try:
                    if urls:
                            url=urls
                    else:
                            url=mgmt_host+":"+mgmt_port
                    dr=self.dr
                    dr.get(url)
                except:
                    tishi="打开网址失败，请检查URL"
                    print(tishi)
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
#调用JS
        def jsc(self,js):
                dr=self.dr
                dr.execute_script(js)
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

# 获取cookies                
        def getcook(self,keys=""):
                if keys:
                        key=keys
                else:
                        key=""
                dr=self.dr
                cook=dr.get_cookie("{}").format(key)
                print(cook)
#添加cookies
        def addcook(self,zidian):
                dr=self.dr
                dr.add_cookie(zidian)#添加示例 {"name":"testname_1234567890","value":"testvalue_1234567890"}
#删除cookies
        def delcook(self):
                dr=self.dr
                dr.delete_all_cookies()
#通过id定位
        def by_id(self,em_id):
                try:
                    dr=self.dr
                    self.em=dr.ind_element_by_id(em_id)
                except:
                    tishi="未找到id为{}的元素".format(em_id)
                    print(tishi)
#通过xpath定位
        def by_xpath(self,em_xpath):
                try:
                    dr=self.dr
                    self.em=dr.find_element_by_xpath(em_xpath)
                except:
                    tishi="未找到xpath为{}的元素".format(em_xpath)
                    print(tishi)
#通过css选择器定位
        def by_css(self,em_css):
                try:
                    dr=self.dr
                    self.em=dr.find_element_by_css_selector(em_css)
                except:
                    tishi="未找到css选择器为{}的元素".format(em_css)
                    print(tishi)
#通过链接的关键字定位链接
        def by_link(self,em_text):
                try:
                    dr=self.dr
                    self.em=dr.find_element_by_partial_link_text(em_text)
                except:
                    tishi="未找到关键字为{}的元素".format(em_text)
                    print(tishi)
#清除内容
        def clear(self):
                em=self.em
                em.clear()
#输入数据
        def input(self,shuju=""):
                if shuju:
                        shuju=shuju
                else:
                        shuju=""
                em=self.em
                em.send_keys(shuju)
#点击元素
        def click(self):
                em=self.em
                em.click()
        def text(self):
                em=self.em
                info=em.get_attribute("textContent")
                print(info)
        def olwt(self,_second=""):
                if _second:
                        _second=_second
                else:
                        _second=7
                dr=self.dr
                dr.implicitly_wait(_second)
                


        def duanyan(self,ff,cs,dy):
                dr=self.dr
                ca=(eval(ff),cs)
                
                assert WebDriverWait(dr,10,0.5).until(EC.text_to_be_present_in_element(ca,dy)(dr))
                
				
chrome=Browser("chrome","Chrome")
ide=Browser("ide","Chrome")
firefox=Browser("firefox","Firefox")
ie=Browser("ie","Ie")
qq=Browser("qq","cHrome")
from modules.yancloud.login.element_login import username_css
if __name__ == "__main__":
        chrome.open_browser()
        chrome.open_url("https://10.10.11.2:9002")
        chrome.by_css(username_css)
        chrome.olwt()
        chrome.text()
        


