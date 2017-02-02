# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists # 导入命令exists

script, from_file, to_file = argv  # 解包 脚本，来源文件，目标文件 是参数

print "Copying from %s to %s" % (from_file, to_file)

# 这两行能不能并到一行？怎么做？
in_file = open(from_file)     # 打开来源文件，并赋值给in_file
indata = in_file.read()       # 读取in_file，赋值给indata

print "The input file is %d bytes long" % len(indata) # len函数，会以数字的形式返回你传递的字符串的长度

print "Does the output file exist? %r" % exists(to_file) # exists参数为文件名,如果文件存在则返回True,不存在则返回False
print "Ready, hit RETURN to continue, CRTRL-C to abort."
raw_input(">")

out_file = open(to_file, 'w') # 以读写模式打开目标文件，并赋值给out_file
out_file.write(indata)        # 将indata变量的内容写入out_file

print "Alright, all done."

out_file.close()
in_file.close()