#coding=utf-8 
#定义浏览器的类，包括浏览器打开、最大化、刷新、前进、后退、新标签、关闭等
import sys,os,datetime,time

path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)

from modules.mains import log

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from modules.mains.new_report import newreport
from modules.mains.load_ini import ReadConfig
               
class Browser():

        def __init__(self):
                brscf = ReadConfig()
                browser_path = brscf.get_brscf("browser_path")
                driver_path = brscf.get_brscf("driver_path")
                browser_kernel = brscf.get_brscf("browser_kernel")
                
                options = eval("webdriver."+browser_kernel.title()+"Options()")
                #options.add_argument("--headless")#不打开浏览器窗口
                options.add_argument('--ignore-certificate-errors')
                
                #options.add_argument("--user-data-dir="+os.getenv("USERPROFILE")+"/AppData/Local/Google/Chrome/User Data/Default");#chrome浏览器使用默认用户信息
                options.binary_location = browser_path
                self.dr=eval("webdriver."+browser_kernel.title()+"(executable_path=driver_path,options=options)")
                #self.dr=eval("webdriver."+browser_kernel.title()+"(driver_path)") #edge浏览器没有options参数
#2最大化
        def max(self,xnm='',ynm=''):
                if xnm and ynm:
                        dr=self.dr
                        dr.set_window_size(xnm,ynm)
                else:
                        try:
                            dr=self.dr
                            dr.maximize_window()
                        except:
                            info="最大化窗口失败"
                            print(info)
#0打开网址
        def open_url(self,urls):
                url = urls
                dr=self.dr
                try:
                    dr.get(url)
                except:
                    info="打开网址失败，请检查URL"
                    print(info)
#截图
        def create_img (self,img_name):
                dr=self.dr
                report_path=newreport()
                img_path=report_path[0]+"\\image\\"
                if os.path.isdir(img_path):
                        path_img=img_path+img_name+".png"
                        img=dr.save_screenshot(path_img)
                        print("图片保存在"+path_img)
                else:
                        print('图片保存路径{}不存在'.format(img_path))
#2后退
        def back(self):
                dr=self.dr
                dr.back()
#2前进
        def forward(self):
                dr=self.dr
                dr.forward()
#2刷新
        def refresh(self):
                dr=self.dr
                dr.refresh()
#2关闭网页
        def close(self):
                dr=self.dr
                dr.close()
#1关闭浏览器
        def quit(self):
                dr=self.dr
                dr.quit()
#2调用JS
        def jsc(self,js):
                dr=self.dr
                dr.execute_script(js)
#2新的tab页
        def newtable(self,url):
                dr=self.dr
                JS='window.open("{}");'.format(url)#在字符串中引用变量
                dr.execute_script(JS)
#2滑动滚动条某一像素
        def bottom(self,ypxs,xpxs=''):
                dr=self.dr
                if xpxs:
                        JS="window.scrollTo('{}','{}')".format(xpxs,ypxs)
                        dr.execute_script(JS)
                else:
                        JS="window.scrollTo(0,'{}')".format(ypxs)
                        dr.execute_script(JS)

#2获取cookies                
        def getcook(self,keys=""):
                if keys:
                        key=keys
                        dr=self.dr
                        cook=dr.get_cookie(key)
                        print(cook)
                else:
                        dr=self.dr
                        cook=dr.get_cookies()
                        print(cook)
                return cook
#2添加cookies
        def addcook(self,zidian):
                dr=self.dr
                dr.add_cookie(zidian)
                #示例 addcook({"name":"testname_1234567890","value":"testvalue_1234567890"})
#3删除cookies
        def delcook(self,name=''):
                dr=self.dr
                if name:
                        dr.delete_cookie(name)
                else:
                        dr.delete_all_cookies()
#1通过id定位
        def by_id(self,em_id):
                try:
                    dr=self.dr
                    self.em=dr.ind_element_by_id(em_id)
                except:
                    info="未找到id为{}的元素".format(em_id)
                    print(info)
#0通过xpath定位
        def by_xpath(self,em_xpath):
                try:
                    dr=self.dr
                    self.em=dr.find_element_by_xpath(em_xpath)
                except:
                    info="未找到xpath为{}的元素".format(em_xpath)
                    print(info)
#0通过css选择器定位
        def by_css(self,em_css):
                try:
                    dr=self.dr
                    self.em=dr.find_element_by_css_selector(em_css)
                except:
                    info="未找到css选择器为{}的元素".format(em_css)
                    print(info)
#1通过链接的关键字定位链接
        def by_link(self,em_text,Q=''):
                dr=self.dr
                if Q:
                        try:
                            Q='Q'    
                            
                            self.em=dr.find_element_by_link_text(em_text)
                        except:
                            info="未找到关键字为{}的元素".format(em_text)
                            print(info)  
                else:
                        try:
                            dr=self.dr
                            self.em=dr.find_element_by_partial_link_text(em_text)
                        except:
                            info="未找到关键字为{}的元素".format(em_text)
                            print(info)
#1将xpath和css选择器合并
        def by_all(self,em_all):
                try:
                        dr=self.dr
                        if '/' in em_all :
                                self.em=dr.find_element_by_xpath(em_all)
                        else:
                                self.em=dr.find_element_by_css_selector(em_all)

                except:
                       info="未找元素:{}".format(em_all)
                       print(info)
                #return em_all
#1清除内容
        def clear(self):
                try:
                        em=self.em
                        em.clear()
                except:
                        info="元素不能删除信息"
                        print(info)
#0输入数据
        def input(self,shuju=""):
                if shuju:
                        shuju=shuju
                else:
                        shuju=""
                em=self.em
                em.send_keys(shuju)
#0点击元素
        def click(self):
                em=self.em
                em.click()
#1获取属性
        def attri(self,attr):
                em=self.em
                info=em.get_attribute(attr)
                #print(info)
                return info
#1获取信息                
        def text(self):
                em=self.em
                info=em.get_attribute("textContent")
                #print(info)
                return info
        def sleep(self,n):
                time.sleep(n)
#0隐式等待               
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
#1鼠标单击
        def click_mouse(self,ems=''):
                dr=self.dr
                if ems:
                        en=ems  
                        if '/'in en:
                                eb=dr.find_element_by_xpath(en)
                                ActionChains(dr).click(eb).perform()         
                        else:
                                eb=dr.find_element_by_css_selector(en)
                                ActionChains(dr).click(eb).perform()      
                else:
                        ActionChains(dr).click().perform()
#1鼠标右键单击
        def rclick_mouse(self,ems=''):
                dr=self.dr
                if ems:
                        en=ems
                        
                        if '/'in en:
                                eb=dr.find_element_by_xpath(en)
                                ActionChains(dr).context_click(eb).perform()
                                
                        else:
                                eb=dr.find_element_by_css_selector(en)
                                ActionChains(dr).context_click(eb).perform()
                        
                else:
                        ActionChains(dr).context_click().perform()
#1鼠标移动到某元素
        def move_mouse(self,ems=''):
                dr=self.dr
                en=ems
                        
                if '/'in en:
                        eb=dr.find_element_by_xpath(en)
                        ActionChains(dr).move_to_element(eb).perform()
                                
                else:
                        eb=dr.find_element_by_css_selector(en)
                        ActionChains(dr).move_to_element(eb).perform()
#鼠标移动到某坐标(不太行)
        def move_zb(self,xzb,yzb):
                dr=self.dr
                ActionChains(dr).move_by_offset(xzb,yzb).perform()
#移动某元素的某坐标（错误）
        def move_(self,ems,xzb,yzb):
                dr=self.dr
                ActionChains(dr).move_to_element_with_offset(ems,xzb,yzb).perform()
#2鼠标双击(未验证)
        def dclick_elem(self,ems=''):
                dr=self.dr
                if ems:
                        en=ems
                        
                        if '/'in en:
                                eb=dr.find_element_by_xpath(en)
                                ActionChains(dr).double_click(eb).perform()
                                
                        else:
                                eb=dr.find_element_by_css_selector(en)
                                ActionChains(dr).double_click(eb).perform()
                        
                else:
                        ActionChains(dr).double_click().perform()
#拖动某一元素（未验证）
        def drag_drop(self,fr,to):
                dr=self.dr
                ActionChains(dr).drag_and_drop(fr,to).perform()

#单击不松开(未验证)
        def click_hold(self,ems=''):
                dr=self.dr
                if ems:
                        en=ems
                        
                        if '/'in en:
                                eb=dr.find_element_by_xpath(en)
                                ActionChains(dr).click_and_hold(eb).perform()
                                
                        else:
                                eb=dr.find_element_by_css_selector(en)
                                ActionChains(dr).click_and_hold(eb).perform()
                        
                else:
                        ActionChains(dr).click_and_hold().perform()
#释放左键（未验证）
        def release(self):
                dr=self.dr
                ActionChains(dr).release()
#键盘按键（未完成）
        def key_board(self,key1,elem='',key3=''):
                dr=self.dr
                ActionChains(dr).key_down(key1,elem).send_keys(key3).perform()


        def creat_chrome():
                
                creat_chrome=Browser("chrome","Chrome")
                return Browser
#chrome=Browser("chrome","Chrome")
browser=Browser()
'''                
ie=Browser("ie","Ie")
chrome=Browser("chrome","Chrome")
ide=Browser("ide","Chrome")
firefox=Browser("firefox","Firefox")
ie=Browser("ie","Ie")
other=Browser("other","Chrome")
'''
if __name__ == "__main__":
        #chrome=Browser("chrome","Chrome")
        browser.open_url("https://10.10.11.3:9004")

