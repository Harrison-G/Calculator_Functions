#Defines basic mathematical functions.

import time, numbers, math, cmath, decimal, fractions, random, statistics, itertools, functools, operator

variables = {}

#Command Line Interface

def commandLine(command):
    if len(command.split(' = '))==2: #If defining a variable
        decimal=0
        command_split=(command.split(' = ')[1]).split()
        for i in range(len(command_split)):
            print(command_split[i])
            if command_split[i] in globals():
                print(command_split[i])
                if variables[command_split[i]]['mode']==decimal:
                    decimal=1
                command_split[i] = globals()[command_split[i]]
                print(command_split[i])
        print(command_split)
        command_define=command.split(' = ')[0] + ' = '
        for i in command_split:
            command_define += str(i)
        command = command_define
        defineVariable(command)
        evalInput="Done."
    else:
        for i in command.split():
            if i in globals():
                print(i)
                i = globals()[i]
                print(i)
        evalInput = eval(command)
    
    if evalInput==None:
        return "Done."
    else:
        return evalInput

def defineVariable(expression):
    if len(expression.split('/'))==1: #If variable value is a decimal
        myMode=''
        if len(expression.split('.'))==1 and (expression.split(' = ')[0] in variables.keys()):
            myMode='fraction'
        else:
            myMode='decimal'
        variables[expression.split(' = ')[0]]={'mode':myMode,'decimal':float(fractions.Fraction(eval(expression.split(' = ')[1]))),'fraction':fractions.Fraction(eval(expression.split(' = ')[1]))}
    else: #If variable value is a fraction
        z = eval(expression.split(' = ')[1])
        fraction = fractions.Fraction(z)#(expression.split(' = ')[1]))
        numerator = fraction.numerator
        denominator = fraction.denominator
        numerator = fraction.numerator
        denominator = fraction.denominator
        non_repeating=''
        repeating=''
        ########
        decimal_found = False
        v = numerator // denominator
        numerator = 10 * (numerator - v * denominator)
        answer = str(v)
        if numerator == 0:
            return answer
        answer += '.'
        states = {}
        while numerator > 0 :
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                #print(non_repeating + '[' + repeating + ']')
                break
            else:
                non_repeating = (numerator/denominator)/10
            states[numerator] = len(answer)
            v = numerator // denominator
            answer += str(v)
            numerator -= v * denominator
            numerator *= 10
        ########
        print(fraction)
##        last=fractions.Fraction(eval((expression.split(' = ')[1]).split('/')[0]))
##        for i in range(len((expression.split(' = ')[1]).split('/'))-1):
##            last=last/fractions.Fraction((str(expression.split(' = ')[1])).split('/')[i])
##        last=fractions.Fraction(last)
        last = fraction
        variables[expression.split(' = ')[0]]={'mode':'fraction','decimal':float(last),'fraction':last}
    globals()[expression.split(' = ')[0]]=variables[expression.split(' = ')[0]][variables[expression.split(' = ')[0]]['mode']]
    print(globals()[expression.split(' = ')[0]])

def mode(var,fractionOrDecimal):
    variables[var]['mode']=fractionOrDecimal
    globals()[var]=variables[var][variables[var]['mode']]
    return "Done."

while True:
    print(commandLine(input()))
