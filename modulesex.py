#!/usr/bin/python
# -*- coding: UTF-8 -*-

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    # global Money --sys auto take this var as a local var or a global var ...if you apparently write down global(key word),it will be correct.
    global Money
    Money = Money + 1


print Money
AddMoney()
print Money