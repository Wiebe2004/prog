def verwissel(lijst,i):
    ok = False
    for j in range (i, len(lijst)-1):        
        if lijst[j] > lijst[j+1]:
            hulp = lijst[j]
            lijst[j] = lijst[j+1]
            lijst[j+1] = hulp
            ok = True
    return ok

def sorteer(lijst):
    for i in range (0,len(lijst) - 1):
        if not verwissel(lijst,i):
            break
lijst = [1,2,8,7,4,3]
sorteer(lijst)
print(lijst)

