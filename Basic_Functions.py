#Defines basic mathematical functions.

import time, numbers, math, cmath, decimal, fractions, random, statistics, itertools, functools, operator

variables = {}

#Command Line Interface

def commandLine(command):
    if len(command.split('='))==2: #If defining a variable
        defineVariable(command)
        evalInput="Done."
    else:
        evalInput = eval(command)
    
    if evalInput==None:
        return "Done."
    else:
        return evalInput

def defineVariable(expression):
    variables[expression.split('=')[0]]={'mode':'decimal','decimal':float(eval(expression.split('=')[1])),'fraction':fractions.Fraction(eval(expression.split('=')[1])).limit_denominator(10**8)}
    if '/' in expression.split('=')[1]:
        variables[expression.split('=')[0]]['mode']='fraction'
    globals()[expression.split('=')[0]]=variables[expression.split('=')[0]][variables[expression.split('=')[0]]['mode']]
    print(globals()[expression.split('=')[0]])

def mode(var,fractionOrDecimal):
    variables[var]['mode']=fractionOrDecimal
    globals()[var]=variables[var][variables[var]['mode']]
    return "Done."

while True:
    print(commandLine(input()))
