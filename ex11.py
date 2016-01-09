# -*- coding:utf-8 -*-
print "How old are you?",
# input()会根据用户输入变换相应的类型,而且如果要输入字符和字符串的时候必须要用引号包起来,
# 而raw_input()则是不管用户输入什么类型的都会转变成字符型。
# input()会把输入的东西当作python代码进行处理，这么做会有安全问题，应该尽量避开这个函数。
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)
