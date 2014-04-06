#Defines basic mathematical functions.

import math
import cmath
import fractions


#Command Line Interface

def commandLine(command):
    if len(command.split('='))==2: #If defining a variable
        if len(command.split('/'))==1: #If variable value is a decimal
            globals()[command.split('=')[0]]={'mode':'decimal','decimal':float(command.split('=')[1]),'numerator':int(str(fractions.Fraction(str(command.split('=')[1]))).split('/')[0]),'denominator':int(str(fractions.Fraction(str(command.split('=')[1]))).split('/')[1])}
        else: #If variable value is a fraction
            globals()[command.split('=')[0]]={'mode':'fraction','decimal':float(eval(command.split('=')[1])),'numerator':int(str(fractions.Fraction(command.split('=')[1])).split('/')[0]),'denominator':int(str(fractions.Fraction(command.split('=')[1])).split('/')[1])}
            print(globals()[command.split('=')[0]]['decimal'])
            print(globals()[command.split('=')[0]]['numerator'])
            print(globals()[command.split('=')[0]]['denominator'])
        evalInput="Done."
    elif str(command) in globals():
        if globals()[command]['mode']=='fraction':
            evalInput=str(globals()[command]['numerator'])+"/"+str(globals()[command]['denominator'])
        elif globals()[command]['mode']=='decimal':
            evalInput=globals()[command]['decimal']
    else:
        evalInput = eval(command)
             
    if evalInput==None:
        return "Done."
    else:
        return evalInput

def mode(var,fractionOrDecimal):
    globals()[var]['mode']=fractionOrDecimal

while True:
    print(commandLine(input()))
