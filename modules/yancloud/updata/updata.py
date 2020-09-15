# -*-coding:utf-8-*-
#from selenium import webdriver
import os
import sys
sys.path.append("..\..")#配置路径
from selenium import webdriver
import paramiko

from modules.mains import browser as br
brc=br.chrome

def get_url(jekinsurl):

    brc.open_browser()
    brc.open_url(jekinsurl)
    brc.olwt(10)
    brc.by_link('xdata-apiruntime')
    brc.click()
 
    brc.olwt(10)
    brc.by_xpath('//*[@id="buildHistory"]/div[2]/table/tbody/tr[2]/td/div[1]/div/a/img')
    zt=brc.attri('alt')
    print(zt)
    '''
    brc.olwt(10)
    brc.by_xpath('//*[@id="tasks"]/div[5]/a[2]')
    brc.click()
    '''
    brc.sleep(60)
    brc.refresh()
    brc.olwt(10)
    brc.by_xpath('//*[@id="buildHistory"]/div[2]/table/tbody/tr[2]/td/div[1]/div/a/img')
    zt=brc.attri('alt')
    print(zt)
    s=0
    while 'In progress > Console Output' in zt:
        brc.sleep(5)
        brc.refresh()
        s+=1
        print('第%s次刷新'%s)
        
        brc.by_xpath('//*[@id="buildHistory"]/div[2]/table/tbody/tr[2]/td/div[1]/div/a/img')
        zt=brc.attri('alt')
        print(zt)
        if 'Aborted'in zt:
            brc.olwt(10)
            brc.by_xpath('//*[@id="tasks"]/div[5]/a[2]')
            brc.click()
        elif 'Success'in zt:
            break
                    
    if 'Success'in zt: 
        brc.olwt(10)
        brc.by_link('86_64.rpm')
        brc.olwt(10)
        installurl=brc.attri('href')
        print(installurl)

        brc.olwt(10)
        brc.by_link('xdata-apiruntime-3.1.zip','A')
        brc.olwt(10)
        global updataurl
        updataurl=brc.attri('href')
        print(updataurl)
        return installurl,updataurl
    
    else:
        print('程序其它出现错误')
        
def updata_linux():

    ip='10.10.11.4'
    username='root'
    password='yancloud'
    
    timeout=30
    try_times = 3
    if 0==0:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password)
        #b2=a1.open_session()
        #c1=b2.settimeout(timeout) %s'% updataurl)
        #c2=b2.get_pty()
        #c3=b2.invoke_shell()
        print(u'连接%s成功' % ip)

        stdin,stdout,stderr=ssh.exec_command('cd /opt/rh/')
        stdin,stdout,stderr=ssh.exec_command('mkdir /opt/test2/')

        pshell=ssh.invoke_shell()
        pshell.send('cd /opt/rh \n')
        mond='wget http://10.10.11.101:8080/job/xdata-apiruntime/lastSuccessfulBuild/artifact/yanphone-rpm/target/rpm/xdata-apiruntime/RPMS/x86_64/xdata-apiruntime-3.1-20190903286.x86_64.rpm'
        pshell.send(mond+'\n')
        pshell.recv(bufsize=-1)
        pshell.close
        #err = stderr.read()
        #print(err)
        #result = stdout.read()
        #print(result)
        

if __name__ == "__main__":
    #get_url('http://10.10.11.101:8080/')
    updata_linux()
