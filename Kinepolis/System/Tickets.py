class Tickets:
    def __init__(self, userID, playID, numberOfSeats, userInstance, playInstance, timeSlots):
        firstName, lastName, mail = userInstance.getUserInfo(userID)
        roomName, timeSlot, date, movieTitle = playInstance.getInfo(playID)
        self.name = lastName + " " + firstName
        self.playID = playID
        self.room = roomName
        self.time = timeSlots.slotIDToTime(timeSlot)
        self.date = date
        self.numberOfSeats = numberOfSeats

    def printTicket(self):
        print(self.name)
        print(self.numberOfSeats)
        print(self.playID + " " + self.room)
        print(self.date + " " + self.time)