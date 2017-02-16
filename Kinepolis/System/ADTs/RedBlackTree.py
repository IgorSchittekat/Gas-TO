
BLACK = 0
RED = 1

class RedBlackNode:

    def __init__(self, value, info, color = RED):
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.color = color
        self.value = value
        self.info = info
        
    def traverse_node(L):
        
        if self.value == None:
            return 
        
        else:
            traverse_node(L)
            L.append(self.value)
            traverse_node(L)

    def visualize_node(self):
        lijn = ""
        lijn_linker_kind = ""
        lijn_rechter_kind = ""
        
        if self.value == None:
             return lijn
            
        if self.leftChild.value == None:
            lijn_linker_kind = str(self.value) + " -> " + str(self.leftChild.value) + " [style=invis]"
            
        else:
            if self.color == 1: ## node is rood
                
                if self.leftChild.color == 1: ## linker _kind is ook rood
                    lijn_linker_kind = str(self.value) + " -> " + str(self.leftChild.value) + " [style=dotted]"
                    
                else:
                    lijn_linker_kind = str(self.value) + " -> " + str(self.leftChild.value)
                    
            else:  ## node is zwart
                lijn_linker_kind = str(self.value) + " -> " + str(self.leftChild.value)
                
                
                    
        if self.rightChild.value == None:
            lijn_rechter_kind = str(self.value) + " -> " + str(self.rightChild.value) + " [style=invis]"
            
        else:
            if self.color == 1: ## node is rood
                if self.rightChild.color == 1: ## rechter_kind is ook rood
                    lijn_rechter_kind = str(self.value) + " -> " + str(self.rightChild.value) + " [style=dotted]"
                else:
                    lijn_rechter_kind = str(self.value) + " -> " + str(self.rightChild.value)
            else: ## node is zwart
                lijn_rechter_kind = str(self.value) + " -> " + str(self.rightChild.value)
                
        lijn = lijn_linker_kind + "\n"
        lijn = lijn + str(self.value) + " -> " + str(None) + " [style=invis]" + "\n"
        lijn = lijn + lijn_rechter_kind + "\n"
        
        return lijn
        
            
            

class RedBlackTree:

    def __init__(self):
        self.sentinel = RedBlackNode(None, None, BLACK)  ## sentinel wordt gebruikt zodat elke knoop in een roodzwart boom 2 kinderen heeft
        self.sentinel.leftChild = self.sentinel          ## dit maakt het gemakelijker om te inserten en te deleten
        self.sentinel.rightChild = self.sentinel
        self.root = self.sentinel
        self.inorder_traverse_list =[]
        
       
    def is_empty(self):   ##Geeft True terug als de boom leeg is en False als er minstens 1 element in zit
        if self.root == self.sentinel:
            return True
        else:
            return False
    
    def destroy_red_black_tree(self):
        self.root = self.sentinel

    def split_4_node(self, current):
        
        current.leftChild.color = current.rightChild.color = 0
        if current != self.root:

            ## Sibling is de sibling van de huidige knoop
            if current.parent.rightChild == current:
                sibling = current.parent.leftChild
            else:
                sibling = current.parent.rightChild
                
            # geval 1: 4 knoop splitsen met een 2-knoop-ouder --> 3-knoop met ouder
            if current.parent.color == 0 and sibling.color == 0:
                current.color = 1
                
            # geval 2: 4 knoop splitsen met een 3-knoop-ouder -> 4- knoop met ouder en sibling
            if current.parent.color == 0 and sibling.color == 1:
                current.color = 1
            if current.parent.parent != None:
                
                if current.parent.color == 1 and current.parent.parent == 0 and sibling.color == 0:
                    
                    if current.parent == curent.parent.parent.leftChild and current == current.parent.leftChild:
                        temp_node = sibling
                        sibling = current.parent.parent
                        sibling.leftChild = temp_node
                        temp_node.parent= current.parent
                        current.color = 1
                        sibling.color = 1
                        current.parent.parent=None
                        
                    elif current.parent == current.parent.parent.rightChild and currnet == current.parent.leftChild: 
                        temp_node_1= current.parent
                        temp_node_2= current.parent.parent
                        temp_node_1.leftChild = current.rightChild
                        temp_node_2.righthChild = current.leftChild
                        current.rightChild = temp_node_2
                        current.leftChild = temp_node_1
                        temp_node_2.parent = temp_node_1.parent = current
                        current.leftChild.color = current.rightChild.color = 1
                        current.color = 0
                        current.parent = None

                
                    elif current.parent == current.parent.parent.leftChild and current == current.parent.rightChild:
                        temp_node_1= current.parent
                        temp_node_2= current.parent.parent
                        temp_node_1.rightChild = current.leftChild
                        temp_node_2.leftChild = current.rightChild
                        current.rightChild = temp_node_2
                        current.leftChild = temp_node_1
                        current.leftChild.color = current.rightChild.color = 1
                        current.color = 0
                        current.parent = None

                    elif current.parent == current.parent.parent.rightChild and current == current.parent.rightChild:
                        temp_node = sibling
                        sibling = current.parent.parent
                        sibling.parent = current.parent
                        current.parent.leftChild.rightChild = temp_node
                        sibling.color = current.color = 1
                        current.parent.color = 0
                        current.parent.parent = None
                    
        

    def insert(self, key_info_tuple): ## Deze methode voegt een knoop toe met gegeven key en/of info, geeft True terug als de key er 
        
        if isinstance(key_info_tuple,int): ## Als er een gewoon een integer wordt geïnsert is de searchkey de integer en info None
            value = key_info_tuple
            info = None
            
        else:
            value = key_info_tuple[0]  ## Als er een tuple wordt geïnsert met eerste element de searchkey en tweede extra info
            info = key_info_tuple[1]
            
        if self.root == self.sentinel:  ## Wanneer het voor het eerst een element wordt geïnsert
            node = RedBlackNode(value,info)
            node.leftChild = self.sentinel
            node.rightChild = self.sentinel
            node.parent = None
            self.root = node
            self.inorder_traverse_list.append(value)
            return True
            
        else:   ## Anders wordt er naar de plaats gezocht van de key die moet worden geïnsert
            
            current = self.root   
            parent = None
            while current != self.sentinel:
                parent = current
                
                ## Als we een 4 knoop tegenkomen gaan we deze splitsen
                if current.color == 0 and current.leftChild.color == 1 and current.rightChild.color == 1:
                    self.split_4_node(current)
                
                if current.value == value:
                    return False
                
                elif current.value < value:
                    current = current.rightChild
                    
                else:
                    current = current.leftChild

            
            node = RedBlackNode(value,info)
            node.leftChild = self.sentinel
            node.rightChild = self.sentinel
            node.parent = parent
            
            if value > parent.value:
                parent.rightChild = node
                
            else:
                parent.leftChild = node

       
        self.inorder_traverse_list.append(value) 
        return True
 

    def delete(self, value):
        node = self.retrieve_node(value)  ## node is de knoop die moet worden verwijderd
        
        if node == False:  ## Als node niet in de boom te vinden is, kunnen we ze niet deleten en wordt er False teruggegeven
            return False
        
        if node.leftChild == self.sentinel or node.rightChild == self.sentinel:  ## Als node geen linker of rechterkind heeft, wordt new_node node
        
            new_node = node
            
        else:               ##Als het een interne knoop is wordt new_node het rechterkind van node als het een linkerkind heeft
        
            new_node = node.rightChild
            if new_node.leftChild == self.sentinel:
                new_node= new_node.leftChild

 
        if new_node.leftChild != self.sentinel: ## Als new_node een linkerkind heeft wordt node dat linkerkind, anders wordt node het rechterkind
            node = new_node.leftChild
            
        else:
            node = new_node.rightChild


        node.parent = new_node.parent  ## Er wordt zeker gemaakt dat node en new_node dezelfde parent hebben
        
        if new_node.parent:  ## Check ofdat new_node de root is van onze rz boom 
            if new_node == new_node.parent.leftChild: ## node wordt verplaats naar new_node
                new_node.parent.leftChild = node
                
            else:
                new_node.parent.rightChild = node
                
        else:  ##Als new_node wel de root is wordt de root gelijkgesteld aan node
            self.root = node


        del new_node  ## De node wordt verwijdert
        self.inorder_traverse_list.remove(value)
        return True


    def inorder_traverse(self):
        self.inorder_traverse_list.sort()
        return self.inorder_traverse_list

            
    def retrieve_node(self, value):  ## Deze methode wordt gebruikt bij het deleten van een node
        current = self.root
        found = False
        while current != self.sentinel:
            if current.value == value:
                found = True
                return current
            elif value > current.value:
                current = current.rightChild
            else:
                current = current.leftChild
        if not found:
            return False
        
    def retrieve(self, value):
   
        current = self.root
        found = False
        while current != self.sentinel:
            if current.value == value:
                found = True
                return (True, current.info)   ## Als de key wordt gevonden wordt (True, info) teruggegeven
            
            elif value > current.value:
                current = current.rightChild
                
            else:
                current = current.leftChild
                
        if not found:   ## Als de key niet is gevonden wordt (False, None) teruggegeven
            return (False,None)
        
    
    def visualize(self):
        dotCode = ""
        line = ""
        if self.root == self.sentinel:
            return dotCode
        else:
            dotCode = self.root.visualize_node()
        
        self.current = self.root
        for Node in [self.current.leftChild, self.current.rightChild]:
            if Node != self.sentinel:
                line = Node.visualize_node()
            dotCode = dotCode + line

        return dotCode

        

        

        
if __name__ == "__main__":
    
    rb2 = RedBlackTree()
    print(rb2.insert((0, "Hallo")), True)
    print(rb2.insert((6, "Hey")), True)
    print(rb2.insert((12, "Hello")), True)
    print(rb2.insert((1, "Hola")), True)
    print(rb2.retrieve(1), (True, "Hola"))
    print(rb2.delete(0), True)
    print(rb2.retrieve(0), (False, None))
    print(rb2.delete(12),True)
    print(rb2.delete(0), False)

    rb1 = RedBlackTree()
    print(rb1.is_empty(), True)
    print(rb1.insert(50),True)
    print(rb1.is_empty(), False)
    print(rb1.delete(50),True)
    print(rb1.delete(50),False)
    print(rb1.is_empty(), True)
    print(rb1.insert(50), True)
    print(rb1.insert(60),True)
    print(rb1.delete(50), True)
    print(rb1.delete(60),True)
