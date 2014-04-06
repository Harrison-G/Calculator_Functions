#Defines basic mathematical functions.

import math
import cmath
import fractions

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
    if len(expression.split('/'))==1: #If variable value is a decimal
        variables[expression.split('=')[0]]={'mode':'decimal','decimal':float(fractions.Fraction(expression.split('=')[1])),'fraction':fractions.Fraction(expression.split('=')[1])}
    else: #If variable value is a fraction
        variables[expression.split('=')[0]]={'mode':'fraction','decimal':float(fractions.Fraction(expression.split('=')[1])),'fraction':fractions.Fraction(expression.split('=')[1])}
    globals()[expression.split('=')[0]]=variables[expression.split('=')[0]][variables[expression.split('=')[0]]['mode']]

def mode(var,fractionOrDecimal):
    variables[var]['mode']=fractionOrDecimal
    globals()[var]=variables[var][variables[var]['mode']]
    return "Done."

while True:
    print(commandLine(input()))
