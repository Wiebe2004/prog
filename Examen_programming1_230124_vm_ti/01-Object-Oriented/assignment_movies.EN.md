# Exam Question 1: Movies

* Place all code for this exercise in `movies.py`.
* In these instructions we will always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_tests_movies.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests_movies.py
    ```

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect.
    But passed tests do not mean that your code is fully correct!
  * This test file must be able to run correctly to earn credit.

## Class Movie
The class `Movie` represents different movies.  

* Define a class Movie.  
* Define Movie's constructor:  
  * The constructor takes three parameters: `title` (a string), `genres` (a list of genres that are associated with the movie), and `sequel` (a boolean: True if the movie has a sequel, False otherwise).
    * It is not necessary to check whether the type of the parameters is correct.
  * Examples:  
    * title = "Inception"; inception_genres = ["Sci-Fi","Action","Thriller"]; sequel = False  
    * title = "The Dark Knight"; dark_knight_genres = ["Action","Crime","Drama"]; sequel = True  
    * title = "The Shawshank Redemption"; shawshank_genres = ["Drama","Crime"]; sequel = False  
* Store title and sequel in public fields.  
* Store genres in a private field available via a property.  
* Define a setter for genres.
  * A movie must have at least one genre. If the list of genres is missing or empty, the setter should raise a ValueError.  
* Define a method `get_info()` which returns a string representation of the movie, as shown below.  


# Class FilmFestival  

The class FilmFestival represents an event where a sequence of movies will be screened.  

* Define a class `FilmFestival`.  
* Define `FilmFestival`'s constructor:  
  * The constructor takes one parameter: `name` (a string).  
  * A `FilmFestival` also includes a field `movies` which is a list of movies that will be screened.  This list is empty when a `FilmFestival` is being created.
* Store `name` in a public field.  
* Store `movies` in a private field which can be accessed via a property.  
* Define a method `add_movie(movie)` which adds `movie` to `movies`.  
  * A `Movie` should not be added if another `Movie` with the same name is already present in the list. While checking wheter 2 `Movie`s have the same name, you ignore capital letters.
* Define a method `remove_movie(title)` which removes a `Movie` from `movies`, based on the title provided. If there is no `Movie` in `movies` with this title, do nothing. While checking wheter 2 `Movie`'s have the same name, you ignore capital letters.
* Both `add_movie(movie)` and `remove_movie(title)` possibly change the value of the field `movies` but do not return anything.  

## Example usage

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
