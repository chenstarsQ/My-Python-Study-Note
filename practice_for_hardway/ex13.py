# -*- coding: utf-8 -*-
from sys import argv

script,first,second,third = argv


a = input("first is :")
b = input("second is :")
c = input("third is :")

# print("The script is called:",script)
print("Your first variable %s is:%s"% (first,a))
print("Your second variable %s is:%s"%(second,b))
print("Your third variable %s is:%s"%(third,c))