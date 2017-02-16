from System.ADTs.Table import *

class SingleSlot:
    def __init__(self, time, slotID):
        self.time = time
        self.id = slotID

class Slots:
    def __init__(self):
        self.allSlots = Table("23")

    def addSlot(self, time, slotID):
        return self.allSlots.insert((slotID, time))

    def setupDefaultSlots(self):
        self.addSlot("14:30", 1)
        self.addSlot("17:00", 2)
        self.addSlot("20:00", 3)
        self.addSlot("22:30", 4)

    def slotIDToTime(self, slotID):
        return self.allSlots.retrieve(slotID)[1]

    def listAllSlots(self):
        returnList = []
        idList = self.allSlots.traverse()
        for slot in idList:
            returnList.append(self.slotIDToTime(slot))
        return returnList


