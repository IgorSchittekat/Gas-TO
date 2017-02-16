from System.ADTs.Table import *


class SinglePlay:
    def __init__(self, roomName, timeSlot, date, movieID, playID):
        self.roomName = roomName
        self.timeSlot = timeSlot
        self.date = date
        self.movieID = movieID
        self.playID = playID


class Plays:
    def __init__(self, allRooms, allMovies):
        self.allPlays = Table("ll")
        self.allRooms = allRooms
        self.allMovies = allMovies

    def getAllPlays(self):
        self.allPlays.table.bubbleSort("Play") # sort for linked lists
        return self.allPlays.traverse()

    def addPlay(self, roomName, timeSlot, date, movieID, playID):
        toegevoegd = False
        if self.allRooms.isFree(roomName, timeSlot, date):
            self.allRooms.reserveRoom(roomName, timeSlot, date)
            newPlay = SinglePlay(roomName, timeSlot, date, movieID, playID)
            self.allPlays.insert((playID, newPlay))
            toegevoegd = True
        return toegevoegd

    def removePlay(self, playID):
        playExists, playData = self.allPlays.retrieve(playID)
        if playExists:
            self.allRooms.cancelReservation(playData.roomName, playData.timeSlot, playData.date)
            return self.allPlays.delete(playID)
        return playExists

    def getInfo(self, playID):
        playExists, playData = self.allPlays.retrieve(playID)
        return playData.roomName, playData.timeSlot, playData.date, playData.movieID

    def changeRoomName(self, playID, newRoomName):
        veranderd = False
        playExists, playData = self.allPlays.retrieve(playID)
        if playExists:
            if self.allRooms.isFree(newRoomName, playData.timeSlot, playData.date):
                playData.roomName = newRoomName
                veranderd = True
            return veranderd
        return playExists

    def changeTime(self, playID, newTimeSlot):
        veranderd = False
        playExists, playData = self.allPlays.retrieve(playID)
        if playExists:
            if self.allRooms.isFree(playData.roomName, newTimeSlot, playData.date):
                playData.timeSlot = newTimeSlot
                veranderd = True
            return veranderd
        return playExists

    def changeDate(self, playID, newDate):
        veranderd = False
        playExists, playData = self.allPlays.retrieve(playID)
        if playExists:
            if self.allRooms.isFree(playData.roomName, playData.timeSlot, newDate):
                playData.date = newDate
                veranderd = True
            return veranderd
        return playExists

    def changeMovie(self, playID, newMovieID):
        playExists, playData = self.allPlays.retrieve(playID)
        if playExists:
            playData.movieID = newMovieID
        return playExists
