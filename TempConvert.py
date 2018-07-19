# -*- coding: utf-8 -*-
tempStr =input("请输入带有符号的温度值：       ")
if tempStr[-1] in ['F','f']:
    c=(eval(tempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(c))
elif tempStr[-1] in ['C','c']:
    f=eval(tempStr[0:-1])*1.8+32
    print("转换后的温度是{:.2f}F".format(f))
else:
    print("输入数据错误")
    