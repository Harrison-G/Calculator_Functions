#Defines basic mathematical functions.

import math
import cmath
import fractions

variables = {}

#Command Line Interface

def commandLine(command):
    if len(command.split('='))==2: #If defining a variable
        if len(command.split('/'))==1: #If variable value is a decimal
            if float(command.split('=')[1])%1==0:
                variables[command.split('=')[0]]={'mode':'decimal','decimal':float(command.split('=')[1]),'numerator':int(str(fractions.Fraction(str(command.split('=')[1]))).split('/')[0]),'denominator':1}
            else:
                variables[command.split('=')[0]]={'mode':'decimal','decimal':float(command.split('=')[1]),'numerator':int(str(fractions.Fraction(str(command.split('=')[1]))).split('/')[0]),'denominator':int(str(fractions.Fraction(str(command.split('=')[1]))).split('/')[1])}
            globals()[command.split('=')[0]]=variables[command.split('=')[0]]['decimal']
        else: #If variable value is a fraction
            variables[command.split('=')[0]]={'mode':'fraction','decimal':float(eval(command.split('=')[1])),'numerator':int(str(fractions.Fraction(command.split('=')[1])).split('/')[0]),'denominator':int(str(fractions.Fraction(command.split('=')[1])).split('/')[1])}
            globals()[command.split('=')[0]]=variables[command.split('=')[0]]['decimal'] #globals()[command.split('=')[0]]=str(variables[command.split('=')[0]]['numerator'])+'/'+str(variables[command.split('=')[0]]['denominator'])
        evalInput="Done."
    elif str(command) in variables and variables[command]['mode']=='fraction':
        evalInput=str(variables[command.split('=')[0]]['numerator'])+'/'+str(variables[command.split('=')[0]]['denominator'])
    else:
        evalInput = eval(command)
    
    if evalInput==None:
        return "Done."
    else:
        return evalInput

def mode(var,fractionOrDecimal):
    variables[var]['mode']=fractionOrDecimal

while True:
    print(commandLine(input()))
