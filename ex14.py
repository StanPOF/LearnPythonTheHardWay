# -*- coding: utf-8 -*-
from sys import argv

script, user_name = argv
prompt = '>'   # prompt只是一个提示符 可以将prompt换成任意字符 并对其赋值这里'>'是给用户输入时看的

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) # raw_input中插入提示符 即显示提示符 如果想显示问号raw_input("?") 即可

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)