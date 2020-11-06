#coding=utf-8
import sys,os,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains import log

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from modules.mains import myunit as myut
from modules.mains.browser import browser
from modules.yancloud.login import login_procs as lg

class loginTest(myut.MyTest):
    def test_correct_login(self):
        lg.login("superadmin","P@ssw0rd")
        text=u"登录1成功"
        ts=lg.xinxi()
        '''
        if text==ts:
            pass
        else:
            browser.create_img(sys._getframe().f_code.co_name)
        '''
        self.assertEqual(ts, text)

    def test_usererr_login(self):
        lg.login("supera","P@ssw0rd")
        
        text=u"用户名或密码不正确！"
        ts=lg.xinxi()
        self.assertEqual(ts, text)

    def test_passerr_login(self):
        lg.login("superadmin","P#ssw0rd")
        
        text=u"用户名或密码不正确！"
        ts=lg.xinxi()
        self.assertEqual(ts, text)

if __name__=='__main__':
    unittest.main()
