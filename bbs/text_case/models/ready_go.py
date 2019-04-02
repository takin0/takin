# -*-coding:utf-8 -*-
'''
import webbrowser
import selenium

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path_chrome))
webbrowser.get('chrome').open(url,new=1,autoraise=True)

import os
os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://www.baidu.com')
'''
'''
driver= webdriver.Chrome()
driver.maximize_window()
 
driver.implicitly_wait(3)
 

driver.get(url)
#driver.quit()
'''
from load_ini import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import makimg

url=mgmt_host+":"+mgmt_port

print(path_chrome)
print(url)
print(mgmt_user)
print(mgmt_password)

 
__browser_url = path_chrome
options = Options()
options.binary_location = __browser_url
driver = webdriver.Chrome(options=options)

driver.get(url)
driver.find_element_by_css_selector(".signin-username").send_keys(mgmt_user)
driver.find_element_by_css_selector(".signin-password").send_keys(mgmt_password + Keys.RETURN)
makimg.create_img(driver,'login.png')
