# -*-coding:utf-8-*-
#
from selenium import webdriver

def browser(name):
    try:
        driver=eval("webdriver."+name.title()+"()")
        return driver
    #except FileNotFoundError:
       # print("系统中未找到对应的webdriver文件")
    except AttributeError:
        print("此浏览器不能被调用,请检查浏览器名称是否合法(firefox,chrome,ie)")
    except NameError:
        print("被调用的对象中没有此方法")

    except:
        print("打开浏览器失败")

if __name__=='__main__':
    dr = browser("ie")
    dr.get("http://www.baidu.com")
