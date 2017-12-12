# Bezawit Woldegebriel
# DoublyLinkedLists

class Node(object):

    def __init__(self, prev = None, data=None, next = None):
        self._prev = prev
        self._data = data
        self._next = next

    def __str__(self):
        return str(self._data)
    def __repr__(self):
        return "Node(%s,%s,%s)" % (repr(self._prev), repr(self._data), repr (self._next))
    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self._prev == other._prev and self._data == other._data and self._next == other._next

#-------------------------------------------------------------------------------

class DoublyLinkedList(object):
    # (Doubly) linked list.
    # Constructed with a dummy node at the begining and end of the list.
    # The list object stores a references to the dummy node 
    # and also stores list's length.

    def __init__(self):
        self._first = Node(None, None, None)
        self._length = 0
        self._last = Node(self._first, None, None)
        self._first._next = self._last
        
    def __len__(self):
        return self._length
    
    def _insertItemAfterNode(self,item,aNode):
        newNode = Node(aNode, item, aNode._next)
        aNode._next._prev = newNode
        aNode._next= newNode
        self._length += 1

    def _insertItemBeforeNode(self, item, aNode):
        newNode = Node(aNode._prev._next, item, aNode)
        aNode._prev._next = newNode
        aNode._prev = newNode
        self._length += 1
        
    def _nodeBeforeIndex(self, index):
        if 0 <= index <= self._length:
            aNode = self._first
            for i in range(index):
                aNode = aNode._next
            return aNode
        else:
            raise IndexError

    def __getitem__(self, index):
        return self._nodeBeforeIndex(index)._next._data

    def __iter__(self):
        return DoublyLinkedListIterator(self) 
        
    def __setitem__(self, index, item):
        self._nodeBeforeIndex(index)._next._data = item

    def insertItemAtTheFront(self, item):
        self._insertItemAfterNode(item, self._first)
        
    def insertItemAtTheEnd(self, item):
        self._insertItemBeforeNode(item, self._last)

    def insertItemAtIndex(self, index, item):
        '''Valid range 0 <= index <= length.'''
        self._insertItemAfterNode(item, self._nodeBeforeIndex(index))

    def __iter__(self):
        return DoublyLinkedListIterator(self)

    def __repr__(self):
        plist = []
        for item in self:
            plist.append(item)
        return "DoublyLinkedList(%s)" % str(plist)
#-------------------------------------------------------------------------------
class DoublyLinkedListIterator(object):

    def __init__(self, aList):
        self._list = aList
        self._currentIndex = -1
        self._currentNode = self._list._first

    def __iter__(self):
        return self

    def __next__(self):
        if self._currentIndex == self._list._length - 1:
            raise StopIteration
        else:
            self._currentIndex += 1
            self._currentNode = self._currentNode._next
            return self._currentNode._data

#-------------------------------------------------------------------------------
def main():
    print("Creating a Doubly Linked List:")
    x = DoublyLinkedList()
    print(x)
    print()

    print("Adding 4 at the beginning:")
    x.insertItemAtTheFront(4)
    print(x)
    print()

    print("Adding 6 at the beginning:")
    x.insertItemAtTheFront(6)
    print(x)
    print()

    print("Adding 9 at the end:")
    x.insertItemAtTheEnd(9)
    print(x)
    print()

    print("Adding 5 at the end:")
    x.insertItemAtTheEnd(5)
    print(x)
    print()

    print("Inserting 11 item at index 2:")
    x.insertItemAtIndex(2,11)
    print(x)
    print()
          
    print("Inserting 22 item at index 4:")
    x.insertItemAtIndex(4,22)
    print(x)
    print()

    print("Length of the list:")
    print(len(x))
    print()
    
main()

        
