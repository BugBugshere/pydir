#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random


class Parent:
    # 定义父类
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        if self.publicCount:
            pass;
        else:
            self.publicCount += int(random.random() * 100)
        if self.__secretCount:
            self.__secretCount += 1
        else:
            self.__secretCount += self.publicCount + 1

        print self.__secretCount

    def myMethod(self):
        print '调用父类方法'

    def ppMethod(self):
        print self.__class__;
        if self.__class__ == Parent:
            print 'hello daddy'
        else:
            print 'silly boy ,i am your father'


class Child(Parent):  # 定义子类
    def myMethod(self):
        print '调用子类方法'


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
c.ppMethod()
c.count()
c.count()
print c.publicCount

d = Parent()
d.ppMethod()
d.count()
d.count()
