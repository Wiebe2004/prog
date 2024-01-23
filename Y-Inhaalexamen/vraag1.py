from math import sqrt, ceil

def maak_punt(x,y):
    print((x,y))

# maak_punt(45,56)

def afstand(p1,p2):
    # print((p1[0],p1[1]),(p2[0],p2[1]))
    print(float(sqrt((p1[1]-p1[0])**2 + (p2[1]-p2[0])**2)))

# afstand((45,22),(33,44))
    
def is_gelijk(p1,p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

# print(is_gelijk((22,33),(22,33)))

def maak_figuur(p1,p2):
    if is_gelijk(p1,p2):
        return False
    else:
        return [p1,p2]

# print(maak_figuur((22,33),(22,33)))
def voeg_punt_toe(figuur,p1):
    if figuur[-1] == p1:
        return False
    else:
        figuur.append(p1)
        return figuur

def lengtes(figuur):
    res = []
    for i in range(0,len(figuur) - 1):
        a = afstand(figuur[i],figuur[i+1])
        res.append(ceil(a))
    return res
