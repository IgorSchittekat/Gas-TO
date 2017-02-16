class TwoThreeNode:
    #  Constructor
    def __init__(self, left_value=None, right_value=None):
        #  Input parameters get assigned to their attributes
        #  Left value is always bigger than right
        self.left_value = left_value
        self.right_value = right_value

        #  Values are put in the correct order if they are not already
        if right_value is not None and left_value > right_value:
            self.left_value, self.right_value = \
                self.right_value, self.left_value

        #  Initialize mid_value attribute used during split of node
        self.mid_value = None

        #  Following 'pointers' always point to TwoThreeTree()-objects
        #  'pointers'/references to children trees get initialized
        self.left_child = None
        self.mid_child = None
        self.right_child = None

        #  Initialize special split child used during the split of a node
        self.split_child = None

        #  'pointer'/reference to super/parent tree gets initialized
        self.parent = None

    #  The __contains__ operator is overloaded so we can use the 'in' operator
    #  This makes further implementation a bit easier
    def __contains__(self, item):
        #  In case our left and right values are singular objects they are
        #  compared directly to the item left of the 'in' operator
        if self.left_value == item or self.right_value == item:
            return True

        #  In case our left and right values are tuples we check if they
        #  contain the item left of the 'in' operator
        if type(self.left_value) is tuple:
            if item in self.left_value:
                return True
        if type(self.right_value) is tuple:
            if item in self.right_value:
                return True

        return False

    #  Overloading this operator was done for debugging purposes and serves no
    #  use in the further implementation of this ADT
    def __str__(self):
        if self.parent is None:
            return "{}/{},{},{}/{},{},{},{}".format(self.parent,
                                                    self.left_value,
                                                    self.mid_value,
                                                    self.right_value,
                                                    self.left_child,
                                                    self.mid_child,
                                                    self.split_child,
                                                    self.right_child)
        else:
            return "{}/{},{},{}/{},{},{},{}".format(self.parent.root,
                                                    self.left_value,
                                                    self.mid_value,
                                                    self.right_value,
                                                    self.left_child,
                                                    self.mid_child,
                                                    self.split_child,
                                                    self.right_child)

    #  Returns True if the node contains no data/is an empty node
    def is_empty(self):
        return self.size() == 0

    # Returns True if the node contains one data element/is a two-node
    def is_two_node(self):
        return self.size() == 1

    # Returns True if the node contains two data elements/is a three-node
    def is_three_node(self):
        return self.size() == 2

    # Returns True if the node has no children,
    # in other words, if the node is a leaf
    def is_leaf(self):
        #  If all child 'pointers' are empty
        if (
            self.left_child is None
            and
            self.mid_child is None
            and
            self.right_child is None
        ):
            return True
        else:
            return False

    # Returns (int) the amount of data elements a node contains
    def size(self):
        #  Init an empty list to store elements =/= None
        values = []

        #  Traverse all possible value locations and add to values if =/= None
        for attribute in [self.left_value, self.mid_value, self.right_value]:
            if attribute is not None:
                values.append(attribute)

        #  Return the size of values (= the amount of elements a node contains)
        return len(values)

    #  Sorts the values in a node in place
    #  smallest left --> biggest right
    def sort_self(self):
        values = []
        #  Traverse all possible value locations and add to values if =/= None
        for attribute in [self.left_value, self.mid_value, self.right_value]:
            if attribute is not None:
                values.append(attribute)

        #  If the values are not tuples sort the list in place
        if type(values[0]) != tuple:
            values.sort()

        #  If the values are tuples sort the list in place based on
        #  the first element of the tuples
        else:
            values.sort(key=lambda tup: tup[0])

        #  If the node is empty, no left or right values need to be assigned
        if len(values) == 0:
            return

        #  If the node contains only one data element assign it to the
        #  left_value and empty all other values
        if len(values) == 1:
            self.left_value = values[0]
            self.right_value = None
            self.mid_value = None
            return

        #  If node contains two or more data elements assign values from
        #  left to right in order of sorted list (values)
        self.left_value = values[0]
        self.right_value = values[-1]
        if len(values) == 3:
            self.mid_value = values[1]


class TwoThreeTree:
    #  Constructor
    def __init__(self, root_node=None):
        self.root = root_node

    #  Destructor
    def destroy_two_three_tree(self):
        self.root = None

    #  Returns True if tree is empty
    def is_empty(self):
        return self.root is None

    #  Helper method used to reassign children in split method
    #  and reassign their parent references correctly
    def set_child(self, position, child_node):
        #  position:
        #  1 = set left_child
        #  2 = set mid_child
        #  3 = set split_child
        #  4 = set right_child
        if position == 1:
            self.root.left_child = TwoThreeTree(child_node)
            child_node.parent = self
        elif position == 2:
            self.root.mid_child = TwoThreeTree(child_node)
            child_node.parent = self
        elif position == 3:
            self.root.split_child = TwoThreeTree(child_node)
            child_node.parent = self
        elif position == 4:
            self.root.right_child = TwoThreeTree(child_node)
            child_node.parent = self

    #  This inorder_traverse method has multiple uses which are determined
    #  by the passed boolean parameters
    #  ~if successor_search is True the method locates the leftmost child of
    #   the subtree where traversal started, so if we want the inorder
    #   successor of a node we can call successor_search on it's right child
    #  ~if parent_repair is True the tree is traversed and any missing or
    #   incorrect parent references are corrected
    #  ~if both successor_search and parent_repair are False then an ordered
    #   list of all values/search keys is returned
    def inorder_traverse(self, successor_search=False, parent_repair=False):
        #  initialize empty list
        L = []
        #  If the root of the current tree is a two-node we only have to deal
        #  with one value and two children so we proceed accordingly
        if self.root.is_two_node():
            #  We check if the left child exists
            if self.root.left_child is not None:
                #  If we are looking for a successor we continue traversing
                #  down the left side of the (sub)tree with successor_search
                #  set to True
                if successor_search:
                    return self.root.left_child.inorder_traverse(True)

                #  If we are repairing parent references we set self as the
                #  parent of the left child and continue traversal with
                #  parent_repair enabled
                elif parent_repair:
                    self.root.left_child.root.parent = self
                    self.root.left_child.inorder_traverse(False, True)

                #  If we're simply traversing we extend the list of keys/values
                #  with the ordered list of keys/values of the left subtree
                else:
                    L.extend(self.root.left_child.inorder_traverse())

            #  If we're looking for a successor and we have no more children
            #  on the left we have reached the leftmost node and we need not
            #  traverse further so we return it
            if successor_search:
                return self

            #  If we're not repairing parent references we're simply traversing
            #  so we append the value stored in the current node to the list
            if not parent_repair:
                #  If the value is a tuple we append the search key
                if type(self.root.left_value) == tuple:
                    L.append(self.root.left_value[0])
                #  If not we simply append the stored value
                else:
                    L.append(self.root.left_value)

            # We check if the right child exists
            if self.root.right_child is not None:
                #  If we are repairing parent references we set self as the
                #  parent of the right child and continue traversal with
                #  parent_repair enabled
                if parent_repair:
                    self.root.right_child.root.parent = self
                    self.root.right_child.inorder_traverse(False, True)

                #  If we're simply traversing we extend the list of keys/values
                #  with the ordered list of keys/values of the right subtree
                else:
                    L.extend(self.root.right_child.inorder_traverse())

        #  If the root of the current tree is a three-node we have to deal with
        #  two values and three children so we proceed accordingly
        elif self.root.is_three_node():
            #  We check if the left child exists
            if self.root.left_child is not None:
                #  If we are looking for a successor we continue traversing
                #  down the left side of the (sub)tree with successor_search
                #  set to True
                if successor_search:
                    return self.root.left_child.inorder_traverse(True)

                #  If we are repairing parent references we set self as the
                #  parent of the left child and continue traversal with
                #  parent_repair enabled
                elif parent_repair:
                    self.root.left_child.root.parent = self
                    self.root.left_child.inorder_traverse(False, True)

                #  If we're simply traversing we extend the list of keys/values
                #  with the ordered list of keys/values of the left subtree
                else:
                    L.extend(self.root.left_child.inorder_traverse())

            #  If we're looking for a successor and we have no more children
            #  on the left we have reached the leftmost node and we need not
            #  traverse further so we return it
            if successor_search:
                return self

            #  If we're not repairing parent references we're simply traversing
            #  so we append the left value stored in the current node
            if not parent_repair:
                #  If the value is a tuple we append the search key
                if type(self.root.left_value) == tuple:
                    L.append(self.root.left_value[0])

                # If not we simply append the stored value
                else:
                    L.append(self.root.left_value)

            # We check if the mid child exists
            if self.root.mid_child is not None:
                #  If we are repairing parent references we set self as the
                #  parent of the mid child and continue traversal with
                #  parent_repair enabled
                if parent_repair:
                    self.root.mid_child.root.parent = self
                    self.root.mid_child.inorder_traverse(False, True)

                #  If we're simply traversing we extend the list of keys/values
                #  with the ordered list of keys/values of the mid subtree
                else:
                    L.extend(self.root.mid_child.inorder_traverse())

            #  If we're not repairing parent references we're simply traversing
            #  so we append the right value stored in the current node
            if not parent_repair:
                #  If the value is a tuple we append the search key
                if type(self.root.right_value) == tuple:
                    L.append(self.root.right_value[0])

                # If not we simply append the stored value
                else:
                    L.append(self.root.right_value)

            # We check if the right child exists
            if self.root.right_child is not None:
                #  If we are repairing parent references we set self as the
                #  parent of the right child and continue traversal with
                #  parent_repair enabled
                if parent_repair:
                    self.root.right_child.root.parent = self
                    self.root.right_child.inorder_traverse(False, True)

                #  If we're simply traversing we extend the list of keys/values
                #  with the ordered list of keys/values of the mid subtree
                else:
                    L.extend(self.root.right_child.inorder_traverse())

        return L

    #  Wrapper method to find the correct inorder successor in the correct
    #  subtree using the inorder_traverse method with successor_search enabled
    def find_inorder_successor(self, smallest=True):
        #  If we need the successor of the left element of a three-node we need
        #  to look for it in the mid subtree
        if self.root.is_three_node() and smallest:
            return self.root.mid_child.inorder_traverse(successor_search=True)
        #  In all other situations we look for the successor in the
        #  right subtree
        else:
            return self.root.right_child.inorder_traverse(successor_search=True
                                                          )

    #  This methods searches the tree for a target item and returns a tuple
    #  with (True, node) if it is found and (False, None) if it is not
    def search(self, target):
        #  If the tree is empty there is nothing to search through
        if self.is_empty():
            return False, None

        #  If the root node contains the target item return True and the location in the tree
        elif target in self.root:
            return True, self

        #  If the root doesn't contain the target item and the node is a leaf
        #  we can't look any further so the tree doesn't contain the item
        elif self.root.is_leaf():
            return False, None

        #  Check if root is a three-node
        elif self.root.is_three_node():
            if type(self.root.left_value) == tuple:
                #  If the target is smaller than the left value continue
                #  down the left subtree
                if target < self.root.left_value[0] and self.root.left_child is not None:
                    return self.root.left_child.search(target)

                #  If the target is larger than the left value and smaller than the
                #  right value continue down the left subtree
                elif target < self.root.right_value[0] and self.root.mid_child is not None:
                    return self.root.mid_child.search(target)

                #  If the target is larger than the right value continue
                #  down the right subtree
                elif target > self.root.right_value[0] and self.root.right_child is not None:
                    return self.root.right_child.search(target)
            else:
                #  If the target is smaller than the left value continue
                #  down the left subtree
                if target < self.root.left_value and self.root.left_child is not None:
                    return self.root.left_child.search(target)

                # If the target is larger than the left value and smaller than the
                #  right value continue down the left subtree
                elif target < self.root.right_value and self.root.mid_child is not None:
                    return self.root.mid_child.search(target)

                # If the target is larger than the right value continue
                #  down the right subtree
                elif target > self.root.right_value and self.root.right_child is not None:
                    return self.root.right_child.search(target)

        #  Check if root is a two-node
        elif self.root.is_two_node():
            if type(self.root.left_value) == tuple:
                #  If the target is smaller than the left value continue
                #  down the left subtree
                if target < self.root.left_value[0] and self.root.left_child is not None:
                    return self.root.left_child.search(target)

                #  If the target is larger than the left value continue
                #  down the right subtree
                elif target > self.root.left_value[0] and self.root.right_child is not None:
                    return self.root.right_child.search(target)
            else:
                #  If the target is smaller than the left value continue
                #  down the left subtree
                if target < self.root.left_value and self.root.left_child is not None:
                    return self.root.left_child.search(target)

                # If the target is larger than the left value continue
                #  down the right subtree
                elif target > self.root.left_value and self.root.right_child is not None:
                    return self.root.right_child.search(target)

    #  Wrapper method which uses the search method to retrieve the node with
    #  the target data and then extracts the correct data from the node and
    #  returns it
    #  We only implemented retrieval for tuple based values containing a search
    #  key as retrieving a singular value is quite useless, for that we can use
    #  the search method which returns the node containing the singular value
    def retrieve(self, target):
        found, node = self.search(target)

        #  If the target it not found
        if not found:
            return False, None

        #  If the target is in the left value return the data from the left
        #  value, not the whole tuple also containing the search key
        if target == node.root.left_value or target in node.root.left_value:
            return True, node.root.left_value[1]

        #  If the target is in the right value return the data from the right
        #  value, not the whole tuple also containing the search key
        elif target == node.root.right_value or target in node.root.right_value:
            return True, node.root.right_value[1]

    #  Helper method which splits nodes during insertion of data, it also
    #  redistributes the children correctly after splitting
    def split(self):
        #  Bool to indicate if current node is a leaf
        root_was_not_leaf = False

        # If a node has no parent it is the main root of the whole tree
        if self.root.parent is None:
            # Create new nodes containing left and right values
            left_node = TwoThreeNode(self.root.left_value)
            right_node = TwoThreeNode(self.root.right_value)

            #  Assign values correctly in current node
            self.root.left_value = self.root.mid_value
            self.root.mid_value = None
            self.root.right_value = None

            # If current node is not a leaf redistribute the children correctly
            if not self.root.is_leaf():
                root_was_not_leaf = True
                #  Save current children
                temp_children_list = [self.root.left_child.root,
                                      self.root.mid_child.root,
                                      self.root.split_child.root,
                                      self.root.right_child.root]
                #  Destroy current children
                self.root.left_child.destroy_two_three_tree()
                self.root.mid_child.destroy_two_three_tree()
                self.root.split_child.destroy_two_three_tree()
                self.root.right_child.destroy_two_three_tree()

            # Set newly created nodes as children
            self.set_child(1, left_node)
            self.set_child(4, right_node)

            # If current node is not a leaf assign its old children to its new
            # children
            if root_was_not_leaf:
                self.root.left_child.set_child(1, temp_children_list[0])
                self.root.left_child.set_child(4, temp_children_list[1])
                self.root.right_child.set_child(1, temp_children_list[2])
                self.root.right_child.set_child(4, temp_children_list[3])

            # This operation sometimes results in incorrect parent references
            #  so we repair them
            self.inorder_traverse(successor_search=False, parent_repair=True)

        # If the parent is a two-node we proceed accordingly
        elif self.root.parent.root.is_two_node():
            # We'e splitting the right subtree
            if self.root.mid_value  > self.root.parent.root.left_value:
                # We move own mid value to right value parent
                self.root.parent.root.right_value = self.root.mid_value
                # We remove own mid value
                self.root.mid_value = None
                #  We create new node containing own left value
                new_node = TwoThreeNode(self.root.left_value)
                # We set newly created node to mid child of parent
                self.root.parent.set_child(2, new_node)
                # We move own right value to own left value
                self.root.left_value = self.root.right_value
                # We remove own right value
                self.root.right_value = None

                # If current node is not a leaf redistribute the children
                # correctly
                if not self.root.is_leaf():
                    root_was_not_leaf = True
                    #  Save current children
                    temp_children_list = [self.root.left_child.root,
                                          self.root.mid_child.root,
                                          self.root.split_child.root,
                                          self.root.right_child.root]
                    #  Destroy current children
                    self.root.left_child.destroy_two_three_tree()
                    self.root.mid_child.destroy_two_three_tree()
                    self.root.split_child.destroy_two_three_tree()
                    self.root.right_child.destroy_two_three_tree()

                # If current node is not a leaf assign its old children to its
                # new children
                if root_was_not_leaf:
                    self.root.parent.root.mid_child.set_child(1, temp_children_list[0])
                    self.root.parent.root.mid_child.set_child(4, temp_children_list[1])
                    self.root.parent.root.right_child.set_child(1, temp_children_list[2])
                    self.root.parent.root.right_child.set_child(4, temp_children_list[3])

            #  We'e splitting the left subtree
            #  Analogous to split of right subtree just think in other direction
            elif self.root.mid_value < self.root.parent.root.left_value:
                self.root.parent.root.right_value = self.root.parent.root.left_value
                self.root.parent.root.left_value = self.root.mid_value
                self.root.mid_value = None
                new_node = TwoThreeNode(self.root.right_value)
                self.root.parent.set_child(2, new_node)
                self.root.right_value = None

                if not self.root.is_leaf():
                    root_was_not_leaf = True
                    temp_children_list = [self.root.left_child.root,
                                          self.root.mid_child.root,
                                          self.root.split_child.root,
                                          self.root.right_child.root]
                    self.root.left_child.destroy_two_three_tree()
                    self.root.mid_child.destroy_two_three_tree()
                    self.root.split_child.destroy_two_three_tree()
                    self.root.right_child.destroy_two_three_tree()

                if root_was_not_leaf:
                    self.root.parent.root.left_child.set_child(1, temp_children_list[0])
                    self.root.parent.root.left_child.set_child(4, temp_children_list[1])
                    self.root.parent.root.mid_child.set_child(1, temp_children_list[2])
                    self.root.parent.root.mid_child.set_child(4, temp_children_list[3])

            self.root.parent.inorder_traverse(successor_search=False, parent_repair=True)

        # If the parent is a three-node we proceed accordingly
        elif self.root.parent.root.is_three_node():
            # We'e splitting the left subtree
            if self.root.mid_value < self.root.parent.root.left_value:
                # Move left value of parent to mid
                self.root.parent.root.mid_value = self.root.parent.root.left_value
                # Move own mid value to parent left
                self.root.parent.root.left_value = self.root.mid_value
                # Remove own mid value
                self.root.mid_value = None
                # Move parent's mid child to split child postition
                self.root.parent.root.split_child = self.root.parent.root.mid_child
                # Remove parent's mid child
                self.root.parent.root.mid_child = None
                # Create new mid child for parent
                new_node = TwoThreeNode(self.root.right_value)
                # Set parent's mid child to newly created node
                self.root.parent.set_child(2, new_node)
                # Remove own right value
                self.root.right_value = None

                # Rest is analogous to parent is two-node
                if not self.root.is_leaf():
                    root_was_not_leaf = True
                    temp_children_list = [self.root.left_child.root,
                                          self.root.mid_child.root,
                                          self.root.split_child.root,
                                          self.root.right_child.root]
                    self.root.left_child.destroy_two_three_tree()
                    self.root.mid_child.destroy_two_three_tree()
                    self.root.split_child.destroy_two_three_tree()
                    self.root.right_child.destroy_two_three_tree()

                if root_was_not_leaf:
                    self.root.parent.root.left_child.set_child(1, temp_children_list[0])
                    self.root.parent.root.left_child.set_child(4, temp_children_list[1])
                    self.root.parent.root.mid_child.set_child(1, temp_children_list[2])
                    self.root.parent.root.mid_child.set_child(4, temp_children_list[3])

                self.root.parent.inorder_traverse(successor_search=False, parent_repair=True)
                self.root.parent.split()

            # We'e splitting the right subtree, analogous to split left subtree
            elif self.root.mid_value > self.root.parent.root.right_value:
                self.root.parent.root.mid_value = self.root.parent.root.right_value
                self.root.parent.root.right_value = self.root.mid_value
                self.root.mid_value = None
                new_node = TwoThreeNode(self.root.left_value)
                self.root.parent.set_child(3, new_node)
                self.root.left_value = self.root.right_value
                self.root.right_value = None

                if not self.root.is_leaf():
                    root_was_not_leaf = True
                    temp_children_list = [self.root.left_child.root,
                                          self.root.mid_child.root,
                                          self.root.split_child.root,
                                          self.root.right_child.root]
                    self.root.left_child.destroy_two_three_tree()
                    self.root.mid_child.destroy_two_three_tree()
                    self.root.split_child.destroy_two_three_tree()
                    self.root.right_child.destroy_two_three_tree()

                if root_was_not_leaf:
                    self.root.parent.root.split_child.set_child(1, temp_children_list[0])
                    self.root.parent.root.split_child.set_child(4, temp_children_list[1])
                    self.root.parent.root.right_child.set_child(1, temp_children_list[2])
                    self.root.parent.root.right_child.set_child(4, temp_children_list[3])

                self.root.parent.inorder_traverse(successor_search=False, parent_repair=True)
                self.root.parent.split()

            # We'e splitting the mid subtree, analogous to split left subtree
            elif(self.root.mid_value > self.root.parent.root.left_value and
                         self.root.mid_value < self.root.parent.root.right_value):
                self.root.parent.root.mid_value = self.root.mid_value
                self.root.mid_value = None
                new_node = TwoThreeNode(self.root.right_value)
                self.root.parent.set_child(3, new_node)
                self.root.right_value = None

                if not self.root.is_leaf():
                    root_was_not_leaf = True
                    temp_children_list = [self.root.left_child.root,
                                          self.root.mid_child.root,
                                          self.root.split_child.root,
                                          self.root.right_child.root]
                    self.root.left_child.destroy_two_three_tree()
                    self.root.mid_child.destroy_two_three_tree()
                    self.root.split_child.destroy_two_three_tree()
                    self.root.right_child.destroy_two_three_tree()

                if root_was_not_leaf:
                    self.root.parent.root.mid_child.set_child(1, temp_children_list[0])
                    self.root.parent.root.mid_child.set_child(4, temp_children_list[1])
                    self.root.parent.root.split_child.set_child(1, temp_children_list[2])
                    self.root.parent.root.split_child.set_child(4, temp_children_list[3])

                self.root.parent.inorder_traverse(successor_search=False, parent_repair=True)
                self.root.parent.split()

    #  Inserts the given data into the tree, returns boolean indicating
    #  success of operation
    def insert(self, payload):
        #  If tree is empty create new node and make it the root
        if self.root is None:
            self.root = TwoThreeNode(payload)
            return True

        #  If tree already contains given data don't insert, return False
        elif payload in self.root:
            return False

        #  insert if node is a leaf
        elif self.root.is_leaf():
            #  if node has only one value, insert  in right value
            if self.root.is_two_node():
                self.root.right_value = payload
            #  if node has only two values, insert  in mid value
            elif self.root.is_three_node():
                self.root.mid_value = payload
            #  sort the values of the node
            self.root.sort_self()
            #  if node now contains 3 elements split it
            if self.root.size() == 3:
                self.split()
            return True

        #  if node is not a leaf, look for point of insertion further down the
        #  tree
        else:
            #  check if node is a three-node
            if self.root.is_three_node():
                #  compare item to be inserted to values in node and proceed
                #  down correct subtree
                if payload < self.root.left_value and self.root.left_child is not None:
                    return self.root.left_child.insert(payload)
                elif payload < self.root.right_value and self.root.mid_child is not None:
                    return self.root.mid_child.insert(payload)
                elif payload > self.root.right_value and self.root.right_child is not None:
                    return self.root.right_child.insert(payload)

            #  check if node is a two-node
            elif self.root.is_two_node():
                #  compare item to be inserted to values in node and proceed
                #  down correct subtree
                if payload < self.root.left_value and self.root.left_child is not None:
                    return self.root.left_child.insert(payload)
                elif payload > self.root.left_value and self.root.right_child is not None:
                    return self.root.right_child.insert(payload)

    #  Deletes given data or data associated with given search key, returns a
    #  boolean indicating the success of the operation
    def delete(self, target):
        #  Determines if target is present, if so also its location
        present, location = self.search(target)
        #  If the item is not present in the tree it can't be deleted
        if not present:
            return False
        successor = None
        #  If the element is not in a leaf
        if not location.root.is_leaf():
            #  Check if node is two-node
            if location.root.is_two_node():
                #  We find the inorder successor and replace the value to be
                #  deleted with it
                successor = location.find_inorder_successor()
                location.root.left_value = successor.root.left_value
            #  Check if node is three-node
            elif location.root.is_three_node():
                #  We find the inorder successor and replace the value to be
                #  deleted with it
                #  If the target is the left value the successor is in the mid
                #  subtree, if the target is the right value the successor is
                #  in the right subtree
                if location.root.left_value == target:
                    successor = location.find_inorder_successor(True)
                    location.root.left_value = successor.root.left_value
                else:
                    successor = location.find_inorder_successor(False)
                    location.root.right_value = successor.root.left_value
            #  We fix the tree starting at the location of the successor
            successor.fix_tree()
            return True
        # If the element is in a leaf
        else:
            #  If target is in a two-node leaf it needs to be deleted by fixing
            #  the tree
            if location.root.is_two_node():
                location.fix_tree()
            #  If the target is in a three-node leaf we just delete is and move
            #  the other value to the left of the node
            elif location.root.is_three_node():
                if location.root.left_value == target or target in location.root.left_value:
                    location.root.left_value = location.root.right_value
                location.root.right_value = None
            return True

    #  Fixes/rebalances the tree after performing a delete operation, returns a
    #  boolean indicating success
    def fix_tree(self):
        #  if the node is a leaf and a three-node we just need to delete the left value (inorder successor)
        if self.root.is_three_node():
            self.root.left_value = self.root.right_value
            self.root.right_value = None
            return

        #  if node is the root, delete it
        elif self.root.parent is None:
            # we can't just delete because our variable would point to an empty tree
            if self.root.left_child is None and self.root.right_child is None:
                self.destroy_two_three_tree()
                return
            if self.root.left_child is None:
                self.root.left_child = self.root.right_child
            # we place all values and children of child in root
            self.root.left_value = self.root.left_child.root.left_value
            self.root.right_value = self.root.left_child.root.right_value
            if self.root.left_child.root.mid_child is not None:
                self.root.left_child.root.mid_child.root.parent = self
                self.root.mid_child = self.root.left_child.root.mid_child
            else:
                self.root.mid_child = None
            if self.root.left_child.root.right_child is not None:
                self.root.left_child.root.right_child.root.parent = self
                self.root.right_child = self.root.left_child.root.right_child
            else:
                self.root.right_child = None
            if self.root.left_child.root.left_child is not None:
                self.root.left_child.root.left_child.root.parent = self
                self.root.left_child = self.root.left_child.root.left_child
            else:
                self.root.left_child = None
            return

        # empty node is left child
        elif self.root.parent.root.left_child is self:
            if self.root.parent.root.is_three_node():
                if self.root.parent.root.mid_child.root.is_three_node():
                    # redistribute values
                    self.root.left_value = self.root.parent.root.left_value
                    self.root.parent.root.left_value = self.root.parent.root.mid_child.root.left_value
                    self.root.parent.root.mid_child.root.left_value = self.root.parent.root.mid_child.root.right_value
                    self.root.parent.root.mid_child.root.right_value = None
                    # redistribute children
                    if not self.root.is_leaf() or not self.root.parent.root.mid_child.root.is_leaf():
                        if self.root.left_child is None:
                            self.root.left_child = self.root.right_child
                        self.root.right_child = self.root.parent.root.mid_child.root.left_child
                        self.root.right_child.root.parent = self
                        self.root.parent.root.mid_child.root.left_child = self.root.parent.root.mid_child.root.mid_child
                        self.root.parent.root.mid_child.root.mid_child = None
                elif self.root.parent.root.mid_child.root.is_two_node():
                    # bring down value from parent to sibling
                    self.root.parent.root.mid_child.root.right_value = self.root.parent.root.mid_child.root.left_value
                    self.root.parent.root.mid_child.root.left_value = self.root.parent.root.left_value
                    # if parent has two values, move right one to left
                    self.root.parent.root.left_value = self.root.parent.root.right_value
                    self.root.parent.root.right_value = None
                    # if node is internal redistribute the children
                    if not self.root.is_leaf() or not self.root.parent.root.mid_child.root.is_leaf():
                        if self.root.left_child is None:
                            self.root.left_child = self.root.right_child
                        self.root.parent.root.mid_child.root.mid_child = self.root.parent.root.mid_child.root.left_child
                        self.root.parent.root.mid_child.root.left_child = self.root.left_child
                        self.root.left_child.root.parent = self.root.parent.root.mid_child
                    # move merged node to left position
                    self.root.parent.root.left_child = self.root.parent.root.mid_child
                    self.root.parent.root.mid_child = None
            elif self.root.parent.root.is_two_node():
                # if sibling is a three-node we can redistribute
                if self.root.parent.root.right_child.root.is_three_node():
                    # redistribute values
                    self.root.left_value = self.root.parent.root.left_value
                    self.root.parent.root.left_value = self.root.parent.root.right_child.root.left_value
                    self.root.parent.root.right_child.root.left_value = self.root.parent.root.right_child.root.right_value
                    self.root.parent.root.right_child.root.right_value = None
                    # redistribute children
                    if not self.root.is_leaf() or not self.root.parent.root.right_child.root.is_leaf():
                        if self.root.left_child is None:
                            self.root.left_child = self.root.right_child
                        self.root.right_child = self.root.parent.root.right_child.root.left_child
                        self.root.right_child.root.parent = self
                        self.root.parent.root.right_child.root.left_child = self.root.parent.root.right_child.root.mid_child
                        self.root.parent.root.mid_child.root.mid_child = None
                # if sibling is a two-node we need to merge
                elif self.root.parent.root.right_child.root.is_two_node():
                    # bring down value from parent to sibling
                    self.root.parent.root.right_child.root.right_value = self.root.parent.root.right_child.root.left_value
                    self.root.parent.root.right_child.root.left_value = self.root.parent.root.left_value
                    # parent node is now empty
                    self.root.parent.root.left_value = None
                    # if node is internal redistribute the children
                    if not self.root.is_leaf() or not self.root.parent.root.right_child.root.is_leaf():
                        if self.root.left_child is None:
                            self.root.left_child = self.root.right_child
                        self.root.parent.root.right_child.root.mid_child = self.root.parent.root.right_child.root.left_child
                        self.root.parent.root.right_child.root.left_child = self.root.left_child
                        self.root.left_child.root.parent = self.root.parent.root.right_child
                    # remove empty node
                    self.root.parent.root.left_child = None

        # empty node is right child
        elif self.root.parent.root.right_child is self:
            if self.root.parent.root.is_three_node():
                if self.root.parent.root.mid_child.root.is_three_node():
                    # redistribute values
                    self.root.left_value = self.root.parent.root.right_value
                    self.root.parent.root.right_value = self.root.parent.root.mid_child.root.right_value
                    self.root.parent.root.mid_child.root.right_value = None
                    # redistribute children
                    if not self.root.is_leaf() or not self.root.parent.root.mid_child.root.is_leaf():
                        if self.root.right_child is None:
                            self.root.right_child = self.root.left_child
                        self.root.left_child = self.root.parent.root.mid_child.root.right_child
                        self.root.left_child.root.parent = self
                        self.root.parent.root.mid_child.root.right_child = self.root.parent.root.mid_child.root.mid_child
                        self.root.parent.root.mid_child.root.mid_child = None
                # if sibling is a two-node we need to merge
                elif self.root.parent.root.mid_child.root.is_two_node():
                    # bring down value from parent to sibling
                    self.root.parent.root.mid_child.root.left_value = self.root.parent.root.left_value
                    # right value of parent is now empty because it has been move down
                    self.root.parent.root.right_value = None
                    # if node is internal redistribute the children
                    if not self.root.is_leaf() or not self.root.parent.root.mid_child.root.is_leaf():
                        if self.root.right_child is None:
                            self.root.right_child = self.root.left_child
                        self.root.parent.root.mid_child.root.mid_child = self.root.parent.root.mid_child.root.right_child
                        self.root.parent.root.mid_child.root.right_child = self.root.right_child
                        self.root.left_child.root.parent = self.root.parent.root.mid_child
                    # move merged node to right position
                    self.root.parent.root.right_child = self.root.parent.root.mid_child
                    self.root.parent.root.mid_child = None
            elif self.root.parent.root.is_two_node():
                # if sibling is a three-node we can redistribute
                if self.root.parent.root.left_child.root.is_three_node():
                    # redistribute values
                    self.root.left_value = self.root.parent.root.left_value
                    self.root.parent.root.left_value = self.root.parent.root.left_child.root.right_value
                    self.root.parent.root.left_child.root.right_value = None
                    # redistribute children
                    if not self.root.is_leaf() or not self.root.parent.root.left_child.root.is_leaf():
                        if self.root.right_child is None:
                            self.root.right_child = self.root.left_child
                        self.root.left_child = self.root.parent.root.left_child.root.right_child
                        self.root.left_child.root.parent = self
                        self.root.parent.root.left_child.root.right_child = self.root.parent.root.left_child.root.mid_child
                        self.root.parent.root.left_child.root.mid_child = None
                # if sibling is a two-node we need to merge
                elif self.root.parent.root.left_child.root.is_two_node():
                    # bring down value from parent to sibling
                    self.root.parent.root.left_child.root.right_value = self.root.parent.root.left_value
                    # parent node is now empty
                    self.root.parent.root.left_value = None
                    # if node is internal redistribute the children
                    if not self.root.is_leaf() or not self.root.parent.root.left_child.root.is_leaf():
                        if self.root.right_child is None:
                            self.root.right_child = self.root.left_child
                        self.root.parent.root.left_child.root.mid_child = self.root.parent.root.left_child.root.right_child
                        self.root.parent.root.left_child.root.right_child = self.root.right_child
                        self.root.right_child.root.parent = self.root.parent.root.left_child
                    # remove empty node
                    self.root.parent.root.right_child = None

        # empty node is mid child
        elif self.root.parent.root.mid_child is self:
            # if empty node is the mid child then parent is always three-node
            # left sibling is three-node
            if self.root.parent.root.left_child.root.is_three_node():
                # redistribute values
                self.root.left_value = self.root.parent.root.left_value
                self.root.parent.root.left_value = self.root.parent.root.left_child.root.right_value
                self.root.parent.root.left_child.root.right_value = None
                # redistribute children
                if not self.root.is_leaf() or not self.root.parent.root.left_child.root.is_leaf():
                    if self.root.right_child is None:
                        self.root.right_child = self.root.left_child
                    self.root.left_child = self.root.parent.root.left_child.root.right_child
                    self.root.left_child.root.parent = self
                    self.root.parent.root.left_child.root.right_child = self.root.parent.root.left_child.root.mid_child
                    self.root.parent.root.left_child.root.mid_child = None
            # right sibling is three-node
            elif self.root.parent.root.right_child.root.is_three_node():
                # redistribute values
                self.root.left_value = self.root.parent.root.right_value
                self.root.parent.root.right_value = self.root.parent.root.right_child.root.left_value
                self.root.parent.root.right_child.root.left_value = self.root.parent.root.left_child.root.right_value
                self.root.parent.root.left_child.root.right_value = None
                # redistribute children
                if not self.root.is_leaf() or not self.root.parent.root.right_child.root.is_leaf():
                    if self.root.left_child is None:
                        self.root.left_child = self.root.right_child
                    self.root.right_child = self.root.parent.root.right_child.root.left_child
                    self.root.right_child.root.parent = self
                    self.root.parent.root.right_child.root.left_child = self.root.parent.root.right_child.root.mid_child
                    self.root.parent.root.right_child.root.mid_child = None
            # if siblings are  two-node's we need to merge
            elif self.root.parent.root.left_child.root.is_two_node():
                # bring down value from parent to sibling
                self.root.parent.root.left_child.root.right_value = self.root.parent.root.left_value
                self.root.parent.root.left_value = self.root.parent.root.right_value
                self.root.parent.root.right_value = None
                # if node is internal redistribute the children
                if not self.root.is_leaf() or not self.root.parent.root.left_child.root.is_leaf():
                    if self.root.left_child is None:
                        self.root.left_child = self.root.right_child
                    self.root.parent.root.left_child.root.mid_child = self.root.parent.root.left_child.root.right_child
                    self.root.parent.root.left_child.root.right_child = self.root.left_child
                    self.root.left_child.root.parent = self.root.parent.root.left_child
                # remove mid node
                self.root.parent.root.mid_child = None

        #  If the parent is now empty it needs to be fixed
        if self.root.parent.root.is_empty():
            self.root.parent.fix_tree()
        return

    #  Returns a string containing the description of the tree in dot language
    #  (only the body, in other words without 'digraph G {}')
    def visualize(self):
        dotString = ""
        content = ""
        if self.root.is_two_node():
            if type(self.root.left_value) == tuple:
                content = "\"" + str(self.root.left_value[0]) + "\""
            else:
                content = "\"" + str(self.root.left_value) + "\""
        elif self.root.is_three_node():
            if type(self.root.left_value) == tuple:
                content = "\"" + str(self.root.left_value[0]) + "  |  " + str(self.root.right_value[0]) + "\""
            else:
                content = "\"" + str(self.root.left_value) + "  |  " + str(self.root.right_value) + "\""

        for child in [self.root.left_child,
                      self.root.mid_child,
                      self.root.right_child]:
            if child is not None and child.root is not None:
                child_content = ""
                if child.root.is_two_node():
                    if type(self.root.left_value) == tuple:
                        child_content = "\"" + str(child.root.left_value[0]) + "\""
                    else:
                        child_content = "\"" + str(child.root.left_value) + "\""
                elif child.root.is_three_node():
                    if type(self.root.left_value) == tuple:
                        child_content = "\"" + str(child.root.left_value[0]) + "  |  " + str(child.root.right_value[0]) + "\""
                    else:
                        child_content = "\"" + str(child.root.left_value) + "  |  " + str(child.root.right_value) + "\""
                dotString += content + " -> " + child_content + "\n"
                dotString += child.visualize()
            else:
                if type(self.root.left_value) == tuple:
                    invisibleNodeID = "invisiNode" + str(self.root.left_value[0])
                else:
                    invisibleNodeID = "invisiNode" + str(self.root.left_value)
                invisibleNode = invisibleNodeID + " [label=\"\",width=.1,style=invis]\n"
                dotString += invisibleNode
                dotString += content + " -> " + invisibleNodeID + " [style=invis]\n"


        return dotString


"""if __name__ == "__main__":
    a = TwoThreeNode(1)
    b = TwoThreeTree(a)
    b.destroy_two_three_tree()
    c = TwoThreeTree()
    c.insert(10)
    # c.insert(5)
    # c.insert(9)
    # c.insert(20)
    # c.insert(12)
    # c.insert(2)
    # c.insert(7)
    # c.insert(21)
    c.delete(10)

      c.insert((4,'andrei'))
   c.insert((6,'andrei'))
   c.insert((23,'andrei'))
   c.insert((6,'andrei'))
   c.insert((19,'andrei'))
   c.insert((60,'andrei'))
   c.insert((75,'andrei'))
   c.insert((100,'andrei'))
   c.insert((130,'andrei'))
   c.insert((90,'andrei'))
   c.insert((10,'andrei'))
   c.insert((30,'andrei'))
   c.delete(90)
   c.insert((675,'andrei'))
   c.insert((123,'andrei'))
   c.insert((285,'andrei'))
   c.insert((69,'andrei'))
   c.insert((99,'andrei'))
   c.insert((120,'andrei'))
   c.insert((420,'andrei'))
   c.insert((890,'andrei'))
   c.insert((455,'andrei'))
   c.insert((900,'andrei'))
   c.insert((648,'andrei'))
   c.insert((792,'andrei'))
   c.delete(69)
   c.insert((55,'andrei'))
   c.insert((101,'andrei'))
   c.insert((555,'andrei'))
   c.insert((666,'andrei'))
   c.insert((777,'andrei'))
   c.insert((999,'andrei'))
   c.insert((606,'andrei'))
   c.insert((1001,'andrei'))
   c.insert((439,'andrei'))
   c.insert((904,'andrei'))
   c.insert((421,'andrei'))
   c.insert((86,'andrei'))
   c.delete(420)

   print(c.visualize())

  tree = TwoThreeTree()
for i in range(1,50001):
random.seed(log(i**5, 56))
x = random.randint(1, 10000)
tree.insert(x)
tree.inorder_traverse()"""

