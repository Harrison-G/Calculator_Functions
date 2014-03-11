#Defines basic mathematical functions.

import math

def power(string):
    myString = string.split('^')
    l=len(string.split('^'))
    n=pow(float(myString[l-2]),float(myString[l-1]))
    for q in range(l-2):
        n=pow(float(myString[l-q-3]),n)
    return n
