#Fibonaci sequence to that number or to the Nth number
# By using Binet's formula and golden ratio = 1.6180339887

# Xn = ((G.R)^n - (1 - G.R)^n) / 5 ^ (1/2)

from __future__ import division
import math


gr = 1.6180339887

def fibNum(n):
    a = pow(gr,n)
    b = pow((1-gr),n)
    c = math.sqrt(5)
    fib = (a-b)/c

    return math.ceil(fib)

print fibNum(55)
