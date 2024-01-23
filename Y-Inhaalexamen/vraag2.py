import random


class Mijn:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.geraakt = False

    def raak(self):
        self.geraakt = True

    def is_geraakt(self):
        if self.geraakt == True:
            return f"De mijn is geraakt!"
        else:
            return f"De mijn is niet geraakt!"


class Veld:
    def __init__(self, hoogte, mijnen):
        assert 3 <= hoogte <= 5, "De hoogte is min 3 en max 5"
        self.hoogte = hoogte
        for m in mijnen:
            assert mijnen.count(m) == 1, "element mag maar 1 keer voorkomen"
            assert m.x_coord in range(1, hoogte + 1) and m.y_coord in range(
                1, hoogte + 1
            ), "mijnen moeten in veld liggen"
        self.mijnen = mijnen

    def raak_mijn(self, x, y):
        for mijn in self.mijnen:
            if mijn.x_coord == x and mijn.y_coord == y:
                if not mijn.is_geraakt():
                    mijn.raak()
                    return True
        return False

    def __repr__(self):
        uit = ""
        for i in range(1, self.hoogte + 1):
            lijn = ""
            for j in range(1, self.hoogte + 1):
                lijn += "."
            for m in self.mijnen:
                if m.x_coord == i and m.is_geraakt():
                    lijn = lijn[: (m.y_coord - 1)] + "X" + lijn[m.y_coord :]
            uit += lijn + "\n"
        return uit
    
hoogte = int(input("Hoe groot moet het speelveld zijn (tussen 3 en 5)? "))
mijn_x = random.randint(1, hoogte)
mijn_y = random.randint(1, hoogte)
mijn = Mijn(mijn_x, mijn_y)
veld = Veld(hoogte, [mijn])

while True:
    print("0. Stop het spel.")
    print("1. Geef een coördinaat in.")

    keuze = input("Maak een keuze: ")

    if keuze == "0":
        print("Het spel wordt gestopt.")
        break
    elif keuze == "1":
        x = int(input("Geef de x-coördinaat in: "))
        y = int(input("Geef de y-coördinaat in: "))
        
        if veld.raak_mijn(x, y):
            print("Mijn geraakt!")
        else:
            print("Geen mijn geraakt.")
        
        print(veld)
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
