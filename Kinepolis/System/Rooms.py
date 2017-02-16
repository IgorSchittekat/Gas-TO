from System.ADTs.Table import *


class SingleRoom:

    def __init__(self, roomName, seats):
        self.roomName = roomName
        self.seats = seats
        self.allReservations = Table("23")  # datastructure

    def reserve(self, timeSlot, date):
        # time: 00:00
        # date: dd/mm/jjjj
        usedSeats = Table("stack")
        entered = Table("stack")
        return self.allReservations.insert((date + " " + str(timeSlot), (usedSeats, entered)))

    def cancel(self, timeSlot, date):
        return self.allReservations.delete(date + " " + str(timeSlot))

    def showReservations(self):
        return self.allReservations.traverse()

    def showEmptySeats(self, timeSlot, date):
        usedSeats = self.allReservations.retrieve(date + " " + str(timeSlot))[1]
        if usedSeats is None:
            return self.seats
        return self.seats - usedSeats[0].table.size

    def isFree(self, timeSlot, date):
        return not self.allReservations.retrieve(date + " " + str(timeSlot))[0]

    def changeSeats(self, seats, timeSlot, date):
        # Positive seats decreases emptySeats
        # Negative seats increases emptySeats
        usedSeats = self.allReservations.retrieve(date + " " + str(timeSlot))
        if usedSeats[1] is None:
            return False
        else:
            usedSeats = usedSeats[1][0]
        if seats < 0:
            if abs(seats) <= usedSeats.table.size:
                for _ in range(abs(seats)):
                    usedSeats.table.pop()
                return True
            return False
        elif seats > 0:
            if seats + usedSeats.table.size <= self.seats:
                for _ in range(seats):
                    usedSeats.table.push("X")
                return True
            return False

    def enterRoom(self, timeSlot, date, peopleAmount):
        self.changeSeats((-1)*peopleAmount, timeSlot, date)
        entered = self.allReservations.retrieve(date + " " + str(timeSlot))[1]
        if entered is not None:
            entered = entered[1]
            for _ in range(peopleAmount):
                entered.table.push("X")

    def entered(self, timeSlot, date):
        entered = self.allReservations.retrieve(date + " " + str(timeSlot))[1]
        if entered is not None:
            return entered[1].table.size
        return 0


class Rooms:

    def __init__(self):
        self.allRooms = Table("hsep", 10, "dll")             # datastructure
        self.totalRooms = 0

    def addRoom(self, room, seats=100):
        if type(room) != SingleRoom:
            room = SingleRoom(room, seats)
        roomName = room.roomName
        rv = self.allRooms.insert((roomName, room))
        if rv is True:
            self.totalRooms += 1
        return rv

    def deleteRoom(self, roomName):
        rv = self.allRooms.delete(roomName)
        if rv is True:
            self.totalRooms -= 1
        return rv

    def retrieveRoom(self, roomName):
        return self.allRooms.retrieve(roomName)[1]

    def showRooms(self):
        return self.allRooms.traverse()

    def showReservations(self, roomName):
        room = self.allRooms.retrieve(roomName)[1]
        return room.showReservations()

    def reserveRoom(self, roomName, timeSlot, date):
        room = self.allRooms.retrieve(roomName)[1]
        return room.reserve(timeSlot, date)

    def cancelReservation(self, roomName, timeSlot, date):
        room = self.allRooms.retrieve(roomName)[1]
        return room.cancel(timeSlot, date)

    def showEmptySeats(self, roomName, timeSlot, date):
        room = self.allRooms.retrieve(roomName)[1]
        return room.showEmptySeats(timeSlot, date)

    def isFree(self, roomName, timeSlot, date):
        room = self.allRooms.retrieve(roomName)[1]
        return room.isFree(timeSlot, date)


    def changeEmptySeats(self, roomName, timeSlot, date, seats):
        if self.allRooms.retrieve(roomName) is False:
            return False
        room = self.allRooms.retrieve(roomName)[1]
        return room.changeSeats(seats, timeSlot, date)
