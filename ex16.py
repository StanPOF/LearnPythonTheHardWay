# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)." # 退出键
print "If you do want that, hit RETURN."        # 回车进行下一步

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')    # 打开文件 模式为w 并赋值给target

print "Truncating the file.  Goodbye!"
target.truncate()             # truncate清空文件

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:") # 输入第一句话
line2 = raw_input("line2:") # 输入第二句话
line3 = raw_input("line3:") # 输入第三句话

print "I'm going to write these to the file."

target.write(line1) # 写入第一句话
target.write("\n")  # 写入换行
target.write(line2) # 写入第二句话
target.write("\n")  # 写入换行
target.write(line3) # 写入换行
target.write("\n")  # 写入第三句话

print "And finally, we close it."
target.close()