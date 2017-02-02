# -*- coding: utf-8 -*-
def print_two(*args):  # def就是定义函数,print_two函数名称,*args中的*告诉python把函数所有的变量收到名为args的列表中去,结尾要有冒号
    arg1, arg2 = args                         # 解包,变量为arg1,arg2 注意前面要有四格缩进,函数结束位置要取消缩进
    print "arg1: %r, arg2: %r" % (arg1, arg2) # 函数的作用就是打印变量
    
def print_two_again(arg1, arg2):              # 省去了解包过程
    print "arg1: %r, arg2: %r" % (arg1, arg2) # 作用同上
    
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."


print_two('Stan', 'POF')
print_two_again('Stan', 'POF')
print_one('Fuck!')
print_none()