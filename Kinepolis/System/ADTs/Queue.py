class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.queueFront = None
        self.queueBack = None
        self.size = 0

    def destroyQueue(self):
        self.queueFront = None
        self.queueBack = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, newItem):
        n = Node(newItem)
        if not self.is_empty():
            self.queueBack.next = n
        self.queueBack = n
        if self.is_empty():
            self.queueFront = n
        # als het 2e element wordt toegevorgd
        if self.size == 1:
            self.queueFront.next = self.queueBack
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False, None
        n = self.queueFront
        self.queueFront = n.next
        self.size -= 1
        return True, n.item

    def getFront(self):
        if self.is_empty():
            return False, None
        return True, self.queueFront.item

    def visualize(self):
        code = '\tnode [shape=record];\n' \
               '\tstruct [label="'

        ptr = self.queueFront
        while ptr is not None:
            if ptr is self.queueFront:
                code += "<front> "
            else:
                code += "|"
            code += str(ptr.item)
            ptr = ptr.next
        code += '"];\n' \
                '\tFront [shape=plaintext];\n' \
                '\tFront -> struct:front\n' \

        return code

if __name__ == "__main__":
    s = Queue()
    s.enqueue(5)
    s.enqueue(10)
    s.enqueue(6)
    s.enqueue(7)
    s.enqueue(20)
    s.dequeue()
    s.enqueue(1)
    print(s.visualize())

