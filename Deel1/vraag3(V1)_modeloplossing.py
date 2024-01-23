f_invoer = open("input.txt")
f_uitvoer = open("resultaten.csv","w")
lijn = f_invoer.readline()
while lijn != "":
    s = lijn.split(",")
    naam = s[0]
    voornaam = s[1]
    tijd = int(s[4])
    lijn = f_invoer.readline()
    s = lijn.split(",")
    while s[0] == naam and s[1] == voornaam and lijn != "":
        tijd += int(s[4])
        lijn = f_invoer.readline()
        s = lijn.split(",")
    nieuwe_lijn = naam + ";" + voornaam + ";" + str(tijd) +"\n"
    f_uitvoer.write(nieuwe_lijn)
f_invoer.close()
f_uitvoer.close()