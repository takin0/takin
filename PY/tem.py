#温度转换
Tem=input("请输入带有符号的温度值：")
if Tem[-1] in ['F','f']:
    C = (eval(Tem[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif Tem[-1] in ['C','c']:
    F = eval(Tem[0:-1])*1.8+32
    print("转换后的温度{:.2f}F".format(F))
else:
    print("输入的格式错误")
