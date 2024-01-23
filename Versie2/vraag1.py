def index_kleinste(lijst, i):
    # Controleer of de opgegeven index binnen het bereik van de lijst ligt
    if i < 0 or i >= len(lijst):
        return -1
    
    kleinste_index = i
    for j in range(i + 1, len(lijst)):
        if lijst[j] < lijst[kleinste_index]:
            kleinste_index = j
    
    return kleinste_index if kleinste_index != i else -1

        
def verwissel(lijst,i):
    if 0 <= i < len(lijst):
        indexK = index_kleinste(lijst, i)
    print(indexK)
    if 0 <= indexK < len(lijst):
        print(f"Oude lijst:{lijst}")
        lijst[i], lijst[indexK] = lijst[indexK],lijst[i]
    print(f"Nieuwe lijst {lijst}")
    # print(f"Gesorteerde lijst: {sorteer(lijst)}")

def sorteer(lijst):
    for i in range(len(lijst)):
        verwissel(lijst, i)



mijn_lijst = [4, 2, 7, 1, 9, 3]
print("Oorspronkelijke lijst:", mijn_lijst)

sorteer(mijn_lijst)
print("Gesorteerde lijst:", mijn_lijst)


    