#截图函数
#-*-coding:utf-8-*-
from selenium import webdriver
import os
import driver as dri

import datetime

base_dir= os.path.dirname(os.path.dirname(os.path.abspath('.')))
file_path=base_dir+"\\report\\"

dirlist = os.listdir(file_path)
dirlist = sorted(dirlist, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
newdir=dirlist[-1]


def create_img (driver,file_name):
	base_dir= os.path.dirname(os.path.dirname(os.path.abspath('.')))
	file_path=base_dir+"\\report\\"+newdir+"\\image\\"+file_name+".png"
	driver.save_screenshot(file_path)
	print("图片保存在"+file_path)
	
if __name__=='__main__':
        dr = dri.browser("chrome")
        dr.get("http://www.qq.com")
        create_img(dr,'login')

