#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict3 = {'Sex':'male'}
dict.update(dict2)
print "Value : %s" %  dict
dict.update(dict3)
print "Value : %s" %  dict