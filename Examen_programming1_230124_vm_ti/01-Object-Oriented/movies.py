class Movie:
    def __init__(self,title,genres,sequal):
        self.title = title
        self.sequel = sequal
        self.__genres = genres

    @property
    def genres(self):
        return self.__genres
    
    @genres.setter
    def genres(self, genres):
        if genres is None or len(genres) < 0:
            raise ValueError("Lijst van genres is leeg.")
        self.__genres = genres

    def __printGenres(self):
        res = ""
        for g in self.genres:
            res += g + " "
        return res[:-1]

    def get_info(self):
        No = ""
        if not self.sequel:
            No = "No "
        return f"Movie: {self.title}, Genres: {self.__printGenres()}, Has {No}Sequel"
    

class FilmFestival:
    def __init__(self, name):
        self.name = name
        self.__movies = list()

    @property
    def movies(self):
        return self.__movies
    
    def __findMovieIndex(self,title):
        for i in range(0,len(self.movies)):
            if self.movies[i].title.lower() == title.lower():
                return i
        return -1
    
    def add_movie(self,movie):
        if self.__findMovieIndex(movie.title) < 0:
            self.__movies.append(movie)
    
    def remove_movie(self,title):
        index = self.__findMovieIndex(title)
        if index >= 0:
            self.__movies.pop(index)


inception_movie = Movie("Inception",["Sci-Fi","Action","Thriller"],False)
dark_knight_movie = Movie("The Dark Knight",["Action","Crime","Drama"],True)
shawshank_movie = Movie("The Shawshank Redemption",["Drama","Crime"],False) 

filmfest_parade = FilmFestival("FilmFest Parade") 

filmfest_parade.add_movie(inception_movie)
filmfest_parade.add_movie(dark_knight_movie)
filmfest_parade.add_movie(shawshank_movie) 

filmfest_parade.remove_movie("inception")

for movie in filmfest_parade.movies:  
    print(movie.get_info())  