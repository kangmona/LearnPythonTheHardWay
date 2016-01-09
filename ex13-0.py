# -*- coding:utf-8 -*-
# 把这些我们导入(import)进来的功能称作modules(模组)。
# 需要把 sys modules(模组) import 进来
from sys import argv

# 将 argv “解包(unpack)”，与其将所有参数放到同一个变量下面，
# 我们将每个参数赋予一个变量名： script, first, second, 以及 third。
# 这也许看上去有些奇怪, 不过”解包”可能是最好的描述方式了。
# 它的含义很简单：“把 argv 中的东西解包，将所有的参数依次赋予左边的变量名”。
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# argv和raw_input()不同点：用户输入的时机。
# 如果参数是在用户执行命令时就要输入，那就是argv，见ex13-0.py
# 如果参数是在脚本运行过程中需要用户输入，那就用raw_input()，见本ex13-1.py
# 如果要结合argv和raw_input()，见ex13-2.py
