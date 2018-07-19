# -*- coding: utf-8 -*-
#摄氏度与华氏度的转换
''' tempStr =input("请输入带有符号的温度值：       ")
if tempStr[-1] in ['F','f']: #索引和切片
    c=(eval(tempStr[0:-1])-32)/1.8#eval 将字符串最外侧的引号去掉
    print("转换后的温度是{:.2f}C".format(c))#大括号表示槽，把format中的c变量填充到这个槽内
elif tempStr[-1] in ['C','c']:#冒号是语法的一部分，不能省略
    f=eval(tempStr[0:-1])*1.8+32
    print("转换后的温度是{:.2f}F".format(f))
else:
    print("输入数据错误") '''


# 包含了 整数 浮点 字符串 列表（数组） 四种数据




tempStr =input("请输入带有符号的温度值：       ")
if tempStr[0] in ['F','f']: #索引和切片
    c=(eval(tempStr[1:])-32)/1.8#eval 将字符串最外侧的引号去掉
    print("转换后的摄氏温度是{:.2f}C".format(c))#大括号表示槽，把format中的c变量填充到这个槽内
elif tempStr[0] in ['C','c']:#冒号是语法的一部分，不能省略
    f=eval(tempStr[1:])*1.8+32
    print("转换后的华氏温度是{:.2f}F".format(f))
else:
    print("输入数据错误")