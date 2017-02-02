# -*- coding: utf-8 -*-
from sys import argv # argument参数 argv＝argument variable 参数变量

script, first, second, third = argv # 这一步unpack解包argv中的东西

print "The script is called:", script # 将四个参数分别命名并放到同一个变量下面
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# 运行时必须传递3个命令行参数
# agvr和raw_input()的区别在于用户输入参数的时机不同