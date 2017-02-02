# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Get a blanket.\n" # 定义一个函数 打印两个参数


print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)  # 调用函数
# 直接将数字当作参数代入函数


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50    
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 调用函数
# 将两个参数分别用变量表示 先给变量赋值 再把变量代入函数


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # 直接将数字当作参数代入函数 这里可以进行运算


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # 调用函数
# 也可以将变量与数字同时代入函数参数 并进行运算