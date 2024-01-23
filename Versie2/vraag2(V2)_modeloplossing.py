from copy import copy
class Film:
    def __init__(self,titel,speelduur) -> None:
        assert speelduur >= 60, "speelduur van film moet minimaal 60 minuten zijn"
        self.titel = titel
        self.speelduur = speelduur
        self.rating = 0

    def geef_rating(self,ratings):
        l = [x for x in ratings if x >= 0 and x <= 5]
        self.rating = (int(sum(l)/len(l)) if len(l) != 0 else 0)
    
    def __eq__(self, andere_film) -> bool:
        if not isinstance(andere_film,self.__class__):
            return False
        else:
            return self.titel == andere_film.titel

    def __str__(self) -> str:
        uur = self.speelduur // 60
        m = self.speelduur %60
        srating = (self.rating*'*') if self.rating != 0 else "geen rating"
    
        return self.titel + f"({uur}u{m}min;rating: {srating})" 
class Zaal:
    def __init__(self, nummer) -> None:
        self.nummer = nummer
        self.film = None
    
    def zet_film(self,film):
        if  isinstance(film,Film) and self.film == None:
            self.film = copy(film)
    
    def verwijder_film(self):
        self.film = None
    
    def zelfde_film(self, andere_zaal):
        if not isinstance(andere_zaal, Zaal):
            return False
        else:
            return self.film == andere_zaal.film
    
    def zet_rating(self,ratings):
        if self.film != None:
            self.film.geef_rating(ratings)
    
    def __str__(self) -> str:
        zin1 = "Zaal: " + str(self.nummer) 
        zin2 = str(self.film) if self.film != None else "geen film"
        return zin1 + "\n" + zin2 

frozen = Film("Frozen",135)
zaal1 = Zaal(12)
zaal2 = Zaal(14)
zaal1.zet_film(frozen)
zaal2.zet_film(frozen)

if zaal1.film == zaal2.film:
    info = "dezelfde film als"
else:
    info = "een andere film dan"
print('in zaal met nummer ' + str(zaal1.nummer) + " speelt " + info + " de film in zaal met nummer " + str(zaal2.nummer))
zaal3 = Zaal(11)
andere_film = Film("Andere",100)
zaal3.zet_film(andere_film)
if zaal1.film == zaal3.film:
    info = "dezelfde film als"
else:
    info = "een andere film dan"
print('in zaal met nummer ' + str(zaal1.nummer) + " speelt " + info + " de film in zaal met nummer " + str(zaal3.nummer))

zaal1.zet_rating([1,2,3,4,10,5,1,2,3,4,5,20])
zaal2.zet_rating([5,5,5,5,5])
print(zaal2)