#coding=utf-8
import sys,os

base_dir=os.path.dirname(os.path.realpath(__file__))
base_dir=base_dir.replace('\\', '/')

from modules.mains import log
from modules import run_yancloud_test

if __name__=='__main__':
    try:
        run_yancloud_test.test_yancloud()
    except:
        log.logger.exception('abcdef')

