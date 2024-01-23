def begint_met_klinker(woord):
    if len(woord) != 0:
        if woord[0] in {'a','A','e','E','i','I','o','O','u','U'}:
            return True
        else:
            return False
    return False

def begint_met_medeklinker(woord):
    if len(woord) != 0:
        medeklinkers = set(c for c in "bcdfghjklmnpqrstvwxyz")
        woord = woord.lower()
        if woord[0] in medeklinkers:
            return True
        else:
            return False
    return False

def eindigt_op_medeklinker(woord):
    if len(woord) != 0:
        medeklinkers = set(c for c in "bcdfghjklmnpqrstvwxyz")
        woord = woord.lower()
        if woord[len(woord) - 1] in medeklinkers:
            return True
        else:
            return False
    return False

def eindigt_op_klinker(woord):
    if len(woord) != 0:
        if woord[len(woord) - 1] in {'a','A','e','E','i','I','o','O','u','U'}:
            return True
        else:
            return False
    return False

def kortste_woord_begint_met_klinker(lijst):
    if len(lijst) != 0:
        lijst = list(w for w in lijst if begint_met_klinker(w))
        return min(lijst, key = lambda w : len(w))

def langste_woord_eindigt_op_klinker(lijst):
    if len(lijst) != 0:
        lijst = list(w for w in lijst if eindigt_op_klinker(w))
        return max(lijst, key = lambda w : len(w))

def kortste_woord_begint_met_medeklinker(lijst):
    if len(lijst) != 0:
        lijst = list(w for w in lijst if begint_met_medeklinker(w))
        return min(lijst, key = lambda w : len(w))

def langste_woord_eindigt_op_medeklinker(lijst):
    if len(lijst) != 0:
        lijst = list(w for w in lijst if eindigt_op_medeklinker(w))
        return max(lijst, key = lambda w : len(w))

f_invoer = open("woordenlijst_invoer.txt")
f_uitvoer = open("uitvoer.txt","w")
tekst = f_invoer.read()
tekst = tekst.replace("\n"," ")
lijst = tekst.split(" ")
woord1 = langste_woord_eindigt_op_klinker(lijst)
f_uitvoer.write("Het langste woord dat eindigt op een klinker is: " + woord1 + "\n")
woord2 = langste_woord_eindigt_op_medeklinker(lijst)
f_uitvoer.write("Het langste woord dat eindigt op een medeklinker is: " + woord2 + "\n")
woord3 = kortste_woord_begint_met_klinker(lijst)
f_uitvoer.write("Het kortste woord dat begint met een klinker is: " + woord3 + "\n")
woord4 = kortste_woord_begint_met_medeklinker(lijst)
f_uitvoer.write("Het kortste woord dat begint met een medeklinker is: " + woord4 + "\n")
aantal_klinkers = 0
for c in set(c for c in {'a','A','e','E','i','I','o','O','u','U'}):
    aantal_klinkers += tekst.count(c)
f_uitvoer.write("Het aantal gebruikte klinkers is: " + str(aantal_klinkers) + "\n")
aantal_medeklinkers = 0
tekst = tekst.lower()
for c in set(c for c in "bcdfghjklmnpqrstvwxyz"):
    aantal_medeklinkers += tekst.count(c)
f_uitvoer.write("Het aantal gebruikte medeklinkers is: " + str(aantal_medeklinkers) + "\n")
f_uitvoer.close()
f_invoer.close()