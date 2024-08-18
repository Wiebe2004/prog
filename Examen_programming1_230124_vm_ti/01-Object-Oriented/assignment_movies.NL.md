# Examenvraag 1: Movies

* Plaats alle code voor deze oefening in `movies.py`.
* In deze instructies zullen we altijd `self` weglaten.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een `basic_tests_movies.py` bestand ontvangen dat basis testen bevat, zoals of bepaalde classes bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_tests_movies.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich op die klasse richten worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Het niet slagen/overslaan van tests betekent dat je code zeker incompleet of incorrect is.
    Maar geslaagde tests betekenen niet dat je code volledig correct is!
  * Dit testbestand moet correct uitgevoerd kunnen worden om punten te verdienen.

## Klasse Movie
De klasse `Movie` vertegenwoordigt verschillende films.  

* Definieer een klasse Movie.  
* Definieer de constructor van Movie:  
  * De constructor neemt drie parameters: `title` (een string), `genres` (een lijst van genres die geassocieerd zijn met de film), en `sequel` (een boolean: True als de film een vervolg heeft, False anders).
    * Het is niet nodig om af te toetsen of het type van de parameters correct is.
  * Voorbeelden:  
    * title = "Inception"; inception_genres = ["Sci-Fi","Action","Thriller"]; sequel = False  
    * title = "The Dark Knight"; dark_knight_genres = ["Action","Crime","Drama"]; sequel = True  
    * title = "The Shawshank Redemption"; shawshank_genres = ["Drama","Crime"]; sequel = False  
* Sla title en sequel op in public fields.  
* Sla genres op in een private field dat beschikbaar is via een property.  
* Definieer een setter voor genres.
  * Een film moet minstens één genre hebben. Als de lijst van genres ontbreekt of leeg is, moet de setter een ValueError oproepen.  
* Definieer een methode `get_info()` die een stringrepresentatie van de film teruggeeft, zoals onderaan getoond.  


# Klasse FilmFestival  

De klasse `FilmFestival` vertegenwoordigt een evenement waar een reeks films wordt vertoond.  

* Definieer een klasse `FilmFestival`.  
* Definieer de constructor van `FilmFestival`:  
  * De constructor neemt één parameter: `name` (een string).  
  * Een `FilmFestival` bevat ook een veld `movies` dat een lijst is van films die vertoond zullen worden. Deze lijst is leeg wanneer een `FilmFestival` wordt aangemaakt.
* Sla `name` op in een public field.  
* Sla `movies` op in een private field dat toegankelijk is via een property.  
* Definieer een methode `add_movie(movie)` die `movie` toevoegt aan `movies`.  
  * Een `Movie` mag niet toegevoegd worden wanneer er al een `Movie` met dezelfde naam in de lijst staat. Bij de controle of 2 `Movie`s dezelfde naam hebben, hou je geen rekening met hoofdletters. 
* Definieer een methode `remove_movie(title)` die een `Movie` verwijdert uit `movies`, gebaseerd op de opgegeven titel. Als er geen `Movie` is in `films` met deze titel, doe dan niets.  Bij de controle of 2 `Movie`'s dezelfde naam hebben, hou je geen rekening met hoofdletters. 
* Zowel `add_movie(movie)` als `remove_movie(title)` veranderen eventueel de waarde van het veld `movies` maar geven niets terug.  

## Voorbeeldgebruik

```python
>>> inception_movie = Movie("Inception",["Sci-Fi","Action","Thriller"],False)
>>> dark_knight_movie = Movie("The Dark Knight",["Action","Crime","Drama"],True)
>>> shawshank_movie = Movie("The Shawshank Redemption",["Drama","Crime"],False) 

>>> filmfest_parade = FilmFestival("FilmFest Parade") 

>>> filmfest_parade.add_movie(inception_movie)
>>> filmfest_parade.add_movie(dark_knight_movie)
>>> filmfest_parade.add_movie(shawshank_movie) 

>>> filmfest_parade.remove_movie("inception")

>>> for movie in filmfest_parade.movies:  
      print(movie.get_info())  

Movie: The Dark Knight, Genres: Action Crime Drama, Has Sequel 
Movie: The Shawshank Redemption, Genres: Drama Crime, Has No Sequel
```
