# -*- coding:utf-8 -*-
# 使用 argv 来获取文件名
from sys import argv

script, filename = argv

# open(),类似raw_input()会接受一个参数，并且返回一个值，可以将这个值赋予一个变量。
# 这就是打开文件的过程。
txt = open(filename)

print "Here's your file %r:" % filename
# 当你说txt.read 时，你的意思其实是：“嘿 txt！执行你的 read 命令，无需任何参数！”
print txt.read()


print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
