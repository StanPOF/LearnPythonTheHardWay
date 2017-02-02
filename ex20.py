# -*- coding: utf-8 -*-
from sys import argv # 导入参数变量

script, input_file = argv # unpack参数变量 脚本＋输入文件

def print_all(f):
    print f.read() # 定义print_all函数 打印整个参数f

def rewind(f):
    f.seek(0) # 定义rewind函数 作用为规定指针位置为文件的开头(移动0位)
    
def print_a_line(line_count, f):
    print line_count, f.readline() # 定义print_a_line函数 作用是打印line_count和从指针位置读取f一行内容的结果

current_file = open(input_file) # open输入文件 并赋值给current_file

print "Frist let's print the whole file:\n"

print_all(current_file) # 调用函数 参数为current_file

print "Now let's get rewind, kind of like a tape."

rewind(current_file) # 调用函数 将指针移到current_file的开头

print "Let's print three lines."

current_line = 1 # 令current_line为1
print_a_line(current_line, current_file) # 调用函数 打印1 current_file

current_line = current_line + 1 # 令current_line为current_line + 1 ＝ 2
print_a_line(current_line, current_file) # 调用函数 打印2 current_file

current_line = current_line + 1 # 令current_line为current_line + 1 ＝ 3
print_a_line(current_line, current_file) # 调用函数 打印3 current_file

# readline函数一次只读取一行内容,一个脚本中连续readline即可读取多行内容