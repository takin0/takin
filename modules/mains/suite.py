import sys,os,time,unittest

base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
base_dir=base_dir.replace('\\', '/')
sys.path.append(base_dir)

from modules.mains import log
from modules.mains.report import TestReport
from modules.mains import sendemail

test_file = "*test.py"
top_level_dir = None

class Suite():
    def creat_suite(self,test_dir,test_file = test_file):
        suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(test_dir, pattern = test_file,top_level_dir = top_level_dir)
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTest(test_case)
            #print (suite)
        return suite

    def run_suite(self,test_dir,test_file = test_file,description = u"自动化测试报告"):
        sign = test_dir.split("/")[-1]
        report = TestReport()
        with open(report.creat_report(sign), 'w', encoding='utf-8') as file:
            runner = unittest.TextTestRunner(stream = file, descriptions = description, verbosity = 2)   
            runner.run(self.creat_suite(test_dir,test_file = test_file))
        sendemail.send_mail()
        os._exit(0)
        
if __name__ == '__main__':
    test_dir = base_dir + "/modules/yancloud"    
    #creat_suite(test_dir)
    suite = Suite()
    suite.run_suite(test_dir)
