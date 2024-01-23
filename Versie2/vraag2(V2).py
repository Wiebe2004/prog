class Film:
    def __init__(self, titel, speelduur):
        self.titel = titel
        assert speelduur >= 60, "De speelduur moet minstens 60min zijn"
        self.speelduur = speelduur
        self.rating = 0

    def zet_rating(self, lijst):
        geldige_ratings = [rating for rating in lijst if 0 <= rating <= 5]
        if geldige_ratings:
            self.rating = sum(geldige_ratings) / len(geldige_ratings)
        return self.rating

    def __str__(self):
        return (
            f"Titel: {self.titel}, Speelduur: {self.speelduur}, Rating: {self.rating}"
        )


class Zaal:
    def __init__(self, zaalnummer):
        self.film = None
        self.zaalnummer = zaalnummer

    def zet_film(self, film_object):
        if not self.film:
            self.film = film_object

    def verwijder_film(self):
        self.film = None

    def dezelfde_film(self, andere_zaal):
        return (
            self.film and andere_zaal.film and self.film.titel == andere_zaal.film.titel
        )

    def zet_rating(self, lijst):
        if self.film:
            self.film.zet_rating(lijst)

    def __str__(self):
        return f"Zaal: {self.zaalnummer}\nFilm: {str(self.film)}"


# Applicatie
# film_frozen = Film("Frozen", 135)
# zaal_12 = Zaal(12)
# zaal_14 = Zaal(14)

# zaal_12.zet_film(film_frozen)
# zaal_14.zet_film(film_frozen)

# if zaal_12.dezelfde_film(zaal_14):
#     print(
#         f"In zaal met nummer {zaal_12.zaalnummer} speelt dezelfde film als de film in zaal met nummer {zaal_14.zaalnummer}"
#     )
# else:
#     print(
#         f"In zaal met nummer {zaal_12.zaalnummer} speelt een andere film dan de film in zaal met nummer {zaal_14.zaalnummer}"
#     )

# film_andere = Film("Andere Film", 120)
# zaal_andere = Zaal(11)

# zaal_andere.zet_film(film_andere)

# if zaal_12.dezelfde_film(zaal_andere):
#     print(
#         f"In zaal met nummer {zaal_12.zaalnummer} speelt dezelfde film als de film in zaal met nummer {zaal_andere.zaalnummer}"
#     )
# else:
#     print(
#         f"In zaal met nummer {zaal_12.zaalnummer} speelt een andere film dan de film in zaal met nummer {zaal_andere.zaalnummer}"
#     )

# zaal_12.zet_rating([1, 2, 3, 4, 10, 5, 1, 2, 3, 4, 5, 20])
# zaal_14.zet_rating([5, 5, 5, 5, 5])

# print(str(zaal_12))
# print(str(zaal_14))

frozen = Film("Frozen",135)
zaal1 = Zaal(12)
zaal2 = Zaal(14)
zaal1.zet_film(frozen)
zaal2.zet_film(frozen)

if zaal1.film == zaal2.film:
    info = "dezelfde film als"
else:
    info = "een andere film dan"
print('in zaal met nummer ' + str(zaal1.zaalnummer) + " speelt " + info + " de film in zaal met nummer " + str(zaal2.zaalnummer))
zaal3 = Zaal(11)
andere_film = Film("Andere",100)
zaal3.zet_film(andere_film)
if zaal1.film == zaal3.film:
    info = "dezelfde film als"
else:
    info = "een andere film dan"
print('in zaal met nummer ' + str(zaal1.zaalnummer) + " speelt " + info + " de film in zaal met nummer " + str(zaal3.zaalnummer))

zaal1.zet_rating([1,2,3,4,10,5,1,2,3,4,5,20])
zaal2.zet_rating([5,5,5,5,5])
print(zaal1)