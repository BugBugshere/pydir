#!/usr/bin/python
# -*- coding: UTF-8 -*-
##tuple
yuanzu = (1,2,3,4,5,'fuck you');
print yuanzu * 2


##dict
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales',3:'sss'}

 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict[3]		#output key value eq 3
print tinydict.values()    # 输出所有值


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

print tup1+tup2+tup3


dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: (37,55,63) };
print dict2[98.6]