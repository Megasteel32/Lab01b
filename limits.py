# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Finding Limits
# Date:        8/25/2020

import numpy
import matplotlib

from math import *

func1=1 # Creating variables to use repeatedly
func2=1
func3=1

print("This shows the function f(x) = sin(x)/x evaluated from x=1 to x=10^-7")
print(sin(func1)/func1) # prints the first iteration
func1=(func1/10)        # changes the value of the variable for the next iteration
print(sin(func1)/func1) # recursion
func1=(func1/10)        # recursion
print(sin(func1)/func1) # recursion
func1=(func1/10)        # recursion
print(sin(func1)/func1) # recursion
func1=(func1/10)        # recursion
print(sin(func1)/func1) # recursion
func1=(func1/10)        # recursion
print(sin(func1)/func1) # recursion
func1=(func1/10)        # recursion
print(sin(func1)/func1) # made you look
func1=(func1/10)        # recursion
print(sin(func1)/func1) # recursion

print("This shows the function g(x) = 1-cos(x)/x^2 evaluated from x=1 to x=10^-7")
print(((1-cos(func2))/(func2*func2))) # no recursion jokes this time
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2)))
func2=(func2/10)
print(((1-cos(func2))/(func2*func2))) # I know a good UDP joke, but you probably wouldn't get it

print("This shows the function h(x) = (1 + 1/x)^x evaluated from x=1 to x=10^7")
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)
func3=func3*10
print((1+(1/func3))**func3)









