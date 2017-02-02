# -*- coding: utf-8 -*-
print "How old are you?", # print后面的,是为了避免换行。
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So you're %s old, %r tall and %r heavy." % (age, height, weight)