#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 导入 testpackage 包
import testpackage

kitty = testpackage.Cat

hellokitty = kitty("white", "female")

print hellokitty.miao()

print kitty.__module__

testpackage.wang();
testpackage.beast();