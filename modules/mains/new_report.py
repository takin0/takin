#coding=utf-8
#截图函数
import os,datetime
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
from modules.mains import log
#print(path_base)

def newreport():
        dir_path=path_base+"/report/"#测试报告路径
        dirlist = os.listdir(dir_path)
        mdirlist = sorted(dirlist, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))
        mnewdir=mdirlist[-1]
        adirlist = sorted(dirlist, key=lambda x: os.path.getatime(os.path.join(dir_path, x)))
        anewdir=adirlist[-1]
        cdirlist = sorted(dirlist, key=lambda x: os.path.getctime(os.path.join(dir_path, x)))
        cnewdir=cdirlist[-1]
        if mnewdir==cnewdir==anewdir:
                newdir=mnewdir#最新报告文件夹
        else:
                print('文件时间不统一')
                newdir=mnewdir              
        file_path=dir_path+newdir#最新报告文件夹路径
        return file_path,newdir

if __name__=='__main__':
        newreport()

