# -*- coding:utf-8 -*-
# 仅用raw_input写的脚本
filename = raw_input("Type your filename:")

print "Here's your file %r:" % filename
txt = open(filename)
print txt.read()
