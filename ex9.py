# -*- coding:utf-8 -*-
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"# \n为换行


print "Here are the days: ", days
print "Here are the months: " , months
# 使用%r时\n换行就不灵了，因为%r打印出的是你写出来的方式。它是用来调试的”原始“格式。
print "Here are the months: %r " % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""# 三引号之间不能有空格
