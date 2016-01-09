# -*- coding:utf-8 -*-
# argv和raw_input()不同点：用户输入的时机。
# 如果参数是在用户执行命令时就要输入，那就是argv，见ex13-0.py
# 如果参数是在脚本运行过程中需要用户输入，那就用raw_input()，见本ex13-1.py
# 如果要结合argv和raw_input()，见ex13-2.py
from sys import argv

script, first, second, third = argv

print "The script is called:", script
raw_input("Your name:")
raw_input("Your age:")
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
raw_input("Your fourth variable is:")
raw_input("Your fifth variable is:")
