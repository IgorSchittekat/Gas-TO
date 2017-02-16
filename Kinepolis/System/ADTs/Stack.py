class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def destroyStack(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, newItem):
        n = Node(newItem)
        if not self.is_empty():
            n.next = self.top
        self.top = n
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            return False, None
        n = self.top
        self.top = n.next
        self.size -= 1
        return True, n.item

    def getTop(self):
        if self.is_empty():
            return False, None
        return True, self.top.item

    def visualize(self):
        code = '\tnode [shape=record];\n' \
               '\tstruct [label="'

        ptr = self.top
        while ptr is not None:
            if ptr is self.top:
                code += "<top> "
            else:
                code += "|"
            code += str(ptr.item)
            ptr = ptr.next
        code += '"];\n' \
                '\trankdir=LR\n' \
                '\tTop [shape=plaintext];\n' \
                '\tTop -> struct:top\n' \

        return code

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(6)
    s.push(7)
    s.push(20)
    s.pop()
    s.push(1)
    print(s.visualize())

