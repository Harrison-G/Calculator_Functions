#Defines basic mathematical functions.

import math


#Command Line Interface
def commandLine():
    evalInput = eval(input())
    if evalInput==None:
        return "Done."
    else:
        return evalInput
    

#Calculates exponents in the form of "a^b^c^..."
def power(string):
    myString = string.split('^')
    l=len(string.split('^'))
    if l==1:
        return string
    else:
        n=pow(float(myString[l-2]),float(myString[l-1]))
        for q in range(l-2):
            n=pow(float(myString[l-q-3]),n)
        return n

#Evaluates given arithmetic e.g.2+3,2-3,2*3,2/3,2**3
def evaluate():
    print(eval(input()))
