# -*- coding: utf-8 -*-
age = raw_input("How old are you?") 
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you're %r years old, %r tall and %r heavy." % (age, height, weight)

# 与ex11的作用是一样的 但是更加简洁 直接使用raw_input() 省去一次赋值打印