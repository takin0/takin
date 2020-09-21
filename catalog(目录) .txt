一、conf/  #配置
	1.global.ini  #浏览器和邮箱配置：浏览器地址、对应驱动地址、对应内核名称
	2.logggin.conf  #日志配置：日志输出方式、日志格式

二、driver/  #浏览器驱动
	1.chromedriver.exe  #谷歌浏览器驱动
	2.geckodriver.exe  #火狐浏览器驱动
	3.IEDriverServer.exe  #IE浏览器驱动
	4.msedgedriver.exe  #edge浏览器驱动

三、日志/  #日志文件，由conf/logggin.conf文件配置
	1.service.log 
	2.today.log
	3.max1G.log
	
四、modules/  #主程序
	1 mains/  #主要文件
  		1.browser.py  #浏览器初始化及相关操作
  		2.load_ini.py  #加载conf/global.ini配置文件
  		3.log.py  #加载日志配置并实例化
  		4.myunit.py  #定义测试类
		5.sendemail.py  #打包最新测试报告并发送邮件
		6.report.py  #创建新的报告目录和查找最新的报告目录
		7.suite.py  #创建新的测试suite和run测试suite
 	2 yancloud/  #运行平台系统演示
  		1.login/  登陆模块演示	
			1.element_login.py  #页面元素演示
			2.login_procs.py  #操作流程演示
			3.login_test.py  #测试用例演示
  		2.update/  部署模块演示
			1.element_update.py  #页面元素演示
			2.update_procs.py  #操作流程演示
			3.update_test.py  #测试用例演示

 	3 jd/  #京东商城系统演示
  		1.登陆模块
			1.页面元素
			2.操作流程
			3.测试用例
  		2.部署模块
			1.页面元素
			2.操作流程
			3.测试用例
	。。。

	4.run_yancloud_test.py  #运行平台系统执行文件
	5.暂无			#京东商城系统执行文件

五、package/  #第三方依赖包，暂无

六、report/  #测试报告保存目录

七、run_test.py  #测试脚本执行入口文件

八、README.rst  #自述文件

