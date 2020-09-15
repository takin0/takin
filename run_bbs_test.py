#coding=utf-8
import sys,os,time,unittest

base_dir=os.path.dirname(os.path.realpath(__file__))
base_dir=base_dir.replace('\\', '/')
from modules.mains import log
from modules.mains.sendemail import send_mail


test_dir = base_dir+"/modules/yancloud"
test_file="*test.py"
description=u"自动化测试报告"
top_level_dir = None


def creatsuite():
    suite=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=test_file,top_level_dir=top_level_dir)
    for test_suite in discover:
        for test_case in test_suite:
            #testunit.addTest(test_case)
            suite.addTest(test_case)
            print (suite)
    return suite

def newreport():
        newdir="Test_"+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        file_path=base_dir+"/report/"+newdir+"/image/"
        fp=os.makedirs(file_path)
        report_path=base_dir+"/report/"+newdir+"/test.txt"
        return report_path
    
if __name__=='__main__':   
    with open(newreport(), 'w', encoding='utf-8') as file:
        runner=unittest.TextTestRunner(stream=file, descriptions=description, verbosity=2)   
        runner.run(creatsuite())
    send_mail()
    os._exit(0)
