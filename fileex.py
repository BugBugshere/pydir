#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import related module
import os

#os.rename("fool.txt","foo.txt")

# open a file
fo = open("foo.txt", "r+")
print "file name : ", fo.name

#print fo.write("www.abc.com.cn!")
str = fo.read()
print "what is read : ", str

# seek the position
position = fo.tell();
print "the position is : ", position

# take the point into the beginning
position = fo.seek(0, 0)  # the 2nd arg default value is 0
print "re-get file content : ", fo.read()

#os.rename("foo.txt","fool.txt")

print os.getcwd()
# close opened file
fo.close();


try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "close file"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"
#else:
#    print "内容写入文件成功"
