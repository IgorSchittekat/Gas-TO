from os import path
class BSTNode:
    def __init__(self, newItem):
        # newItem = (searchKey, content)
        if type(newItem) == tuple:
            try:
                self.key = newItem[0]
                self.content = newItem[1:]
                if len(self.content) == 1:
                    self.content = self.content[0]      # to prevent tuple with 1 element -> just get element
            except:
                #if newItem[1] doesn's exist
                self.content = newItem[0]
        # newItem = (searchKey)
        else:
            self.key = newItem
            self.content = newItem


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def destroySearchTree(self):
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def is_empty(self):
        return self.root is None

    def searchTreeInsert(self, newItem):
        newItem = BSTNode(newItem)
        if self.is_empty():
            self.root = newItem
            return True
        # returnt False wanneer newItem al in de tree zit.
        if self.root.key == newItem.key or type(self.root.key) != type(newItem.key):
            return False
        # Linker deelboom
        elif newItem.key < self.root.key:
            if self.leftChild is None:
                self.leftChild = BinarySearchTree()
            return self.leftChild.searchTreeInsert((newItem.key, newItem.content))
        # Rechter deelboom
        elif newItem.key > self.root.key:
            if self.rightChild is None:
                self.rightChild = BinarySearchTree()
            return self.rightChild.searchTreeInsert((newItem.key, newItem.content))


    def searchTreeDelete(self, searchKey):
        if self.root is None:
            return False
        if self.root.key == searchKey:
            if self.leftChild is None and self.rightChild is None:
                self.root = None
                return True

            if self.leftChild is None and self.rightChild != None:
                self.root = self.rightChild.root
                self.leftChild = self.rightChild.leftChild
                self.rightChild = self.rightChild.rightChild
                return True
            elif self.rightChild is None and self.leftChild != None:
                self.root = self.leftChild.root
                self.rightChild = self.leftChild.rightChild
                self.leftChild = self.leftChild.leftChild
                return True
            else:
                inSucParrent, child = self.inorderSuccessor(self, True)
                if child == "Right":
                    self.root = inSucParrent.rightChild.root
                    self.rightChild = self.rightChild.rightChild
                    return True
                else:
                    self.root = inSucParrent.leftChild.root
                    inSucParrent.leftChild = inSucParrent.leftChild.rightChild
                    return True
        # op zoek naar item in linker deelboom
        elif searchKey < self.root.key:
            if self.leftChild == None:
                return False
            rv = self.leftChild.searchTreeDelete(searchKey)
            if self.leftChild.root == None:
                self.leftChild = None
            return rv
        # op zoek naar item in rechter deelboom
        elif searchKey > self.root.key:
            if self.rightChild == None:
                return False
            rv = self.rightChild.searchTreeDelete(searchKey)
            if self.rightChild.root == None:
                self.rightChild = None
            return rv

    def inorderSuccessor(self, testobject, test):
        if test is True:
            if testobject.rightChild.leftChild is None:
                return testobject, "Right"
            else:
                return self.inorderSuccessor(self.rightChild, False)
        else:
            if testobject.leftChild.leftChild is None:
                return testobject, "Left"
            return self.inorderSuccessor(testobject.leftChild, False)

    def searchTreeRetrieve(self, searchKey):
        if self.root is None:
            return False, None
        if self.root.key == searchKey:
            return True, self.root.content
        elif searchKey < self.root.key:
            if self.leftChild is None:
                return False, None
            return self.leftChild.searchTreeRetrieve(searchKey)
        elif searchKey > self.root.key:
            if self.rightChild is None:
                return False, None
            return self.rightChild.searchTreeRetrieve(searchKey)

    def inorderTraverse(self):
        L = []
        if self.root is None:
            return L
        if self.leftChild is None:
            if self.root.key not in L:
                L.append(self.root.key)
            if self.rightChild is None:
                return L
        else:
            rv = self.leftChild.inorderTraverse()
            for i in rv:
                L.append(i)
        if self.root.key not in L:
            L.append(self.root.key)
        if self.rightChild is None:
            if self.root.key not in L:
                L.append(self.root.key)
            return L
        else:
            rv = self.rightChild.inorderTraverse()
            for i in rv:
                L.append(i)
        return L

    def visualize(self, count=0):
        return self.visRec()[0]

    def visRec(self, count=0):
        code = ""
        if (self.leftChild, self.rightChild) == (None, None):
            return code, count

        for tree in [self.leftChild, self.rightChild]:
            if tree is None:
                code += '\tnone' + str(count) + ' [lable="",style=invis]\n'
                code += '\t"' + str(self.root.key) + '" -> none' + str(count) + ' [style=invis]\n'
                count += 1
            else:
                code += '\t"' + str(self.root.key) + '" -> "' + str(tree.root.key) + '"\n'
                temp, count = tree.visRec(count + 1)
                code += temp

        return code, count


if __name__ == "__main__":
    b = BinarySearchTree()
    #b.searchTreeInsert(20)
    b.searchTreeInsert(10)
    b.searchTreeInsert(5)
    b.searchTreeInsert(9)
    #b.searchTreeInsert(22)
    #b.searchTreeInsert(15)
    #b.searchTreeInsert(1)
    #b.searchTreeInsert(30)
    #b.searchTreeInsert(9)
    #b.searchTreeInsert(12)
    #b.searchTreeInsert(30)
    #b.searchTreeInsert(17)
    #b.searchTreeInsert(13)
    #b.searchTreeInsert(7)
    #b.searchTreeInsert(11)
    #b.searchTreeInsert(19)
    #b.searchTreeInsert(8)
    #b.searchTreeInsert(6)
    #b.searchTreeInsert(5)
    #b.searchTreeInsert(40)
    #b.searchTreeInsert(35)
    #b.searchTreeInsert(3)
    #b.searchTreeInsert(27)
    #b.searchTreeInsert(32)
    #b.searchTreeInsert(39)
    #b.searchTreeInsert(4)
    #b.searchTreeDelete(13)
    #b.searchTreeDelete(17)
    #b.searchTreeDelete(10)





    print(b.visualize())






















