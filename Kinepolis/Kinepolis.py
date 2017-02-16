from System.Movies import *
from System.Plays import *
from System.Reservations import *
from System.Rooms import *
from System.Users import *
from System.Slots import *
import Log
from os import listdir, remove


### HELPER FUNCTIONS ###

def createLogFile(date, timestamp):
    Log.log(allMovies, allPlays, timestamp, date, allSlots)

def executeInstruction(instruction, initFinished, timeSlotPrompt):
    splitInstruction = instruction.split()
    if initFinished:
        print(splitInstruction[0] + " " + splitInstruction[1] + ":")
        if splitInstruction[2] == "reserveer":
            allReservations.createReservation(int(splitInstruction[3]),
                                              int(splitInstruction[4]),
                                              int(splitInstruction[5]))
            firstName, lastName, mail = allUsers.getUserInfo(int(splitInstruction[3]))
            roomName, timeSlot, date, movieID = allPlays.getInfo(int(splitInstruction[4]))
            movieTitle = allMovies.getMovieTitle(movieID)
            time = allSlots.slotIDToTime(timeSlot)
            print("{} {} bought {} tickets for the screening of \"{}\" on {} at {}".format(firstName, lastName, splitInstruction[5], movieTitle, date, time))
        elif splitInstruction[2] == "ticket":
            roomName, timeSlot, date, movieID = allPlays.getInfo(int(splitInstruction[3]))
            if splitInstruction[4] == "1":
                print("1 person has entered room #{}".format(roomName))
            else:
                print("{} people have entered room #{}".format(splitInstruction[4], roomName))
            room = allRooms.retrieveRoom(roomName)
            room.enterRoom(timeSlot, date, int(splitInstruction[4]))
        elif splitInstruction[2] == "log":
            createLogFile(splitInstruction[0], splitInstruction[1])
            print("A log file was created and placed in the Output folder")

    else:
        if splitInstruction[0] == "zaal":
            allRooms.addRoom(int(splitInstruction[1]),
                             int(splitInstruction[2]))
            print("Room #{} with {} seats is now available for screening movies".format(splitInstruction[1], splitInstruction[2]))

        elif splitInstruction[0] == "film":
            privateSplit = instruction.split("\"")
            allMovies.addMovie(privateSplit[1],
                               float(privateSplit[2]),
                               int(splitInstruction[1]))
            rating = int(float(privateSplit[2]) * 100)
            print("The movie titled \"{}\" with a rating of {}% is now available for viewing".format(privateSplit[1], rating))

        elif splitInstruction[0] == "vertoning":
            allPlays.addPlay(int(splitInstruction[2]),
                             int(splitInstruction[3]),
                             splitInstruction[4],
                             int(splitInstruction[5]),
                             int(splitInstruction[1]))
            movieTitle = allMovies.getMovieTitle(int(splitInstruction[5]))
            time = allSlots.slotIDToTime(int(splitInstruction[3]))
            print("A screening of \"{}\" has been scheduled on {} at {} in room #{} ".format(movieTitle, splitInstruction[4], time, splitInstruction[2]))

        elif splitInstruction[0] == "gebruiker":
            allUsers.addUser(splitInstruction[2],
                             splitInstruction[3],
                             splitInstruction[4],
                             int(splitInstruction[1]))
            print("{} {} has been registered with following email address: {} ".format(splitInstruction[2], splitInstruction[3], splitInstruction[4]))

        elif splitInstruction[0] == "tijdsslot" and timeSlotPrompt.upper() == "N":
            allSlots.addSlot(splitInstruction[2],
                             int(splitInstruction[1]))
            print("Movies can now be screened at {}".format(splitInstruction[2]))


### DATA STRUCTURE INIT ###
## timeslots
allSlots = Slots()
## rooms
allRooms = Rooms()
## films
allMovies = Movies()
## vertoningen
allPlays = Plays(allRooms, allMovies)
## users
allUsers = Users()
## reservations
allReservations = Reservations(allRooms, allUsers, allPlays, allSlots)


### SYSTEM INIT ###
print("RUNNING KINEPOLIS")

# input selection
print("\n~AVAILABLE INPUT FILES~")
fileNumber = 1
files = listdir("Input/Kinepolis/")

for file in files:
    print(str(fileNumber) + ") " + file)
    fileNumber += 1

while True:
    inputFileNumber = input(
        "\nSelect number of file you wish to use as input:\n")
    if int(inputFileNumber) not in range(1, len(files) + 1):
        print("Invalid file number, please try again")
    else:
        break

pathToInputFile = "Input/Kinepolis/" + files[int(inputFileNumber) - 1]
with open(pathToInputFile) as inputF:
    instructions = [instruction.strip() for instruction in
                    inputF.readlines() if
                    (instruction[0] != "#" and len(instruction) > 1)]

clearPrompt = input("Would you like to clear the Output folder? (Y/N)\n")
if clearPrompt.upper() == "Y":
    files = [f for f in listdir("Output/KinepolisLog")]
    for f in files:
        remove("Output/KinepolisLog/" + f)

# default timeslots?
timeSlotPrompt = input("Would you like to use the default timeslots? (Y/N)\n")
if timeSlotPrompt.upper() == "Y":
    allSlots.setupDefaultSlots()


### INPUT PROCESSING AND OUTPUT CREATION ###
instructions.reverse()
initFinished = False
while len(instructions) > 0:
    nextInstruction = instructions.pop()
    if nextInstruction == "init":
        print("\n~INITIALIZING SYSTEM~\n")
    elif nextInstruction == "start":
        print("\n~INITIALIZATION FINISHED~\n~STARTING SYSTEM~")
        initFinished = True
    elif len(nextInstruction) == 0:
        pass
    else:
        executeInstruction(nextInstruction, initFinished, timeSlotPrompt)




"""from System.Movies import *
from System.Plays import *
from System.Reservations import *
from System.Rooms import *
from System.Users import *
from System.Slots import *

### INIT ###
# timeslots
timeSlots = Slots()
timeSlots.setupDefaultSlots()

# rooms
allRooms = Rooms()
allRooms.addRoom(1, 200)

#films
allMovies = Movies()
allMovies.addMovie("The Matrix", 0.95, 3)

# vertoningen, in vb werkt men met slots, wij met tijdstippen
allPlays = Plays(allRooms, allMovies)
allPlays.addPlay(1, 1, "2017-01-01", "The Matrix", 9)
allPlays.addPlay(1, 2, "2017-01-01", "The Matrix", 10)
allPlays.addPlay(1, 3, "2017-01-01", "The Matrix", 11)

# users
allUsers = Users()
allUsers.addUser("John", "Doe", "john@doe.com", 1)
allUsers.addUser("Tom", "Hofkens", "tom.hofkens@uantwerpen.be", 2)

# reservations
allReservations = Reservations(allRooms, allUsers, allPlays, timeSlots)

### START ###

allReservations.createReservation(1, 9, 2)
allReservations.createReservation(2, 9, 8)
allReservations.createReservation(2, 10, 2)"""
