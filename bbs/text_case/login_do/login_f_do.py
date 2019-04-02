import sys
import time
sys.path.append("..")
import models.browser
#import models.load_ini
models.browser.chrome.open_browser()
#models.browser.chrome2.max()

models.browser.chrome.open_url("https://www.baidu.com")
#models.browser.ie.addcook({"name":"testname_1234567890","value":"testvalue_1234567890"})
#models.browser.ie.getcook()



models.browser.chrome.newtable("https://www.taobao.com")
time.sleep(3)
models.browser.chrome.bottom("10000")

'''
models.browser.ie2.back()
models.browser.ie2.forward()
models.browser.ie2.refresh()
models.browser.ie2.close()
models.browser.ie2.quit()
models.browser.chrome.newtable("https://www.baidu.com")
'''
