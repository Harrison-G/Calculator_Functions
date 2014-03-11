#Formulas_and_Identities_from_Trigonometry

trigMode = 1

def setTrigMode(mode):
    if mode=="degrees":
        trigMode=math.pi/180
    elif mode=="radians":
        trigMode=1
    else:
        error

def sin(num):
    return math.sin(num*trigMode)
    
def cos(num):
    return math.cos(num*trigMode)
    
def tan(num):
    return math.tan(num*trigMode)
