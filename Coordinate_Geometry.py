import math

def slope(x1,y1,x2,y2):
    return (str((y2-y1)/(x2-x1)))

def distance(x1,y1,x2,y2):
    if math.floor(math.sqrt(pow((x2-x1),2)+(pow((y2-y1),2))))==(math.sqrt(pow((x2-x1),2)+(pow((y2-y1),2)))):
        return (str(int(math.sqrt(pow((x2-x1),2)+(pow((y2-y1),2))))))
    else:
        outside_root = 1
        inside_root = (pow((x2-x1),2)+(pow((y2-y1),2)))
        d = 2
        while (d * d <= inside_root):
            if (inside_root % (d * d) == 0): # inside_root evenly divisible by d * d
                inside_root = inside_root / (d * d)
                outside_root = outside_root * d
            else:
                d = d + 1
    inside_root=int(inside_root)
    if outside_root==1:
        return("√"+ str(inside_root))
    else:
        return(str(outside_root) + "√"+ str(inside_root))

def midpoint(x1,y1,x2,y2):
    return (str((x1+x2)/2) + ", " + str((y1+y2)/2))
