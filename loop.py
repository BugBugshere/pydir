#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

i = 1
while i<10:
	i+=1
	if i%2 >0:
		continue
	else:
		print i

print "Good bye!"


count = 0
while count < 25:
	count = count + 1
   	if count > 15:
   		pass
	else :   
		print count, " is  less than 15"
else:
   print count, " is not less than 25"

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit
 
print "Good bye!"

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]
 
print "Good bye!"

#for...else
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num-1): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

random.seed(100)
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)


str = u"123456";  # Only digit in this string
print str.isnumeric();
