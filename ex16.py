# -*- coding:utf-8 -*-
# 做一个简单的文本编辑器
# .open()——打开文件
# .close()——关闭文件
# .truncate()——清空文件。小心使用
# .write(stuff)——将stuff写入文件
# .read()——读取全部内容
# .readline()——逐行读取
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# 用读写模式打开filename这个文件，并赋值给target
# open(filename, 'r')——读取模式打开
# open(filename, 'w')——读写模式打开
# open(filename, 'a')——写入模式打开
# open(filename, 'b')——二进制模式打开文件(可以和其他模式并用)
# open(filename, '+')——读/写模式(可以和其他模式并用)
# open(filename, 'U')——支持换行符(例如：\n、\r 或 \n\r 等)
# a=open('text.txt','w');-->使用open()函数来打开text.txt文件，以读写模式打开，这样就可以对文件进行读写操作了。
# a.write("大家好，欢迎光临我的网站！")-->打开文后返回一个文件对象，然后调用write()函数写入信息
# a.close();-->最后调用close()关闭文件
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("\n")

# 节省代码写法：
target.write(line1+"\n"+line2+"\n"+line3+"\n")
print "And finally, we close it."
target.close()

# 写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件:
print " Type the filename again:"
file_again = raw_input(">")
target_again = open(filename,'r')
print target_again.read()
