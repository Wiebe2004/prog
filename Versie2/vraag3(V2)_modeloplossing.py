def maak_bestand():
    f_invoer = open("input.txt")
    f_uitvoer = open("resultaten.csv","w")
    lijn = f_invoer.readline()
    
    while lijn != "":
        info = str(lijn).split(sep = ";")
        naam = info[0]
        voornaam = info[1]
        totaal = 0
        while lijn!= "" and info[0] == naam and info[1] == voornaam:
            aantal = info[3]
            totaal += int(aantal)
            lijn = f_invoer.readline()
            info = str(lijn).split(sep = ";")
        
        uit = naam + ";" + voornaam + ";" + str(totaal) + "\n"
        f_uitvoer.write(uit)
    f_invoer.close()
    f_uitvoer.close()

def vraag2(uitgesloten_landen = set()):
    f_invoer = open("input.txt")
    res = set()
    lijn = f_invoer.readline()
    while lijn != "":
        info = lijn.split(";")
        land = info[2]
        if not land in res:
            res.add(land)
        lijn = f_invoer.readline()
    return res.difference(uitgesloten_landen)
print(vraag2({'Nederland','Portugal'}))