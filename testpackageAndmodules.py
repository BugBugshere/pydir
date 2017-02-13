#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 导入 testpackage 包
import testpackage

kitty = testpackage.Cat

hellokitty = kitty("white", "female")

print hellokitty.miao()

print kitty.__module__

testpackage.wang();

print kitty.__class__

print kitty.__doc__

print kitty.__dict__

testpackage.beast();
