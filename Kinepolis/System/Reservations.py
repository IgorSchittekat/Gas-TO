from System.Tickets import *
from System.ADTs.Table import *


class SingleReservation:
    def __init__(self, userID, playID, timeSlot, date, numbOfSeats, reservationID):
        self.userID = userID #integer
        self.playID = playID #integer
        self.timeSlot = timeSlot
        self.date = date #string
        self.numbOfSeats = numbOfSeats
        self.reservationID = reservationID


class Reservations:
    def __init__(self, allRooms, allUsers, allPlays, timeSlots):
        self.allReservations = Table("queue")
        self.allRooms = allRooms
        self.allPlays = allPlays
        self.allUsers = allUsers
        self.timeSlots = timeSlots
        self.totalReservations = 0
        self.newReservationId = 1

    def createReservation(self, userID, playID, numbOfSeats):
        roomName, timeSlot, date, movieTitle = self.allPlays.getInfo(playID)
        if self.allRooms.showEmptySeats(roomName, timeSlot, date) >= numbOfSeats:
            self.allRooms.changeEmptySeats(roomName, timeSlot, date, numbOfSeats)
            self.totalReservations += 1
            newReservation = SingleReservation(userID, playID, timeSlot, date, numbOfSeats, self.newReservationId)
            self.allReservations.insert((self.newReservationId, newReservation))
            self.newReservationId += 1
            newTicket = Tickets(userID, playID, numbOfSeats, self.allUsers, self.allPlays, self.timeSlots)
            return newTicket

    def changeReservation(self, reservationID, newNumberOfSeats):
        reservationExists, reservationInfo = self.allReservations.retrieve(reservationID)
        if reservationExists:
            roomName, timeSlot, date, movieTitle = self.allPlays.getInfo(reservationInfo[1].playID)
            seatDelta = newNumberOfSeats - reservationInfo[1].numberOfSeats
            if seatDelta == 0:
                pass
            elif seatDelta < 0 or seatDelta <= self.allRooms.showEmptySeats(roomName, timeSlot, date):
                self.allRooms.changeEmptySeats(roomName, timeSlot, date, seatDelta)
            reservationInfo[1].numberOfSeats = newNumberOfSeats
            newTicket = Tickets(reservationInfo[1].userID,
                               reservationInfo[1].playID,
                               newNumberOfSeats,
                               self.allUsers,
                               self.allPlays, self.timeSlots)
            return newTicket

    def cancelReservation(self, reservationID):
        if self.allReservations.delete(reservationID):
            self.totalReservations -= 1
            return True
        return False
