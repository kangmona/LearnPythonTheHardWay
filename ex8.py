# -*- coding:utf-8 -*-
formatter = "%r %r %r %r"
# 只有再想要获取某些东西的调试信息时才能用到%r
# %r给你的是变量的“程序员原始版本”

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)# True, False不能用引号，否则就是表示字符串
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )# %r是用来调试和排错的，所以有时打印出来的是单引号（尽管可能实际用的是双引号）



formatter2 = "%s %s %s %s"
# 带入后全部无外侧引号
print formatter2 % (1, 2, 3, 4)
print formatter2 % ("one", "two", "three", "four")
print formatter2 % (True, False, False, True)
print formatter2 % (formatter, formatter, formatter, formatter)
print formatter2 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
print formatter2 % ("小明", "小红", "小莉", "小刚")
