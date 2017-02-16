class Node:
    def __init__(self):

        self.waarde1 = None
        self.waarde2 = None
        self.waarde3 = None
        self.kind1 = None
        self.kind2 = None
        self.kind3 = None
        self.kind4 = None
        self.ouder = None

    def isFull(self):
        if (self.waarde1 is not None and self.waarde2 is not None
            and self.waarde3 is not None):
            return True
        else:
            return False

    def getKinderen(self):
        if self.kind1 is None:
            alleKinderen = []
            return alleKinderen
        elif (self.kind1 is not None and self.kind2 is None):
            alleKinderen = [self.kind1]
            return alleKinderen
        elif (self.kind1 is not None and self.kind2 is not None and self.kind3 is None):
            alleKinderen = [self.kind1, self.kind2]
            return alleKinderen
        elif (self.kind1 is not None and self.kind2 is not None and self.kind3 is not None
         and self.kind4 is None):
            alleKinderen = [self.kind1, self.kind2, self.kind3]
            return alleKinderen
        elif (self.kind1 is not None and self.kind2 is not None and self.kind3 is not None
            and self.kind4 is not None):
            alleKinderen = [self.kind1, self.kind2, self.kind3, self.kind4]
            return alleKinderen

    def getWaarden(self):
        if self.waarde1 is None:
            return None
        elif self.waarde1 is not None and self.waarde2 is None:
            alleWaarden = [self.waarde1]
            return alleWaarden
        elif self.waarde1 is not None and self.waarde2 is not None\
                and self.waarde3 is None:
            alleWaarden = [self.waarde1, self.waarde2]
            return alleWaarden
        elif self.waarde1 is not None and self.waarde2 is not None \
                and self. waarde3 is not None:
            alleWaarden = [self.waarde1, self.waarde2, self.waarde3]
            return alleWaarden

    def sortValues(self):
        if self.waarde1 is None:
            return None
        elif self.waarde1 is not None and self.waarde2 is None:
            return [self.waarde1]
        elif self.waarde2 is not None and self.waarde1 is not None and self.waarde3 is None:
            waarden = [self.waarde1, self.waarde2]
            sortedWaarden = sorted(waarden)
            self.waarde1 = sortedWaarden[0]
            self.waarde2 = sortedWaarden[1]
        elif self.waarde1 is not None and self.waarde2 is not None and self.waarde3 is not None:
            waarden = [self.waarde1, self.waarde2, self.waarde3]
            sortedWaarden = sorted(waarden)
            self.waarde1 = sortedWaarden[0]
            self.waarde2 = sortedWaarden[1]
            self.waarde3 = sortedWaarden[2]

class TwoThreeFourTree(Node):
    def __init__(self):
        #Create an empty 2-3-4 tree
        super().__init__()
        self.root = Node()
        # return self.root

    def destroyTwoThreeFourTree(self):
        #Remove 2-3-4 tree
        self.root = Node()

        return True

    def is_empty(self):
        #Displays whether the tree is empty or not
        if self.getWaarden() == None:
            return True
        elif self.getWaarden() is not None:
            return False

    def isLeaf(self):

        if len(self.getKinderen()) == 0:
            return True
        if len(self.getKinderen()) != 0:
            return False

    def insertItem(self, newItem):

        # Insert in correct place, return True if succeeded
        # newItem should be an integer
        # if self.search(newItem) == True:
        # return False

        if self.isLeaf() is True:

            if self.is_empty() is True:
                self.waarde1 = newItem
                return True
            elif len(self.getWaarden()) == 1:
                if newItem > self.waarde1:
                    self.waarde2 = newItem
                elif newItem < self.waarde1:
                    temp = self.waarde1
                    self.waarde1 = newItem
                    self.waarde2 = temp
                return True
            elif len(self.getWaarden()) == 2:
                self.waarde3 = newItem
                self.sortValues()
                return True
            elif len(self.getWaarden()) == 3:

                if self.ouder == None:

                    self.kind1 = TwoThreeFourTree()
                    self.kind1.waarde1 = self.waarde1
                    self.kind1.ouder = self

                    self.kind2 = TwoThreeFourTree()
                    self.kind2.waarde1 = self.waarde3
                    self.kind2.ouder = self

                    self.waarde1 = self.waarde2
                    self.waarde2 = None
                    self.waarde3 = None
                    self.kind1.ouder.insertItem(newItem)

                elif len(self.ouder.getWaarden()) == 1:

                    if self.waarde2 < self.ouder.waarde1:
                        self.ouder.waarde2 = self.ouder.waarde1
                        self.ouder.waarde1 = self.waarde2

                        self.ouder.kind3 = TwoThreeFourTree()
                        self.ouder.kind3 = self.ouder.kind2
                        self.ouder.kind3.ouder = self.ouder

                        self.ouder.kind1 = TwoThreeFourTree()
                        self.ouder.kind1.waarde1 = self.waarde1

                        self.ouder.kind2 = TwoThreeFourTree()
                        self.ouder.kind2.waarde1 = self.waarde3
                        self.ouder.insertItem(newItem)

                    elif self.waarde2 > self.ouder.waarde1:
                        self.ouder.waarde2 = self.waarde2

                        self.ouder.kind3 = TwoThreeFourTree()
                        self.ouder.kind3.waarde1 = self.waarde3
                        self.ouder.kind3.ouder = self.ouder
                        self.waarde2 = None
                        self.waarde3 = None
                        self.ouder.insertItem(newItem)

                elif len(self.ouder.getWaarden()) == 2:

                    if self.waarde2 < self.ouder.waarde1:

                        self.ouder.waarde3 = self.waarde2
                        self.ouder.sortValues()

                        self.ouder.kind4 = TwoThreeFourTree()
                        self.ouder.kind4 = self.ouder.kind3
                        self.ouder.kind4.ouder = self.ouder

                        self.ouder.kind3 = TwoThreeFourTree()
                        self.ouder.kind3 = self.ouder.kind2
                        self.ouder.kind3.ouder = self.ouder

                        self.ouder.kind2.destroyTwoThreeFourTree()
                        self.ouder.kind2.waarde1 = self.waarde3

                        self.ouder.kind1.destroyTwoThreeFourTree()
                        self.ouder.kind1.waarde1 = self.waarde1
                        self.ouder.kind1.waarde2 = None
                        self.ouder.kind1.waarde3 = None
                        self.ouder.insertItem(newItem)



                    elif self.ouder.waarde1 < self.waarde2 < self.ouder.waarde2:
                        self.ouder.kind4 = TwoThreeFourTree()
                        self.ouder.kind4 = self.ouder.kind3

                        self.ouder.waarde3 = self.waarde2
                        self.ouder.sortValues()

                        self.ouder.kind2.destroyTwoThreeFourTree()
                        self.ouder.kind2.waarde1 = self.waarde1

                        self.ouder.kind3.destroyTwoThreeFourTree()
                        self.ouder.kind3.waarde1 = self.waarde3
                        self.waarde2 = None
                        self.waarde3 = None
                        self.ouder.insertItem(newItem)

                    elif self.ouder.waarde2 < self.waarde2:
                        self.ouder.waarde3 = self.waarde2

                        self.ouder.kind3.destroyTwoThreeFourTree()
                        self.ouder.kind3.waarde1 = self.waarde1

                        self.ouder.kind4 = TwoThreeFourTree()
                        self.ouder.kind4.waarde1 = self.waarde3
                        self.ouder.kind4.ouder = self.ouder
                        self.waarde2 = None
                        self.waarde3 = None
                        self.ouder.insertItem(newItem)

                elif len(self.ouder.getWaarden()) == 3:

                    self.ouder.kind1.kind1 = TwoThreeFourTree()
                    self.ouder.kind1.kind1.ouder = self.ouder.kind1
                    self.ouder.kind1.kind1.waarde1 = self.ouder.kind1.waarde1
                    self.ouder.kind1.kind1.waarde2 = self.ouder.kind1.waarde2
                    self.ouder.kind1.kind1.waarde3 = self.ouder.kind1.waarde3
                    self.ouder.kind1.waarde1 = self.ouder.waarde1
                    self.ouder.kind1.waarde2 = None
                    self.ouder.kind1.waarde3 = None

                    self.ouder.kind1.kind2 = TwoThreeFourTree()
                    self.ouder.kind1.kind2.waarde1 = self.ouder.kind2.waarde1
                    self.ouder.kind1.kind2.waarde2 = self.ouder.kind2.waarde2
                    self.ouder.kind1.kind2.waarde3 = self.ouder.kind2.waarde3
                    self.ouder.kind1.kind2.ouder = self.ouder.kind1

                    self.ouder.kind2.kind1 = TwoThreeFourTree()
                    self.ouder.kind2.kind1 = self.ouder.kind3
                    self.ouder.kind2.kind1.ouder = self.ouder.kind2

                    self.ouder.kind2.kind2 = TwoThreeFourTree()
                    self.ouder.kind2.kind2 = self.ouder.kind4
                    self.ouder.kind2.kind2.ouder = self.ouder.kind2

                    self.ouder.waarde1 = self.ouder.ouder.waarde3
                    self.ouder.waarde2 = None
                    self.ouder.waarde3 = None
                    self.ouder.ouder.kind3 = None
                    self.ouder.ouder.kind4 = None

                    self.ouder.ouder.waarde1 = self.ouder.ouder.waarde2
                    self.ouder.ouder.waarde2 = None
                    self.ouder.ouder.waarde3 = None
                    self.ouder.ouder.insertItem(newItem)
                    #Insert newItem in newtree

        elif self.isLeaf() is False:

            if len(self.getWaarden()) == 1:

                if self.waarde1 < newItem:

                    self.kind2.insertItem(newItem)
                elif self.waarde1 > newItem:
                    self.kind1.insertItem(newItem)

            elif len(self.getWaarden()) == 2:

                if self.waarde1 > newItem:
                    self.kind1.insertItem(newItem)
                elif self.waarde1 < newItem < self.waarde2:
                    self.kind2.insertItem(newItem)
                elif self.waarde2 < newItem:
                    self.kind3.insertItem(newItem)

            elif len(self.getWaarden()) == 3:
                if newItem < self.waarde1:
                    self.kind1.insertItem(newItem)
                elif self.waarde1 < newItem < self.waarde2:
                    self.kind2.insertItem(newItem)
                elif self.waarde2 < newItem < self.waarde3:
                    self.kind3.insertItem(newItem)
                elif self.waarde3 < newItem:
                    self.kind4.insertItem(newItem)
        return False

    def deleteItem(self, x):

        if self.isLeaf() is True:
            print('test')
            print(self.getKinderen())
            if self.getKinderen() == []:

                if len(self.getWaarden()) == 1:

                    if self.waarde1 == x:
                        self.waarde1 = None

                elif len(self.getWaarden()) == 2:
                    if self.waarde1 == x:
                        self.waarde1 = self.waarde2
                        self.waarde2 = None
                        return True
                    elif self.waarde2 == x:
                        self.waarde2 = None
                        return True

                elif len(self.getWaarden()) == 3:
                    if self.waarde1 == x:
                        self.waarde1 = self.waarde2
                        self.waarde2 = self.waarde3
                        self.waarde3 = None
                        return True

                    elif self.waarde2 == x:
                        self.waarde2 = self.waarde3
                        self.waarde3 = None
                        return True

                    elif self.waarde3 == x:
                        self.waarde3 = None
                        return True


        elif self.getKinderen() != []:

#Waarde zit in de 'parent' node
            if len(self.getWaarden()) == 1 and self.waarde1 == x:

                if len(self.kind1.getWaarden()) == 1:
                    if len(self.kind2.getWaarden()) == 2:
                        self.waarde1 = self.kind1.waarde1
                        self.waarde2 = self.kind2.waarde1
                        self.waarde3 = self.kind2.waarde2
                        self.kind1 = None
                        self.kind2 = None

                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde1 = self.kind2.waarde1
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = self.kind2.waarde3

                elif len(self.kind2.getWaarden()) == 1:
                    if len(self.kind1.getWaarden()) == 2:
                        self.waarde1 = self.kind1.waarde1
                        self.waarde2 = self.kind1.waarde2
                        self.waarde3 = self.kind2.waarde1
                        self.kind1 = None
                        self.kind2 = None
                    elif len(self.kind1.getWaarden()) == 3:
                        self.waarde1 = self.kind1.waarde3
                        self.kind1.waarde3 = None
                elif len(self.kind1.getWaarden()) >= 2 and len(
                        self.kind2.getWaarden()) >= 2:

                    self.waarde1 = self.kind2.waarde1
                    self.kind2.waarde1 = self.kind2.waarde2
                    self.kind2.waarde2 = self.kind2.waarde3
                    self.kind2.waarde3 = None

            elif len(self.getWaarden()) == 1 and self.waarde1 != x:
                if x > self.waarde1:
                    if len(self.kind2.getWaarden()) == 1:
                        if self.kind2.waarde1 == x:

                            if len(self.kind1.getWaarden()) == 2:
                                self.waarde3 = self.waarde1
                                self.waarde2 = self.kind1.waarde2
                                self.waarde1 = self.kind1.waarde1
                                self.kind1 = None
                                self.kind2 = None

                            elif len(self.kind1.getWaarden()) == 3:
                                self.kind2.waarde1 = self.waarde1
                                self.waarde1 = self.kind1.waarde3
                                self.kind1.waarde3 = None

                        elif self.kind1.waarde1 == x:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif self.kind1.waarde2 == x:
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif self.kind1.waarde3 == x:
                            self.kind1.waarde3 = None

                    elif len(self.kind2.getWaarden()) == 2:
                        if self.kind2.waarde1 == x:
                            self.kind2.waarde1 = self.kind2.waarde2
                            self.kind2.waarde2 = None
                        elif self.kind2.waarde2 ==x:
                            self.kind2.waarde2 = None

                    elif len(self.kind2.getWaarden()) ==3:
                        if self.kind2.waarde1 == x:
                            self.kind2.waarde1 = self.kind2.waarde2
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None

                        elif self.kind2.waarde2 == x:
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None

                        elif self.kind2.waarde3 == x:
                            self.kind2.waarde3 = None

                if x < self.waarde1:
                    if len(self.kind1.getWaarden()) == 1:
                        if self.kind1.waarde1 == x:

                            if len(self.kind2.getWaarden()) == 2:
                                self.waarde2 = self.kind2.waarde1
                                self.waarde3 = self.kind2.waarde2
                                self.kind1 = None
                                self.kind2 = None

                            elif len(self.kind2.getWaarden()) == 3:
                                self.kind1.waarde1 = self.waarde1
                                self.waarde1 = self.kind2.waarde1
                                self.kind2.waarde1 = self.kind2.waarde2
                                self.kind2.waarde2 = self.kind2.waarde3
                                self.kind2.waarde3 = None

                    elif len(self.kind1.getWaarden()) == 2:
                        if self.kind1.waarde1 == x:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = None
                        elif self.kind2.waarde2 == x:
                            self.kind2.waarde2 = None

                    elif len(self.kind1.getWaarden()) == 3:
                        if self.kind1.waarde1 == x:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None

                        elif self.kind1.waarde2 == x:
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None

                        elif self.kind1.waarde3 == x:
                            self.kind1.waarde3 = None

            elif len(self.getWaarden()) == 2:
                if x == self.waarde1:
                    if len(self.kind1.getWaarden()) == 1 and \
                       len(self.kind2.getWaarden()) == 1:
                        self.waarde1 = self.waarde2
                        self.waarde2 = None
                        self.kind1.waarde2 = self.kind2.waarde1
                        self.kind2 = self.kind3
                        self.kind3 = None
                    elif len(self.kind1.getWaarden()) == 2:
                        self.waarde1 = self.kind1.waarde2
                        self.kind1.waarde2 = None

                    elif len(self.kind1.getWaarden()) == 3:
                        self.waarde1 = self.kind1.waarde3
                        self.kind1.waarde3 = None

                    elif len(self.kind2.getWaarden()) == 2:
                        self.waarde1 = self.kind2.waarde1
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = None

                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde1 = self.kind2.waarde1
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = self.kind2.waarde3
                        self.kind2.waarde3 = None

                elif x == self.waarde2:
                    if len(self.kind2.getWaarden()) == 1 and \
                        len(self.kind3.getWaarden()) == 1:
                        self.waarde2 = None
                        self.kind2.waarde2 = self.kind3.waarde1
                        self.kind3 = None
                    elif len(self.kind2.getWaarden()) == 2:
                        self.waarde2 = self.kind2.waarde2
                        self.kind2.waarde2 = None

                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde2 = self.kind2.waarde3
                        self.kind2.waarde3 = None

                    elif len(self.kind3.getWaarden()) == 2:
                        self.waarde2 = self.kind3.waarde1
                        self.kind3.waarde1 = self.kind3.waarde2
                        self.kind3.waarde2 = None

                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde2 = self.kind3.waarde1
                        self.kind3.waarde1 = self.kind3.waarde2
                        self.kind3.waarde2 = self.kind3.waarde3
                        self.kind3.waarde3 = None

                elif x < self.waarde1:

                    if len(self.kind1.getWaarden()) == 1:
                        if x == self.kind1.waarde1:

                            self.kind1.waarde1 = self.waarde1
                            self.kind1.waarde2 = self.kind2.waarde1
                            self.kind2 = self.kind3
                            self.kind3 = None
                            self.waarde1 = self.waarde2
                            self.waarde2 = None

                    elif len(self.kind1.getWaarden()) == 2:
                        if x == self.kind1.waarde1:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = None
                        elif x == self.kind1.waarde2:
                            self.kind1.waarde2 = None


                    elif len(self.kind1.getWaarden()) == 3:

                        if x == self.kind1.waarde1:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif x == self.kind1.waarde2:

                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif x == self.kind1.waarde3:
                            self.kind1.waarde3 = None

                elif self.waarde1 < x < self.waarde2:
                    if len(self.kind2.getWaarden()) == 1 and \
                        x == self.kind2.waarde1:
                        if len(self.kind1.getWaarden()) == 1 and \
                            len(self.kind3.getWaarden()) == 1:
                            self.kind1.waarde2 = self.waarde1
                            self.waarde1 = self.waarde2
                            self.waarde2 = None
                            self.kind2 = self.kind3
                            self.kind3 = None
                        elif len(self.kind1.getWaarden()) ==2:
                            self.kind2.waarde1 = self.waarde1
                            self.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = None

                        elif len(self.kind1.getWaarden()) == 3:
                            self.kind2.waarde1 = self.waarde1
                            self.waarde1 = self.kind1.waarde3
                            self.kind1.waarde3 = None

                        elif len(self.kind3.getWaarden()) == 2:
                            self.kind2.waarde1 = self.waarde2
                            self.waarde2 = self.kind3.waarde1
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = None
                        elif len(self.kind3.getWaarden()) == 3:
                            self.kind2.waarde1 = self.kind3.waarde1
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None

                    elif len(self.kind2.getWaarden()) == 2 and \
                        x == self.kind2.waarde1:
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = None
                    elif len(self.kind2.getWaarden()) == 2 and \
                        x == self.kind2.waarde2:
                        self.kind2.waarde2 = None
                    elif len(self.kind2.getWaarden()) == 3:
                        if x == self.kind2.waarde1:
                            self.kind2.waarde1 = self.kind2.waarde2
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                        elif x == self.kind2.waarde2:
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                        elif x == self.kind2.waarde3:
                            self.kind2.waarde3 = None

                elif x > self.waarde2:
                    if len(self.kind3.getWaarden()) == 1:
                        if len(self.kind2.getWaarden()) == 1:
                            self.kind2.waarde2 = self.waarde2
                            self.kind3 = None
                            self.waarde2 = None
                        elif len(self.kind2.getWaarden()) == 2:
                            self.kind3.waarde1 = self.waarde2
                            self.waarde2 = self.kind2.waarde2
                            self.kind2.waarde2 = None
                        elif len(self.kind2.getWaarden()) == 3:
                            self.kind3.waarde1 = self.waarde2
                            self.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                    elif len(self.kind3.getWaarden()) == 2:
                        if x == self.kind3.waarde1:
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = None
                        elif x == self.kind3.waarde2:
                            self.kind3.waarde2 = None

                    elif len(self.kind3.getWaarden()) == 3:
                        if x == self.kind3.waarde1:
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None
                        elif x == self.kind3.waarde2:
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None
                        elif x == self.kind3.waarde3:
                            self.kind3.waarde3 = None

            elif len(self.getWaarden()) == 3:
                if x == self.waarde1:
                    if len(self.kind1.getWaarden()) == 1 and \
                        len(self.kind2.getWaarden()) ==1:
                        self.waarde1 = self.waarde2
                        self.waarde2 = self.waarde3
                        self.waarde3 = None
                        self.kind1.waarde2 = self.kind2.waarde1
                        self.kind2 = self.kind3
                        self.kind3 = self.kind4
                    elif len(self.kind1.getWaarden()) == 2:
                        self.waarde1 = self.kind1.waarde2
                        self.kind1.waarde2 = None
                    elif len(self.kind1.getWaarden()) ==3:
                        self.waarde1 = self.kind1.waarde3
                        self.kind1.waarde3 = None
                    elif len(self.kind2.getWaarden()) == 2:
                        self.waarde1 = self.kind2.waarde1
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = None
                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde1 = self.kind2.waarde1
                        self.kind2.waarde1 = self.kind2.waarde2
                        self.kind2.waarde2 = self.kind2.waarde3
                        self.kind2.waarde3 = None

                elif x == self.waarde2:
                    if len(self.kind2.getWaarden()) == 1 and \
                        len(self.kind3.getWaarden()) == 1:
                        self.waarde2 = self.waarde3
                        self.waarde3 = None
                        self.kind2.waarde2 = self.kind3.waarde1
                        self.kind3 = self.kind4
                        self.kind4 = None
                    elif len(self.kind2.getWaarden()) == 2:
                        self.waarde2 = self.kind2.waarde2
                        self.kind2.waarde2 = None
                    elif len(self.kind2.getWaarden()) == 3:
                        self.waarde2 = self.kind2.waarde3
                        self.kind2.waarde3 = None
                    elif len(self.kind3.getWaarden()) == 2:
                        self.waarde2 = self.kind3.waarde1
                        self.kind3.waarde1 = self.kind3.waarde2
                        self.kind3.waarde2 = None
                    elif len(self.kind3.getWaarden()) == 3:
                        self.waarde2 = self.kind3.waarde1
                        self.kind3.waarde1 = self.kind3.waarde2
                        self.kind3.waarde2 = self.kind3.waarde3
                        self.kind3.waarde3 = None
                elif x == self.waarde3:
                    if len(self.kind3.getWaarden()) == 1 and \
                        len(self.kind4.getWaarden()) ==1:
                        self.kind3.waarde2 = self.kind4.waarde1
                        self.kind4 = None
                        self.waarde3 = None
                    elif len(self.kind3.getWaarden()) == 2:
                        self.waarde3 = self.kind3.waarde2
                        self.kind3.waarde2 = None
                    elif len(self.kind3.getWaarden()) == 3:
                        self.waarde3 = self.kind3.waarde3
                        self.kind3.waarde3 = None

                    elif len(self.kind4.getWaarden()) == 2:
                        self.waarde3 = self.kind4.waarde1
                        self.kind4.waarde1 = self.kind4.waarde2
                        self.kind4.waarde2 = None
                    elif len(self.kind4.getWaarden()) == 3:
                        self.waarde3 = self.kind4.waarde1
                        self.kind4.waarde1 = self.kind4.waarde2
                        self.kind4.waarde2 = self.kind4.waarde3
                        self.kind4.waarde3 = None
                elif x < self.waarde1:

                    if len(self.kind1.getWaarden()) == 1 and \
                        len(self.kind2.getWaarden()) ==1:
                        if x == self.kind1.waarde1:
                            self.kind1.waarde1 = self.waarde1
                            self.kind1.waarde2 = self.kind2.waarde1
                            self.kind2 = self.kind3
                            self.kind3 = self.kind4
                            self.kind4 = None
                            self.waarde1 = self.waarde2
                            self.waarde2 = self.waarde3
                            self.waarde3 = None
                    elif len(self.kind1.getWaarden()) == 2:
                        if x == self.kind1.waarde1:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = None
                        elif x == self.kind1.waarde2:
                            self.kind1.waarde2 = None
                    elif len(self.kind1.getWaarden()) == 3:
                        if x == self.kind1.waarde1:
                            self.kind1.waarde1 = self.kind1.waarde2
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif x == self.kind1.waarde2:
                            self.kind1.waarde2 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif x == self.kind1.waarde3:
                            self.kind1.waarde3 = None

                elif self.waarde1 < x < self.waarde2:

                    if len(self.kind2.getWaarden()) == 1:
                        if len(self.kind3.getWaarden()) == 1 and \
                        len(self.kind1.getWaarden()) == 1:
                            if x== self.kind2.waarde1:
                                self.kind1.waarde2 = self.waarde1
                                self.waarde1 = self.waarde2
                                self.waarde2 = self.waarde3
                                self.waarde3 = None
                                self.kind2 = self.kind3
                                self.kind3 = self.kind4
                                self.kind4 = None
                        elif len(self.kind1.getWaarden()) == 2:
                            self.kind2.waarde1 = self.waarde1
                            self.waarde1 = self.kind1.waarde2
                        elif len(self.kind1.getWaarden())==3:
                            self.kind2.waarde1 = self.waarde1
                            self.waarde1 = self.kind1.waarde3
                            self.kind1.waarde3 = None
                        elif len(self.kind3.getWaarden())== 2:
                            self.kind2.waarde1 = self.waarde2
                            self.waarde2 = self.kind3.waarde1
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = None
                        elif len(self.kind3.getWaarden()) == 3:
                            self.kind2.waarde1 = self.waarde2
                            self.waarde2 = self.kind3.waarde1
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None


                    elif len (self.kind2.getWaarden()) == 2:
                        if x == self.kind2.waarde1:
                            self.kind2.waarde1 = self.kind2.waarde2
                            self.kind2.waarde2 = None
                        elif x == self.kind2.waarde2:
                            self.kind2.waarde2 = None
                    elif len(self.kind2.getWaarden()) == 3:
                        if x == self.kind2.waarde1:
                            self.kind2.waarde1 = self.kind2.waarde2
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                        elif x == self.kind2.waarde2:
                            self.kind2.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                        elif x == self.kind2.waarde3:
                            self.kind2.waarde3 = None


                elif self.waarde2 < x < self.waarde3:

                    if len(self.kind2.getWaarden()) == 1:
                        if len(self.kind4.getWaarden()) == 1 and \
                                    len(self.kind3.getWaarden()) == 1:
                            if x == self.kind3.waarde1:
                                self.kind2.waarde2 = self.waarde2
                                self.waarde2 = self.waarde3
                                self.waarde3 = self.waarde4
                                self.waarde4 = None
                                self.kind3 = self.kind4
                                self.kind4 = None
                        elif len(self.kind2.getWaarden()) == 2:
                            self.kind3.waarde1 = self.waarde2
                            self.waarde2 = self.kind3.waarde2
                        elif len(self.kind2.getWaarden()) == 3:
                            self.kind3.waarde1 = self.waarde2
                            self.waarde2 = self.kind2.waarde3
                            self.kind2.waarde3 = None
                        elif len(self.kind4.getWaarden())== 2:
                            self.kind3.waarde1 = self.waarde3
                            self.waarde3 = self.kind4.waarde1
                            self.kind4.waarde1 = self.kind4.waarde2
                            self.kind4.waarde2 = None
                        elif len(self.kind4.getWaarden()) == 3:
                            self.kind3.waarde1 = self.waarde3
                            self.waarde3 = self.kind4.waarde1
                            self.kind4.waarde1 = self.kind4.waarde2
                            self.kind4.waarde2 = self.kind4.waarde3
                            self.kind4.waarde3 = None

                    elif len(self.kind3.getWaarden()) == 2:
                        if x == self.kind3.waarde1:
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = None
                        elif x == self.kind3.waarde2:
                            self.kind3.waarde2 = None
                    elif len(self.kind3.getWaarden()) == 3:
                        if x == self.kind3.waarde1:
                            self.kind3.waarde1 = self.kind3.waarde2
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None
                        elif x == self.kind3.waarde2:
                            self.kind3.waarde2 = self.kind3.waarde3
                            self.kind3.waarde3 = None
                        elif x == self.kind3.waarde3:
                            self.kind3.waarde3 = None

                elif x > self.waarde3:
                    if len(self.kind3.getWaarden()) == 1 and \
                        len(self.kind4.getWaarden()) == 1:
                        if x == self.kind4.waarde1:
                            self.kind3.waarde2 = self.waarde3
                            self.waarde3 = None
                            self.kind4 = None
                    elif len(self.kind4.getWaarden()) == 1 and \
                        len(self.kind3.getWaarden()) == 2:
                        self.kind4.waarde1 = self.waarde3
                        self.waarde3 = self.kind3.waarde2
                        self.kind3.waarde2 = None
                    elif len(self.kind4.getWaarden()) == 1 and \
                        len(self.kind3.getWaarden()) == 3:
                        self.kind4.waarde1 = self.waarde3
                        self.waarde3 = self.kind3.waarde3
                        self.kind3.waarde3 = None
                    elif len(self.kind4.getWaarden()) == 2:
                        if x == self.kind4.waarde1:
                            self.kind4.waarde1 = self.kind4.waarde2
                            self.kind4.waarde2 = None

                        elif x == self.kind4.waarde2:
                            self.kind4.waarde2 = None
                    elif len(self.kind4.getWaarden()) == 3:
                        if x == self.kind4.waarde1:
                            self.kind4.waarde1 = self.kind4.waarde2
                            self.kind4.waarde2 = self.kind4.waarde3
                            self.kind4.waarde3 = None
                        elif x == self.kind4.waarde2:
                            self.kind4.waarde2 = self.kind4.waarde3
                            self.kind4.waarde3 = None
                        elif x == self.kind4.waarde3:
                            self.kind4.waarde3 = None
        return False

    def visualize(self):
        pass

    def inorder_traverse(self):
        pass
    def retrieve(self, searchKey):
        #Search for key in the 234 tree
        #node has 1 element:
        if len(self.getWaarden()) == 1:
            if self.isLeaf() == True:
                if searchKey == self.waarde1:
                    return (True, self.waarde1)
                elif searchKey != self.waarde1:
                    return False
            elif self.isLeaf() == False:
                if searchKey == self.waarde1:
                    return (True, self.waarde1)
                elif searchKey < self.waarde1:
                    return self.kind1.retrieve(searchKey)
                elif searchKey > self.waarde1:
                    return self.kind2.retrieve(searchKey)
        elif len(self.getWaarden()) == 2:

            if self.isLeaf() == True:
                if searchKey == self.waarde1 :
                    return (True, self.waarde1)
                elif searchKey == self.waarde2:
                    return (True, self.waarde2)
                elif searchKey != self.waarde1 and searchKey != self.waarde2:
                    return False
            elif self.isLeaf() == False:

                if searchKey == self.waarde1:
                    return (True, self.waarde1)
                elif  searchKey == self.waarde2:
                    return (True, self.waarde2)
                elif searchKey < self.waarde1:
                    return self.kind1.retrieve(searchKey)
                elif self.waarde1 < searchKey < self.waarde2:
                    return self.kind2.retrieve(searchKey)
                elif searchKey > self.waarde2:
                    return self.kind3.retrieve(searchKey)
        elif len(self.getWaarden()) == 3:
            if self.isLeaf() == True:
                if searchKey == self.waarde1:
                    return (True, self.waarde1)
                elif searchKey == self.waarde2:
                    return (True, self.waarde2)
                elif searchKey == self.waarde3:
                    return (True, self.waarde3)
                elif searchKey != self.waarde1 and \
                    searchKey != self.waarde2 and searchKey != self.waarde3:
                    return False

            elif self.isLeaf() == False:
                if searchKey == self.waarde1:
                    return (True, self.waarde1)
                elif searchKey == self.waarde2:
                    return (True, self.waarde2)
                elif searchKey == self.waarde3:
                    return (True, self.waarde3)
                elif searchKey < self.waarde1:
                    return self.kind1.retrieve(searchKey)
                elif self.waarde1 < searchKey < self.waarde2:
                    return self.kind2.retrieve(searchKey)
                elif self.waarde2 < searchKey < self.waarde3:
                    return self.kind3.retrieve(searchKey)
                elif searchKey > self.waarde3:
                    return self.kind4.retrieve(searchKey)
        return False
if __name__ == "__main__":
    P = TwoThreeFourTree()
    P.insertItem(30)
    P.insertItem(40)
    P.insertItem(35)
    print(P.inorder_traverse())
    P.insertItem(80)
    P.insertItem(20)
    P.insertItem(10)
    P.insertItem(45)
    P.insertItem(120)
    P.insertItem(150)
    P.insertItem(135)
    P.insertItem(60)
    P.insertItem(110)
    P.insertItem(140)
    P.insertItem(160)
    P.insertItem(15)
    P.insertItem(102)
    P.insertItem(5)
    P.insertItem(42)
    P.insertItem(44)
    P.insertItem(33)
    P.insertItem(32)
    P.insertItem(41)
    print(P.retrieve(5))
    print(P.retrieve(42))
    print(P.retrieve(500))
    # print(P.inorderTraverse())
    # P.deleteItem(100)
    #print(P.retrieve(80))
    print('                              ', P.getWaarden())
    print('         ', P.kind1.getWaarden(),'                  ',  P.kind2.getWaarden())
    print(P.kind1.kind1.getWaarden(), P.kind1.kind2.getWaarden(),P.kind1.kind3.getWaarden(),  '  ', P.kind2.kind1.getWaarden() , P.kind2.kind2.getWaarden(), P.kind2.kind3.getWaarden(), P.kind2.kind4.getWaarden())


    #print(P.kind1.getWaarden())
    #print(P.kind2.getWaarden())