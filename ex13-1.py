# -*- coding:utf-8 -*-
# argv和raw_input()不同点：用户输入的时机。
# 如果参数是在用户执行命令时就要输入，那就是argv，见ex13.py
# 如果参数是在脚本运行过程中需要用户输入，那就用raw_input()，见本ex13-1.py
# 如果要结合argv和raw_input()，见ex13-2.py
script = raw_input("The script is called:")
first = raw_input("Your first variable is:")
second = raw_input("Your second variable is:")
third = raw_input("Your third variable is:")
