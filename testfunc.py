#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo(name, age=56, sex='man'):
    "打印任何传入的字符串"
    name += "-Davici"
    print "Name: ", name;
    print "Age: ", age;
    print "sex: ", sex;
    return;


# 调用printinfo函数
printinfo(age=50, sex="man", name="miki");
print
myname = "leeon"
printinfo(name=myname)
print myname


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
testarg = 5566
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)
print "相加后的值为 : ", sum(testarg, 20)