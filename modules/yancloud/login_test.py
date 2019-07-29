import unittest,sys
from selenium import webdriver
import sys
sys.path.append("..\..")#配置路径
from modules.mains import browser as bro
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import login_procs as lg
class loginTest(unittest.TestCase):
    def test_correct_login(self):
        lg.login("superadmin","P@ssw0rd")
        
        lo='/html/body/div/div[1]/div[3]/div[3]/div/div/p'
        text=u"失败"
        #lg.br.duanyan("By.XPATH",lo,text)
        ts=self.driver.find_element_by_xpath(lo).text
        self.assertEqual(ts, text)
if __name__=='__main__':
    unittest.main()

    
    suit=unittest.TestSuite()
    suit.addTest(Test(test_correct_login))
    runner=unittest.TextTestRunner()
    runner.run(suit)
