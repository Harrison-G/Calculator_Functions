#Defines basic mathematical functions.

import math


#Command Line Interface

def commandLine(command):
    if len(command.split("="))==2:
        globals()[command.split("=")[0]]=command.split("=")[1]
        evalInput="Done."
    else:
        evalInput = eval(command)
             
    if evalInput==None:
        return "Done."
    else:
        return evalInput

while True:
    print(commandLine(input()))
