def index_kleinste(lijst,i):
    if  i < 0 or i >= len(lijst):
        return -1
    res = i
    for j in range(i+1,len(lijst)):
        if lijst[j] < lijst[res]:
            res = j
    return res

def verwissel(lijst,i):
    j = index_kleinste(lijst,i)
    if j != -1:
        hulp = lijst[i]
        lijst[i] = lijst[j]
        lijst[j] = hulp

def sorteer(lijst):
    for i in range(0,len(lijst)-1):
        verwissel(lijst,i)

lijst = [1,5,4,8,2,9,-5,11,-125]
sorteer(lijst)
print(lijst)
