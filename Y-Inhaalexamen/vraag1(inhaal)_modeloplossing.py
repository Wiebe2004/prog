from math import sqrt, ceil
def maak_punt(x,y):
    return (x,y)

def afstand(p1,p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def is_gelijk(p1,p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def maak_figuur(p1,p2):
    if is_gelijk(p1,p2):
        return False
    else:
        return [p1,p2]

def voeg_punt_toe(figuur,punt):
    if is_gelijk(punt,figuur[len(figuur)-1]):
        return False
    else:
        figuur.append(punt)
        return True

def lengtes(figuur):
    res = []
    for i in range(0,len(figuur) - 1):
        a = afstand(figuur[i],figuur[i+1])
        res.append(ceil(a))
    return res
