
from System.ADTs.Table import *

class SingleMovie:
    def __init__(self, title, rating, movieID):
        self.movieID = movieID
        self.title = title
        self.rating = rating


class Movies:
    def __init__(self):
        self.allFilms = Table("bst") #datastructure
        self.totalFilms = 0

    def addMovie(self, movie, rating=0.7, movieID=0):
        if type(movie) != SingleMovie:
            movie = SingleMovie(movie, rating, movieID)
        rv = self.allFilms.insert((movie.movieID, movie))
        if rv is True:
            self.totalFilms += 1
        return rv

    def deleteMovie(self, movieID):
        rv = self.allFilms.delete(movieID)
        if rv is True:
            self.totalFilms -= 1
        return rv

    def getMovies(self):
        return self.allFilms.traverse()

    def changeRating(self, movieID, newRating):
        if self.allFilms.retrieve(movieID)[0] is False:
            return False
        film = self.allFilms.retrieve(movieID)[1]
        film.rating = newRating
        return True

    def getMovieTitle(self, movieID):
        return self.allFilms.retrieve(movieID)[1].title
