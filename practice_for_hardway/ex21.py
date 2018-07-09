# -*- coding: utf-8 -*-

def add(a,b):
	print("Adding %d + %d" % (a,b))
	return a + b

def subtract(a,b):
	print("Subtract %d - %d" % (a,b))
	return a - b

def multiply(a,b):
	print("Multiply %d * %d" % (a,b))
	return a * b
	
def divide(a,b):
	print("Divide %d / %d" % (a,b))
	return a / b
	
print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(5,6)
IQ = divide(250,2)

print("Age:%d,height:%d,weight:%d,IQ:%d" % (age,height,weight,IQ))

print("Here is a puzzie")

what = add(age,subtract(height,multiply(weight,divide(IQ,2))))

print("That becomes: ",what,"Can you do it by hand?")