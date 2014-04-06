#Defines basic mathematical functions.

import math
import cmath
import fractions

variables = {}

#Command Line Interface

def commandLine(command):
    if len(command.split('='))==2: #If defining a variable
        if len(command.split('/'))==1: #If variable value is a decimal
            variables[command.split('=')[0]]={'mode':'decimal','decimal':float(fractions.Fraction(command.split('=')[1])),'fraction':fractions.Fraction(command.split('=')[1])}
        else: #If variable value is a fraction
            variables[command.split('=')[0]]={'mode':'fraction','decimal':float(fractions.Fraction(command.split('=')[1])),'fraction':fractions.Fraction(command.split('=')[1])}
        globals()[command.split('=')[0]]=variables[command.split('=')[0]][variables[command.split('=')[0]]['mode']]
        evalInput="Done."
    else:
        evalInput = eval(command)
    
    if evalInput==None:
        return "Done."
    else:
        return evalInput

def mode(var,fractionOrDecimal):
    variables[var]['mode']=fractionOrDecimal
    globals()[var]=variables[var][variables[var]['mode']]
    return "Done."

while True:
    print(commandLine(input()))
