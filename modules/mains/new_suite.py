import sys,os,time,unittest

base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
base_dir=base_dir.replace('\\', '/')
sys.path.append(base_dir)

from modules.mains import log
from modules.mains import sendemail,new_report

test_file="*test.py"
top_level_dir = None


def creat_suite(test_dir):
    suite=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=test_file,top_level_dir=top_level_dir)
    for test_suite in discover:
        for test_case in test_suite:
            #testunit.addTest(test_case)
            suite.addTest(test_case)
            print (suite)
    return suite

def run_suite(test_dir,description=u"自动化测试报告"):
    with open(new_report.creat_report(), 'w', encoding='utf-8') as file:
        runner=unittest.TextTestRunner(stream=file, descriptions=description, verbosity=2)   
        runner.run(creat_suite(test_dir))
    sendemail.send_mail()
    os._exit(0)

if __name__=='__main__':
        
    #creat_suite(test_dir)
    run_suit(test_dir)
