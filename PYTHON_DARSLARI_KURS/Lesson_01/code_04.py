# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:09:39 2024

@author: hp
"""
a=[12,12.4,45,8,7.7]        #number
b=['Hello','nomer','Lower'] #string
c=[12,'yellow']             #different

#List Metod  append(),insert(),copy(),remove(),reverse(),sort()        operator del,len
a.append(2)       
del a[2]
c.insert(1,'Jamshidbek')
print(a,'\n',c)
d=a.copy()
d.remove(12)
print(d)
d.reverse()
print(d)
d.sort()
print(d)
print(len(d))