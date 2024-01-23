# # Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.


# def csom(n):
#     while n >= 10:
#         result = 0
#         for digit in str(n):
#             result += int(digit)
#         n = result
#     return n


# # 2 Werkende manieren


# def csom(n):
#     while n >= 10:
#         n = sum(int(digit) for digit in str(n))
#     return n


# # Voorbeeldgebruik:
# resultaat = csom(377096267)
# # print(f"c-som(377096267) = {resultaat}")


# def isPalindroom(t):
#     if t == t[::-1]:
#         print(f"voorwaarts: {t}")
#         print(f"Achterwaards: {t[::-1]}")
#         return True
#     else:
#         print(f"voorwaarts: {t}")
#         print(f"Achterwaards: {t[::-1]}")
#         return False


# # print(isPalindroom((1,)))


# class Attractie:
#     def __init__(self, naam, grootte):
#         self.__naam = None
#         self.__grootte = None
#         self.naam = naam
#         self.grootte = grootte
#         self.bezoekers = 0

#     @property
#     def naam(self):
#         return self.__naam

#     @naam.setter
#     def naam(self, naam):
#         if naam == "":
#             raise ValueError("Naam mag niet leeg zijn")
#         self.__naam = naam

#     @property
#     def grootte(self):
#         return self.__grootte

#     @grootte.setter
#     def grootte(self, grootte):
#         if grootte < 0:
#             raise ValueError("Grootte mag niet negatief zijn")
#         self.__grootte = grootte

#     def bezoek(self, bezoeker_grootte):
#         if bezoeker_grootte >= self.grootte:
#             self.bezoekers += 1
#             return self.bezoekers
#         else:
#             error_message = f"Bezoeker te klein voor attractie '{self.naam}'"
#             with open("log.txt", "a") as log_file:
#                 log_file.write(error_message + "\n")
#             print(error_message)


# Pagode = Attractie("De Pagode", 0)
# MaEnMo = Attractie("Max & Moritz", 100)
# Baron = Attractie("De Baron", 132)

# # print(MaEnMo.bezoek(110),MaEnMo.bezoek(120))


# class Pretpark:
#     def __init__(self, naam):
#         self.__naam = None
#         self.__attracties = []

#         self.naam = naam

#     @property
#     def naam(self):
#         return self.__naam

#     @naam.setter
#     def naam(self, naam):
#         if naam == "":
#             raise ValueError("Naam mag niet leeg zijn")
#         else:
#             self.__naam = naam

#     def voegAttractieToe(self, attractie):
#         for a in self.__attracties:
#             if a.naam.lower().replace(" ", "") == attractie.naam.lower().replace(" ", ""):
#                 raise ValueError("Deze attractie bestaat al.")
#         self.__attracties.append(attractie)
#         return self.__attracties

#     def printOverzicht(self):
#         attractie_aantal = len(self.__attracties)
#         bezoekers_totaal = sum(attractie.bezoekers for attractie in self.__attracties)
#         return f"{self.naam} is een pretpark met {attractie_aantal} attractie(s) die in totaal {bezoekers_totaal} keer werden bezocht."

# efteling = Pretpark("De Efteling")
# efteling.printOverzicht()

# # Voeg De Pagode toe
# pagode = Attractie("De Pagode", 0)
# efteling.voegAttractieToe(pagode)
# efteling.printOverzicht()

# # Voeg Max & Moritz en De Baron toe
# max_en_moritz = Attractie("Max & Moritz", 100)
# de_baron = Attractie("De Baron", 132)

# print(efteling.voegAttractieToe(max_en_moritz))
# print(efteling.voegAttractieToe(de_baron))
# print(efteling.printOverzicht())

class Pretpark:
    def __init__(self, naam):
        self.__naam = None
        self.__attracties = []

        self.naam = naam

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, naam):
        if naam == "":
            raise ValueError("Naam mag niet leeg zijn")
        else:
            self.__naam = naam

    def voegAttractieToe(self, attractie):
        for a in self.__attracties:
            if a.naam.lower().replace(" ", "") == attractie.naam.lower().replace(" ", ""):
                raise ValueError("Deze attractie bestaat al.")
        self.__attracties.append(attractie)
        return self.__attracties

    def printOverzicht(self):
        attractie_aantal = len(self.__attracties)
        bezoekers_totaal = sum(attractie.bezoekers for attractie in self.__attracties)
        attractie_tekst = "attracties" if attractie_aantal != 1 else "attractie"
        keer_tekst = "keer" if bezoekers_totaal != 1 else "keer"
        return f"{self.naam} is een pretpark met {attractie_aantal} {attractie_tekst} die in totaal {bezoekers_totaal} {keer_tekst} werden bezocht."


class Attractie:
    def __init__(self, naam, grootte):
        self.__naam = None
        self.__grootte = None
        self.naam = naam
        self.grootte = grootte
        self.bezoekers = 0

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, naam):
        if naam == "":
            raise ValueError("Naam mag niet leeg zijn")
        self.__naam = naam

    @property
    def grootte(self):
        return self.__grootte

    @grootte.setter
    def grootte(self, grootte):
        if grootte < 0:
            raise ValueError("Grootte mag niet negatief zijn")
        self.__grootte = grootte

    def bezoek(self, bezoeker_grootte):
        if bezoeker_grootte >= self.grootte:
            self.bezoekers += 1
            return self.bezoekers
        else:
            error_message = f"Bezoeker te klein voor attractie '{self.naam}'"
            with open("log.txt", "a") as log_file:
                log_file.write(error_message + "\n")
            print(error_message)


efteling = Pretpark("De Efteling")
efteling.printOverzicht()

# Voeg De Pagode toe
pagode = Attractie("De Pagode", 0)
efteling.voegAttractieToe(pagode)
efteling.printOverzicht()

# Voeg Max & Moritz en De Baron toe
max_en_moritz = Attractie("Max & Moritz", 100)
de_baron = Attractie("De Baron", 132)

print(efteling.voegAttractieToe(max_en_moritz))
print(efteling.voegAttractieToe(de_baron))
print(efteling.printOverzicht())
