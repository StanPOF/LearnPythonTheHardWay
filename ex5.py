# -*- coding: utf-8 -*-
my_name = 'POF'
my_age = 20
my_height = 178 # 厘米
my_weight = 78 # 千克 一点也不重
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Acutally that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# %s %r %d是一种格式控制工具，告诉python把右边的变量带到左边的字符串中。