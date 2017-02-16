class DoubleLinkedListNode():
    def __init__(self, newItem, prev=None, next=None):
        # newItem = (searchKey, Content)
        if type(newItem) == tuple:
            try:
                self.key = newItem[0]
                self.content = newItem[1:]
                if len(self.content) == 1:
                    self.content = self.content[0]  # to provent tuple with 1 element -> just get element
            except:
                # if newItem[1] doesn's exist
                self.content = newItem[0]
        # newItem = (searchKey)
        else:
            self.key = newItem
            self.content = newItem
        self.prev = prev
        self.next = next


class DoubleLinkedList():
    def __init__(self):
        self.back = None
        self.front = None
        self.size = 0

    def destroyList(self):
        self.front = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def addChain(self, newItem):
        newItem = DoubleLinkedListNode(newItem)

        ptr = self.front
        if self.is_empty():
            self.back = newItem
            newItem.next = newItem
            newItem.prev = newItem
        else:
            while True:                     # To prevent duplicates
                if ptr.key == newItem.key:
                    return False
                ptr = ptr.next
                if ptr == self.front:
                    break
            self.back.next = newItem
            newItem.next = self.front
            self.front.prev = newItem
            newItem.prev = self.back
        self.front = newItem
        self.size += 1
        return True

    def removeChain(self, searchKey):
        ptr = self.front
        preptr = self.back
        while ptr.key != searchKey:
            preptr = ptr
            ptr = ptr.next
            if ptr == self.front:
                return False
        if ptr == self.front:
            self.front = ptr.next
            self.back.next = ptr.next
            self.front.prev = self.back
        elif ptr == self.back:
            preptr.next = self.front
            self.back = preptr
            self.front.prev = self.back
        else:
            preptr.next = ptr.next
            ptr.next.prev = preptr
        self.size -= 1
        return True

    def returnChain(self, searchKey):
        ptr = self.front
        while ptr.key != searchKey:
            ptr = ptr.next
            if ptr == self.front:
                return False, None
        return True, ptr.content

    def visualize(self):
        code = "\trankdir=LR\n" \
               "\tnode [shape=record];\n\t"

        ptr = self.front
        while True:
            if ptr != self.front:
                code += " -> "
            code += str(ptr.key)
            ptr = ptr.next
            if ptr is self.front:
                code += " -> " + str(ptr.key)
                break
        code += "\n\t"
        while True:
            if ptr != self.front:
                code += " -> "
            code += str(ptr.key)
            ptr = ptr.prev
            if ptr is self.front:
                code += " -> " + str(ptr.key)
                break

        return code

    def traverse(self):
        self.bubbleSort()
        ptr = self.front
        L = []
        for i in range(self.size):
            L.append(ptr.key)
            ptr = ptr.next
        return L

    def bubbleSort(self, funct="Key"):
        # BubbleSort algorithm
        size = self.size
        while size != 0 and size != 1:
            ptr = self.front
            nextptr = self.front.next
            for i in range(size-1):
                if funct == "Play":
                    # Sort op Date, Timeslot, Roomname
                    ptrdate = ptr.content.date
                    ptrtime = ptr.content.timeSlot
                    ptrname = ptr.content.roomName
                    nextptrdate = nextptr.content.date
                    nextptrtime = nextptr.content.timeSlot
                    nextptrname = nextptr.content.roomName
                    if (ptrdate > nextptrdate or
                            (ptrdate == nextptrdate and ptrtime > nextptrtime) or
                            (ptrdate == nextptrdate and ptrtime == nextptrtime and ptrname > nextptrname)):
                        # Swap
                        tempkey = ptr.key
                        tempcont = ptr.content
                        ptr.key = nextptr.key
                        ptr.content = nextptr.content
                        nextptr.key = tempkey
                        nextptr.content = tempcont

                else:
                    if ptr.key > nextptr.key:
                        # Swap
                        tempkey = ptr.key
                        tempcont = ptr.content
                        ptr.key = nextptr.key
                        ptr.content = nextptr.content
                        nextptr.key = tempkey
                        nextptr.content = tempcont
                ptr = ptr.next
                nextptr = nextptr.next
            size -= 1

        return

if __name__ == "__main__":
    l = DoubleLinkedList()
    l.addChain(5)
    l.addChain(10)
    l.addChain(6)
    l.addChain(7)
    l.addChain(20)
    l.removeChain(6)
    l.addChain(1)
    print(l.visualize())
    print(l.traverse())