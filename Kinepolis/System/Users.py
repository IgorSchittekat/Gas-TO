from System.ADTs.Table import *


class SingleUser:
    def __init__(self, userID, firstName, lastName, mail):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    # def __contains__(self, item):
    #     return (self.userID == item or
    #             self.firstName == item or
    #             self.lastName == item or
    #             self.mail == item)


class Users:
    def __init__(self):
        self.allUsers = Table("hsep", 10, "bst")  # datastructure
        self.totalUsers = 0

    def addUser(self, firstName, lastName, mail, userID):
        newUser = SingleUser(userID, firstName, lastName, mail)
        insertSucces = self.allUsers.insert((userID, newUser))
        if insertSucces:
            self.totalUsers += 1
        return insertSucces

    def getUserInfo(self, userID):
        userExists, userData = self.allUsers.retrieve(userID)
        return userData.firstName, userData.lastName, userData.mail

    def changeUserMail(self, userID, newMail):
        userExists, userInfo = self.allUsers.retrieve(userID)
        if userExists:
            userInfo[1].mail = newMail
            return True
        return False

    def getUsers(self):
        return self.allUsers.traverse()
