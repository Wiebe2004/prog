from random import randint
class Speler:
    def __init__(self, naam, wapen) -> None:
        self.naam = naam
        self.wapens = set()
        self.wapens.add(wapen.lower())
        self.aantal_vermoord = 0
        self.isDood = False

    def vermoord(self,speler):
        assert not self.isDood, "dode speler kan niet moorden"
        assert not self.__eq__(speler), "speler moet andere speler doden"
        assert not speler.isDood, "andere speler moet levend zijn"
        self.aantal_vermoord += 1
        speler.isDood = True
        d = self.wapens.intersection(speler.wapens)
        self.wapens = self.wapens.union(speler.wapens)
        speler.wapens = d

    def __eq__(self, andere_speler) -> bool:
        if not isinstance(andere_speler,self.__class__):
            return False
        return self.naam == andere_speler.naam

    def __repr__(self) -> str:
        sLevend = ("levend" if not self.isDood else "dood")
        sWapens = ""
        if len(self.wapens) == 0:
            sWapens = "Heeft geen wapens"
        else:
            sWapens = str(self.wapens)
            sWapens = "Wapens: " + sWapens[1:len(sWapens) - 1]
        return self.naam + " is " + sLevend + "\naantal vermoord " + str(self.aantal_vermoord) + "\n" + sWapens

class Gevecht:
    def __init__(self, speler1, speler2) -> None:
        assert not speler1.isDood and not speler2.isDood, "speler in gevecht moet levend zijn"
        self.speler1 = speler1
        self.speler2 = speler2
    def vecht(self):
        i = randint(1,2)
        if i == 1:
            self.speler1.vermoord(self.speler2)
        else:
            self.speler2.vermoord(self.speler1)

an = Speler("an","Speer")
jan = Speler("jan","dolk")
gevecht = Gevecht(an,jan)
gevecht.vecht()
print(an)
print(jan)
jef = Speler("jef","dolk")
gevecht2 = Gevecht(an,jef)
gevecht2.vecht()
print(an)
print(jan)
print(jef)
