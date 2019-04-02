#截图函数
#-*-coding:utf-8-*-
from selenium import webdriver
import os,sys

def create_img (driver,file_name):
	base_dir= os.path.dirname(os.path.dirname(os.path.abspath('.')))
	file_path=base_dir+"\\report\\"+file_name
	driver.save_screenshot(file_path)
	print(file_path)
'''	
if __name__=='__main__':
	create_img(self,'login')'''