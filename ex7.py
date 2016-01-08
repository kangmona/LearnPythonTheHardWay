# -*- coding:utf-8 -*-
print "Mary had a little lamb."
# 创建字符串时使用单引号和双引号都可以，不过一般单引号会被用来创建简短的字符串，如'a','snow'这样的。
print "And everywhere was white as %s." % 'snow'
print "." * 10 # 字符串*数字x，即代表该字符串重复x遍，所以此处为10个点点

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.
# 可以不用comma将这两行写成一行输出，但这样这行的长度超过80个字符，从python代码风格方面来讲是不好的。
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# remove that comma, -->换行，变成两段话。
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
