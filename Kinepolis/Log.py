import System.Plays as Plays
import System.Rooms as Rooms
import System.Movies as Movies
import System.Slots as Slots
import System.Reservations as Reservations
import System.Users as Users


def log(allMovies, allPlays, inTime, inDate, allSlots):
    # allPlays a list of all the Plays you want
    # inTime is the time you want the log to check
    # indate is the date you want the log to check
    # allSlots is a list or tuple of all the available slots
    date = list(inDate)
    day =str(date[8] + date[8])
    month = str(date[5] + date[6])
    year = str(date[0] + date[1] + date[2] + date[3])

    file = open("Output/KinepolisLog/log" + year + month + day + ".html", "a+")
    file.write("<html>\n"
               "\t<head>\n"
               "\t<style>\n"
               "\t\ttable {\n"
               "\t\t\tborder-collapse: collapse;\n"
               "\t\t}\n\n"
               "\t\ttable, td, th {\n"
               "\t\t\tborder: 1px solid black;\n"
               "\t\t}\n"
               "\t</style>\n"
               "</head>\n"
               "\t<body>\n"
               "\t\t<h1>Log op " + inDate + " " + inTime + "</h1>\n")
    file.write("\t\t<table>\n"
               "\t\t\t<thead>\n"
               "\t\t\t\t<td>Datum</td>\n"
               "\t\t\t\t<td>Room</td>\n")
    for i in allSlots.listAllSlots():
        file.write("\t\t\t\t<td>" + i + "</td>\n"
                   "\t\t\t\t<td>Status</td>\n")
    file.write("\t\t\t</thead>\n")

    plays = allPlays.getAllPlays()
    rooms = []
    timeIDs = []
    dates = []
    titles = []
    for playID in plays:
        roomName, time, date, movieTitle = allPlays.getInfo(playID)
        rooms.append(roomName)
        timeIDs.append(time)
        dates.append(date)
        titles.append(movieTitle)
    times = []
    for i in timeIDs:
        times.append(allSlots.slotIDToTime(i))

    while len(rooms) > 0:
        file.write("\t\t\t<tbody>\n"
                   "\t\t\t\t<tr>\n")
        smallest_date = dates[0]
        room = rooms[0]
        index = 0
        for i in range(len(dates)):
            if dates[i] < smallest_date:
                smallest_date = dates[i]
                room = rooms[i]
                index = i
        file.write("\t\t\t\t<td>" + smallest_date + "</td>\n")

        smallest_room = room
        for i in range(len(rooms)):
            if rooms[i] < smallest_room and dates[i] == smallest_date:
                smallest_room = rooms[i]
                index = i
        file.write("\t\t\t\t<td>" + str(smallest_room) + "</td>\n")
        for slot in allSlots.listAllSlots():
            title = ""
            for i in range(len(times)):
                if times[i] == slot and rooms[i] == smallest_room and dates[i] == smallest_date:
                    title = titles[i]
                    time = times[i]
                    timeID = timeIDs[i]
                    date = dates[i]

            if type(title) == str:
                titleString = title
            elif title != "":
                titleString = allMovies.getMovieTitle(int(title))
            else:
                titleString = ""
            file.write("\t\t\t\t<td>" + titleString + "</td>\n")
            if title == "":
                state = ""
            else:
                state = calculate_state(room, allPlays.allRooms, timeID, time, date, inTime, inDate, allSlots)

            file.write("\t\t\t\t<td>" + state + "</td>\n")

        file.write("\t\t\t\t</tr>\n"
                   "\t\t\t</tbody>\n")

        del_index = []
        for i in range(len(rooms)):
            if rooms[i] == rooms[index] and dates[i] == dates[index]:
                del_index.insert(0, i)

        for index in del_index:
            del rooms[index]
            del dates[index]
            del times[index]
            del titles[index]
            del timeIDs[index]


    file.write("\t\t</table>\n"
               "\t</body>\n"
               "</html>")

    file.close()


def calculate_state(room, allRooms, askedTimeID, askedTime, askedDate, currentTime, currentDate, allSlots):
    currentRoom = allRooms.retrieveRoom(room)
    usedSeats = currentRoom.seats - allRooms.showEmptySeats(room, askedTimeID, askedDate)
    timeNow = currentDate + " " + currentTime
    time = askedDate + " " + askedTime
    entered = currentRoom.entered(askedTimeID, askedDate)
    if time <= timeNow:
        if usedSeats == 0:
            if entered == 0:
                state = "C"
            else:
                state = "F: " + str(entered)
        else:
            state = "W: " + str(usedSeats)
    else:
        state = "G: " + str(usedSeats)
    return state

if __name__ == "__main__":
    allSlots = Slots.Slots()
    allSlots.setupDefaultSlots()

    allRooms = Rooms.Rooms()
    allRooms.addRoom(1, 20)
    allRooms.addRoom(2, 20)
    allRooms.addRoom(3, 15)
    allRooms.addRoom(4, 25)

    allFilms = Movies.Movies()
    allFilms.addMovie("The Sting", 8.3, 1)
    allFilms.addMovie("The Terminator", 8.0, 2)
    allFilms.addMovie("Ice Age", 7.6, 3)
    allFilms.addMovie("Saving Private Ryan", 8.6, 4)

    allUsers = Users.Users()
    allUsers.addUser("Andrei", "Bondarenko", "andrei.bondarenco@ad.ua.ac.be", 1)
    allUsers.addUser("Bob", "Verbeke", "bob.verbeke@ad.ua.ac.be", 2)
    allUsers.addUser("Igor", "Schittekat", "igor.schittekat@ad.ua.ac.be", 3)
    allUsers.addUser("Robbe", "van Reeth", "robbe.vanreeth@ad.ua.ac.be", 4)

    allPlays = Plays.Plays(allRooms, allFilms)
    allPlays.addPlay(1, 1, "2017-01-20", "The Sting", 1)
    allPlays.addPlay(2, 1, "2017-01-20", "Ice Age", 2)
    allPlays.addPlay(1, 2, "2017-01-21", "The Terminator", 3)
    allPlays.addPlay(2, 2, "2017-01-20", "Ice Age", 4)
    allPlays.addPlay(1, 3, "2017-01-20", "The Terminator", 5)
    allPlays.addPlay(3, 4, "2017-01-20", "Saving Private Ryan", 6)
    allPlays.addPlay(3, 4, "2017-01-21", "Saving Private Ryan", 7)

    allReservations = Reservations.Reservations(allRooms, allUsers, allPlays, allSlots)

    allReservations.createReservation(1, 1, 5)
    allReservations.createReservation(2, 4, 10)
    allReservations.createReservation(3, 6, 1)
    allReservations.createReservation(4, 1, 15)

    room1 = allRooms.retrieveRoom(1)
    room1.enterRoom(1, "2017-01-20", 10)
    room1.enterRoom(1, "2017-01-20", 9)

    log(allFilms, allPlays, "16:30", "2017-01-20", allSlots)

    room1.enterRoom(1, "2017-01-20", 1)
    room2 = allRooms.retrieveRoom(2)
    room2.enterRoom(2, "2017-01-20", 5)

    log(allFilms, allPlays, "17:00", "2017-01-20", allSlots)

    room2.enterRoom(2, "2017-01-20", 5)
    log(allFilms, allPlays, "17:30", "2017-01-20", allSlots)
