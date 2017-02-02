# -*- coding: utf-8 -*-
from sys import argv    # 导入参数变量

script, filename = argv # 解包参数变量（脚本＋文件）

txt = open(filename)                     # 先open文件，并赋值给txt。open函数。

print "Here's your file %r:" % filename
print txt.read()                         # 再read之前的txt。

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()