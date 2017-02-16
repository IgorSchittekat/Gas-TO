import System.ADTs.BinarySearchTree as BST
import System.ADTs.TwoThreeTree as TTT
import System.ADTs.TwoThreeFourTree as TTFT
import System.ADTs.RedBlackTree as RBT
import System.ADTs.Hashmap as HM
import System.ADTs.LinkedList as LL
import System.ADTs.CircLinkedList as CLL
import System.ADTs.DoubleLinkedList as DLL
import System.ADTs.Stack as S
import System.ADTs.Queue as Q


class Table:
    def __init__(self, method="bst",  hm_size=10, hm_chain="bst"):
        self.method = method
        if method == "bst":
            self.table = BST.BinarySearchTree()
        elif method == "23":
            self.table = TTT.TwoThreeTree()
        elif method == "234":
            self.table = TTFT.TwoThreeFourTree()
        elif method == "rb":
            self.table = RBT.RedBlackTree()
        elif method in ["hlin", "hquad", "hsep"]:
            self.table = HM.HashTable(hm_size, self.method, hm_chain)
        elif method == "ll":
            self.table = LL.LinkedList()
        elif method == "cll":
            self.table = CLL.CircLinkedList()
        elif method == "dll":
            self.table = DLL.DoubleLinkedList()
        elif method == "stack":
            self.table = S.Stack()
        elif method == "queue":
            self.table = Q.Queue()
        else:
            self.table = None

    def destroy(self):
        if self.method == "bst":
            return self.table.destroySearchTree()
        elif self.method == "23":
            return self.table.destroy_two_three_tree()
        elif self.method == "234":
            return self.table.destroyTwoThreeFourTree()
        elif self.method == "rb":
            return self.table.destroyRedBlackTree()
        elif self.method in ["hlin", "hquad", "hsep"]:
            return self.table.destroyHashtable()
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.destroyList()
        elif self.method == "stack":
            return self.table.destroyStack()
        elif self.method == "queue":
            return self.table.destroyQueue()
        else:
            return False

    def is_empty(self):
        return self.table.is_empty()

    def insert(self, newItem):
        if self.method == "bst":
            return self.table.searchTreeInsert(newItem)
        elif self.method == "23":
            return self.table.insert(newItem)
        elif self.method == "234":
            return self.table.insertItem(newItem)
        elif self.method == "rb":
            return self.table.insert(newItem)
        elif self.method in ["hlin", "hquad", "hsep"]:
            return self.table.tableInsert(newItem)
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.addChain(newItem)
        elif self.method == "stack":
            return self.table.push(newItem)
        elif self.method == "queue":
            return self.table.enqueue(newItem)
        else:
            return False

    def delete(self, searchKey=None):
        if self.method == "bst":
            return self.table.searchTreeDelete(searchKey)
        elif self.method == "23":
            return self.table.delete(searchKey)
        elif self.method == "234":
            return self.table.deleteKey(searchKey)
        elif self.method == "rb":
            return self.table.delete(searchKey)
        elif self.method in ["hlin", "hquad", "hsep"]:
            return self.table.tableDelete(searchKey)
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.removeChain(searchKey)
        elif self.method == "stack":
            return self.table.pop()
        elif self.method == "queue":
            return self.table.dequeue()
        else:
            return False

    def retrieve(self, searchKey=None):
        if self.method == "bst":
            return self.table.searchTreeRetrieve(searchKey)
        elif self.method == "23":
            return self.table.retrieve(searchKey)
        elif self.method == "234":
            return self.table.retrieve(searchKey)
        elif self.method == "rb":
            return self.table.retrieve(searchKey)
        elif self.method in ["hlin", "hquad", "hsep"]:
            return self.table.tableRetrieve(searchKey)
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.returnChain(searchKey)
        elif self.method == "stack":
            return self.table.getTop()
        elif self.method == "queue":
            return self.table.getFront()
        else:
            return False, None

    def traverse(self):
        if self.method == "bst":
            return self.table.inorderTraverse()
        elif self.method == "23":
            return self.table.inorder_traverse()
        elif self.method == "234":
            return self.table.inorderTraverse()
        elif self.method == "rb":
            return self.table.inorderTraverse()
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.traverse()
        elif self.method in ["ll", "cll", "dll"]:
            return self.table.traverse()
        else:
            return []

    def visualize(self):
        return self.table.visualize()



