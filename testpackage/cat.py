#!/usr/bin/python
# -*- coding:UTF-8 -*-
class Cat:
    'cat description'
    raiseyear = 0

    def __init__(self, color, sex):
        self.color = color
        self.sex = sex
        Cat.raiseyear += 1
        print self

    def miao(self):
        print "I am a cat , miao"

    def running(self):
        print "this is a common function"

    def displayRaiseYear(self):
        print "Total Year %d" % Cat.raiseyear

    def displayColor(self):
        print "Color : ", self.color, ", Sex: ", self.sex


print "Cat.__doc__:", Cat.__doc__
print "Cat.__name__:", Cat.__name__
print "Cat.__module__:", Cat.__module__
print "Cat.__bases__:", Cat.__bases__
print "Cat.__dict__:", Cat.__dict__