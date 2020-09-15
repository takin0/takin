# -*-coding:utf-8-*-
#from selenium import webdriver
import os
import sys
sys.path.append("..\..\..")#配置路径
from selenium import webdriver

from modules.mains import browser as br
brc=br.chrome

def get_url(jekinsurl):

    brc.open_browser()
    brc.open_url(jekinsurl)
    brc.olwt(10)
    brc.by_link('新闻')
    brc.click()

    brc.olwt(10)
    link=brc.by_xpath('//*[@id="channel-all"]/div/ul/li[8]/a')
    brc.olwt(10)
    updataurl=link.get_attribute('href')
    print(updataurl)

if __name__ == "__main__":
    get_url('https://www.baidu.com')
