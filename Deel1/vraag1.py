def verwissel(lijst, i):
    verwisseling_gebeurd = False

    # Controleer of i binnen de grenzen van de lijst ligt
    if 0 <= i < len(lijst) - 1:
        for j in range(i, len(lijst) - 1):
            x, y = lijst[j], lijst[j + 1]

            if x > y:
                # Verwissel x en y
                lijst[j], lijst[j + 1] = y, x
                verwisseling_gebeurd = True

    return lijst,verwisseling_gebeurd

def sorteer(lijst):
    for i in range(0,len(lijst)-1):
        if not verwissel(lijst,i):
            break

lijst = [1,2,8,7,4,3]
sorteer(lijst)
print(lijst)






# print(verwissel([1,2,8,7,4,3],3))