import random

class Speler:
    def __init__(self,naam,wapen):
        self.naam = naam
        self.wapens = {wapen.lower()}
        self.aantal_vermoord = 0
        self.isDood = False
    
    def vermoord(self,andere_speler):
        assert not self.isDood, "Een dode speler kan niet vermoorden."
        assert not andere_speler.isDood, "Je kunt geen dode speler vermoorden."
        assert self != andere_speler, "Je kunt niet jezelf vermoorden."

        self.aantal_vermoord += 1
        self.isDood = True
        for wapen in andere_speler.wapens:
            if wapen not in self.wapens:
                self.wapens.add(wapen)

class Gevecht:
    def __init__(self,speler1,speler2):
        assert speler1 != speler2, "Spelers moeten verschillend zijn voor een gevecht."
        assert not speler1.isDood and not speler2.isDood, "Dode spelers kunnen niet vechten."
        self.speler1 = speler1
        self.speler2 = speler2
    def vecht(self):
        aanvaller, verdediger = random.choice([(self.speler1, self.speler2), (self.speler2, self.speler1)])

        print(f"{aanvaller.naam} valt aan! {verdediger.naam} verdedigt.")

        aanvaller.vermoord(verdediger)
        print(f"{verdediger.naam} is vermoord door {aanvaller.naam}.")


if __name__ == "__main__":
    speler1 = Speler("Anna", "zwaard")
    speler2 = Speler("Bert", "boog")

    gevecht = Gevecht(speler1, speler2)
    gevecht.vecht()
