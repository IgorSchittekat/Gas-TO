from System.ADTs.LinkedList import *
from System.ADTs.CircLinkedList import *
from System.ADTs.DoubleLinkedList import *
from System.ADTs.BinarySearchTree import *
from System.ADTs.TwoThreeFourTree import *
from System.ADTs.TwoThreeTree import *
from System.ADTs.RedBlackTree import *

class hashTableNode:
    def __init__(self, newItem):
        # newItem = (searchKey, Content)
        if type(newItem) == tuple:
            try:
                self.key = newItem[0]
                self.content = newItem[1:]
                if len(self.content) == 1:
                    self.content = self.content[0]      #to provent tuple with 1 element -> just get element
            except:
                #if newItem[1] doesn's exist
                self.content = newItem[0]

        # newItem = (searchKey)
        else:
            self.key = newItem
            self.content = newItem


class HashTable:

    def __init__(self, size=100, method="hlin", chain="bst"):
        # Fail conditions (size<0, invalid method, invalid chain:
        if size < 0:
            self.size = 0
        else:
            self.size = size
        if method not in ["hlin", "hquad", "hsep"]:
            self.method = "hlin"
        else:
            self.method = method
        if chain not in ["ll", "dll", "cll", "bst", "23", "234", "rb"]:
            self.chain = "bst"
        else:
            self.chain = chain

        # Fill all slots of the hashTable with None
        self.hashTable = []
        for i in range(self.size):
            self.hashTable.append(None)

    def destroyHashTable(self):
        self.hashTable = []
        self.size = 0
        return True

    def is_empty(self):
        # if all slots are None/Deleted -> hashTable is empty
        for i in self.hashTable:
            if i not in [None, "Deleted"]:
                return False
        return True

    def tableInsert(self, newItem):
        newItemNode = hashTableNode(newItem)
        # insert_index is index where NewItem gets inserted
        # start_index is index where the HashTable points first
        insert_index = start_index = int(newItemNode.key) % int(self.size)
        self.offset = 0   # offset from the start_index (used for hlin and hquad to find the next free slot)

        # insert in the right chain (hsep only)
        if self.method == "hsep":
            return self.insertSC(newItemNode, insert_index)

        # Check for a free slot in the Hashtable (hlin and hquad only)
        while (self.hashTable[insert_index] is not None and
                       self.hashTable[insert_index] != "Deleted"):
            if self.hashTable[insert_index].key == newItemNode.key:   # To prevent duplicates
                return False
            insert_index = self.searchNext(start_index) % self.size     # change insert_index to next possible slot
            if insert_index == start_index:       # To prevent infinite loop
                return False

        # If free slot is found
        self.hashTable[insert_index] = newItemNode      # insert newItem
        return True

    def tableDelete(self, searchKey):
        delete_index = start_index = searchKey % self.size      # Same use as insert
        self.offset = 0

        # Delete from the right chain (hsep only)
        if self.method == "hsep":
            return self.deleteSC(searchKey, delete_index)

        # do While loop to check if the item is in the map (and delete it)(hlin and hquad only)
        while True:
            if self.hashTable[delete_index] is None:    # Stop searching by empty slot
                return False
            # if searchKey is found, delete the item -> slot becomes "Deleted"
            if (self.hashTable[delete_index] != "Deleted" and
                        self.hashTable[delete_index].key == searchKey):
                self.hashTable[delete_index] = "Deleted"
                return True
            delete_index = self.searchNext(start_index) % self.size     # change delete_index to next possible slot
            if delete_index == start_index:     # To prevent infinite loop
                return False

    def tableRetrieve(self, searchKey):
        # Allmost the same code as the Delete, only it retrieves the value instead of deleting it
        retrieve_index = start_index = searchKey % self.size
        self.offset = 0

        if self.method == "hsep":
            return self.retrieveSC(searchKey, retrieve_index)

        while True:
            if self.hashTable[retrieve_index] is None:
                return False, None
            if (self.hashTable[retrieve_index] != "Deleted" and         # "Deleted" does not have a key
                    self.hashTable[retrieve_index].key == searchKey):
                return True, self.hashTable[retrieve_index].content
            retrieve_index = self.searchNext(start_index) % self.size
            if retrieve_index == start_index:
                return False, None

    def searchNext(self, index):
        # Find the right spot to insert/delete/retrieve an item (hlin and hquad only)
        if self.method == "hlin":
            self.offset += 1
            return index + self.offset
        elif self.method == "hquad":
            self.offset += 1
            return index + (self.offset ** 2)

    def insertSC(self, newItem, insert_index):
        # Insert an item in the right ADT (hsep only)
        if self.chain == "ll":
            if self.hashTable[insert_index] is None:        # Cant be "Deleted" couse that's hlin and hquad only
                self.hashTable[insert_index] = LinkedList()     # create new ADT
            return self.hashTable[insert_index].addChain((newItem.key, newItem.content))    # Insert in ADT
        elif self.chain == "dll":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = DoubleLinkedList()
            return self.hashTable[insert_index].addChain((newItem.key, newItem.content))
        elif self.chain == "cll":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = CircLinkedList()
            return self.hashTable[insert_index].addChain((newItem.key, newItem.content))
        elif self.chain == "bst":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = BinarySearchTree()
            return self.hashTable[insert_index].searchTreeInsert((newItem.key, newItem.content))
        elif self.chain == "23":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = TwoThreeTree()
            return self.hashTable[insert_index].insert((newItem.key, newItem.content))
        elif self.chain == "234":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = TwoThreeFourTree()
            return self.hashTable[insert_index].insertItem((newItem.key, newItem.content))
        elif self.chain == "rb":
            if self.hashTable[insert_index] is None:
                self.hashTable[insert_index] = RedBlackTree()
            return self.hashTable[insert_index].insert((newItem.key, newItem.content))

    def deleteSC(self, searchKey, delete_index):
        # Delete an item from the right ADT (hsep only)
        if self.hashTable[delete_index] is None:    # Fail condition
            return False
        if self.chain == "ll":
            returnValue = self.hashTable[delete_index].removeChain(searchKey)   # Delete from ADT
        elif self.chain == "dll":
            returnValue = self.hashTable[delete_index].removeChain(searchKey)
        elif self.chain == "cll":
            returnValue = self.hashTable[delete_index].removeChain(searchKey)
        elif self.chain == "bst":
            returnValue = self.hashTable[delete_index].searchTreeDelete(searchKey)
        elif self.chain == "23":
            returnValue = self.hashTable[delete_index].delete(searchKey)
        elif self.chain == "234":
            returnValue = self.hashTable[delete_index].deleteItem(searchKey)
        elif self.chain == "rb":
            returnValue = self.hashTable[delete_index].delete(searchKey)
        # slot becomes None again if the ADT is empty
        if self.hashTable[delete_index].is_empty():
            self.hashTable[delete_index] = None
        return returnValue

    def retrieveSC(self, searchKey, retrieve_index):
        # Retrieve the item from the right ADT (hsep only)
        if self.hashTable[retrieve_index] is None:      # Fail condition
            return False, None
        if self.chain == "ll":
            return self.hashTable[retrieve_index].returnChain(searchKey)        # Retrieve from ADT
        elif self.chain == "dll":
            return self.hashTable[retrieve_index].returnChain(searchKey)
        elif self.chain == "cll":
            return self.hashTable[retrieve_index].returnChain(searchKey)
        elif self.chain == "bst":
            return self.hashTable[retrieve_index].searchTreeRetrieve(searchKey)
        elif self.chain == "23":
            return self.hashTable[retrieve_index].retrieve(searchKey)
        elif self.chain == "234":
            return self.hashTable[retrieve_index].retrieve(searchKey)
        elif self.chain == "rb":
            return self.hashTable[retrieve_index].retrieve(searchKey)

    def changeMethod(self, newMethod):
        # Methods are: {hlin(Lineair Probing), hquad(Quad.ratic Probing, hsep(Seperate Chaining)}
        # Fail conditions: Chainges only possible when HashTable is empty and valid method is given
        if not self.is_empty():
            return False
        if newMethod not in ["hlin", "hquad", "hsep"]:
            return False
        self.method = newMethod
        return True

    def changeChain(self, newChain):
        # Chains are: {ll(LinkedList), dll(DoubleLinkedList), cll(CircLinkedList), bst(BinartSearchTree),
        # 23(TwoThreeTree), 234(TwoThreeFourTree), rb(RedBlackTree)}
        # Fail conditions: Chainges only possible when HashTable is empty and valid chain is given
        if not self.is_empty():
            return False
        if newChain not in ["ll", "dll", "cll", "bst", "23", "234", "rb"]:
            return False
        self.chain = newChain
        return True

    def traverse(self):
        # The traverse of the HashTable is not in order
        L = []
        for i in range(self.size):
            if i not in [None, "Deleted"]:
                if self.method in ["hlin", "hquad"]:
                    L.append(self.hashTable[i].key)     # append elements to list
                elif self.chain in ["bst", "234"]:
                    L.extend(self.hashTable[i].inorderTraverse())   # append all elements at index to list
                elif self.chain in ["ll", "dll", "cll"]:
                    L.extend(self.hashTable[i].traverse())
                elif self.chain in ["23", "rb"]:
                    L.extend(self.hashTable[i].inorder_traverse())
        return sorted(L)

    def visualize(self):
        code = "\tnode [shape=record];\n"
        # create the code for the HashTable (hlin and hquad only)
        if self.method in ["hlin", "hquad"]:
            code += '\tstruct [label="'
            # Get all the values from the table
            for i in range(len(self.hashTable)):
                if i != 0:
                    code += "|"
                if self.hashTable[i] is not None and self.hashTable[i] != "Deleted":
                    code += str(self.hashTable[i].key)      # Get keyvalue
            code += '"];\n' \
                    '\trankdir=LR\n'

        # create the code for the HashTable (hsep only)
        elif self.method == "hsep":
            code += '\tstruct [label="'
            for i in range(self.size):
                if i != 0:
                    code += "|"
                if self.hashTable[i] is not None:
                    code += "<f" + str(i) + ">"
            code += '"];\n'

            if self.chain == "bst":
                code += "\tnode [shape=oval]\n"
                for i in range(len(self.hashTable)):
                    if self.hashTable[i] is None:
                        continue
                    code += self.hashTable[i].visualize()
                    code += "\tstruct:f" + str(i) + ' -> "' + str(self.hashTable[i].root.key) + '"\n'
            elif self.chain in ["ll", "cll", "dll"]:
                code += "\trankdir=LR\n"
                for i in range(len(self.hashTable)):
                    if self.hashTable[i] is None:
                        continue
                    code += self.hashTable[i].visualize()
                    code += "\tstruct:f" + str(i) + ' -> "' + str(self.hashTable[i].front.key) + '"\n'
            elif self.chain == "23":
                code += "\tnode [shape=oval]\n"
                for i in range(len(self.hashTable)):
                    if self.hashTable[i] is None:
                        continue
                    code += self.hashTable[i].visualize()
                    content = ""
                    if self.hashTable[i].root.is_two_node():
                        if type(self.hashTable[i].root.left_value) == tuple:
                            content = "\"" + str(self.hashTable[i].root.left_value[0]) + "\""
                        else:
                            content = "\"" + str(self.hashTable[i].root.left_value) + "\""
                    elif self.hashTable[i].root.is_three_node():
                        if type(self.hashTable[i].root.left_value) == tuple:
                            content = "\"" + str(self.hashTable[i].root.left_value[0]) + "  |  " + str(
                                self.hashTable[i].root.right_value[0]) + "\""
                        else:
                            content = "\"" + str(self.hashTable[i].root.left_value) + "  |  " + str(self.hashTable[i].root.right_value) + "\""

                    code += "\tstruct:f" + str(i) + ' -> ' + content + '\n'

        return code

# if __name__ == "__main__":
    # h = HashTable(5, "hsep", "234")
    # h.tableInsert(5)
    # h.tableInsert(9)
    # h.tableInsert(4)
    # h.tableInsert(6)
    # h.tableInsert(20)
    # h.tableInsert(14)
    # h.tableInsert(19)
    # h.tableInsert(25)
    # h.tableInsert(10)
    # h.tableInsert(1)
    # h.tableInsert(12)
    # h.tableInsert(8)
    # print(h.hashTable)
    # h.tableDelete(25)

    # print(h.visualize())

    # h = HashTable(6, "hsep", "23")
    # h.tableInsert(5)
    # h.tableInsert(20)
    # h.tableInsert(1)
    # h.tableInsert(6)
    # h.tableInsert(10)
    # h.tableInsert(9)
    # print(h.traverse())








