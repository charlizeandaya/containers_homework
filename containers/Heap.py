'''
This file implements the Heap data structure as a subclass of
the BinaryTree.
The book implements Heaps using an *implicit* tree with an
*explicit* vector implementation,
so the code in the book is likely to be less helpful than the code
for the other data structures.
The book's implementation is the traditional implementation because
it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help you
get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs is None:
            xs = []
        for x in xs:
            self.insert(x)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string
        that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap
        will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete
        functions are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left:
            ret &= (node.left.value >= node.value)
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= (node.right.value >= node.value)
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        1. Find the next position in the tree using the binary representation
        of the total number of nodes
            1. You will have to explicitly store the size of your heap in a
            variable (rather than compute it) to maintain the O(log n)
            runtime
            2. See
            https://stackoverflow.com/questions/18241192/implement-heap-using-a-binary-tree
            for hints
        2. Add `value` into the next position
        3. Recursively swap value with its parent until the heap property is
        satisfied

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the BST and AVLTree insert
        functions.
        '''
        if self.root:
            nodes = self.__len__()
            numlist = "{0:b}".format(nodes + 1)[1:]
            self.root = Heap._insert(self.root, value, numlist)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, numlist):
        if numlist[0] == '0':
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, value, numlist[1:])
        if numlist[0] == '1':
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, value, numlist[1:])
        if numlist[0] == '0':
            if node.left.value < node.value:
                newnode = node.value
                node.value = node.left.value
                node.left.value = newnode
                return node
            else:
                return node
        if numlist[0] == '1':
            if node.right.value < node.value:
                newnode = node.value
                node.value = node.right.value
                node.right.value = newnode
                return node
            else:
                return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in list(xs):
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right
        3. "trickle down" the root node: recursively swap it with its largest
        child until the heap property is satisfied

        HINT:
        I created two @staticmethod helper functions: _remove_bottom_right
        and _trickle.
        It's possible to do it with only a single helper (or no helper at all),
        but I personally found dividing up the code into two made the most
        sense.
        '''
        if self.root:
            nodes = self.__len__()
            if nodes == 1:
                self.root = None
        else:
            bottom = "{0:b}".format(nodes)[1:]
            self.root, self.root.value = Heap._remove_bottom_right(
                self.root, bottom)
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, remlist):
        if remlist:
            if remlist[0] == '0':
                if len(remlist) > 1:
                    return Heap._remove_bottom_right(
                        node.left, remlist[1:])
                else:
                    temp = node.left.value
                    node = None
                    return temp

            elif remlist[0] == '1':
                if len(remlist) > 1:
                    return Heap._remove_bottom_right(
                        node.right, remlist[1:])
                else:
                    temp = node.right.value
                    node = None
                    return temp
        else:
            temp = node.value
            node = None
            return temp

    @staticmethod
    def _trickle(node):
        if not Heap._is_heap_satisfied(node):
            if node.left:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node.left = Heap._trickle(node.left)
            elif node.right:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node.right = Heap._trickle(node.right)
            elif node.left and node.right:
                if node.left.value >= node.right.value:
                    temp = node.value
                    node.value = node.right.value
                    node.right.value = temp
                    node.right = Heap._trickle(node.right)
                elif node.left.value <= node.right.value:
                    temp = node.value
                    node.value = node.left.value
                    node.left.value = temp
                    node.left = Heap._trickle(node.left)
            else:
                return node
        else:
            return node
        return node
