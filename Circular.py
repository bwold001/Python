#!/usr/bin/env python3

# Circular Array
# Bezawit Woldegebriel
# 04/01/2014

import ctypes
import math

class CircularArray:
    """A seqential container with O(1) indexing
     and amortized O(1) appending at either end.
     Implemented as a dynamic circular array
     with geometric expansion.
    """

    def __init__(self, item=[]):
        """ Create an empty array or of given items."""

        
        self._dataCount = len(item)
        if len(item) == 0:
            self._blockCapacity = 5
        else:
            self._blockCapacity = 3*self._dataCount

        self._dataStartIndex = self._blockCapacity//3  #start of the middle third
        self._dataEndIndex=0
        self._block = self._makeBlock(self._blockCapacity)

        i = self._dataStartIndex
        for n in item:
            self._block[i] = n
            i+=1

    def append(self, obj):
        if self._dataCount == self._blockCapacity:
            self._resizeBlock()
            self._block[self._dataStartIndex + self._dataCount] = obj
            
        else:
            self._dataEndIndex=(self._dataCount+self._dataStartIndex)-1
            self._dataEndIndex = (self._dataEndIndex + 1)%self._blockCapacity            
            self._block[self._dataEndIndex] = obj
            
        self._dataCount += 1

    def preappend(self,obj):
        if self._dataCount == self._blockCapacity:
            self._resizeBlock()
            self._dataStartIndex -= 1
        else:
            self._dataStartIndex = (self._dataStartIndex - 1) % self._blockCapacity
            
        self._block[self._dataStartIndex]=obj
        self._dataCount += 1

    def _makeBlock(self,capacity):
        return (capacity * ctypes.py_object) ()

    def __getitem__(self, index):
        if not 0 <= index < self._dataCount:
            raise IndexError('Invalid index: ' + str(index) + '.')
        return self._block[self._dataStartIndex + index]

    def insert(self, index, value):
        if not 0 <= index < self._dataCount:
            raise IndexError('Invalid index: ' + str(index) + '.')
        if self._dataStartIndex + self._dataCount == self._blockCapacity:
            self._resizeBlock()
        for j in range(self._dataCount, index, -1): # shift rightmost first
            self._block[self._dataStartIndex+j] = self._block[self._dataStartIndex+j-1]
        self._block[self._dataStartIndex + index] = value # store new value
        self._dataCount += 1

    def remove(self, index):                      
        if not 0 <= index < self._dataCount:
            raise IndexError('Invalid index: ' + str(index) + '.')
        item = self._block[self._dataStartIndex + index]
        for j in range(index, self._dataCount - 1): # shift others to fill gap
            self._block[self._dataStartIndex + j] = self._block[self._dataStartIndex +j + 1]
        self._block[self._dataStartIndex + self._dataCount - 1] = None # help garbage collection

        self._dataCount -= 1

    def removeFirst(self):
        index = 0
        if not 0 <= index < self._dataCount:
            raise IndexError('Invalid index: ' + str(index) + '.')
        item = self._block[self._dataStartIndex + index]
        for j in range(index, self._dataCount - 1): # shift others to fill gap
            self._block[self._dataStartIndex + j] = self._block[self._dataStartIndex +j + 1]
        self._block[self._dataStartIndex + self._dataCount - 1] = None # help garbage collection
        self._dataCount -= 1
        
    def removeLast(self):
        item = (self._dataStartIndex+self._dataCount)-1
        for j in range(item, self._dataCount - 1):
            self._block[self._dataStartIndex + j] = self._block[self._dataStartIndex +j + 1]
        self._block[(item)] = None
        self._dataCount -= 1

    def __eq__(self,other):
        if self._dataCount != other._dataCount:
          return False
        for i in range(self._dataCount):
          if self._block[self._dataStartIndex + i] != other._block[other._dataStartIndex + i]:
            return False
        return True
    
    def __len__(self):
        return self._dataCount

    def __repr__(self):
        items = []
        for i in range(0, self._dataCount):
            items.append(self.__getitem__(i))
        return "CircularArray(" + repr(items) + ")"

    def _print(self):
        items = []
        for i in range(0, self._dataCount):
          items.append(repr(self.__getitem__(i)))
          items.append(",")
        preItems = "_," * self._dataStartIndex
        postItems = "_," * (self._blockCapacity - self._dataStartIndex - self._dataCount)
        print(preItems + "".join(items) + postItems,
              " capacity=", self._blockCapacity,
              " count=", self._dataCount,
              " startIndex=", self._dataStartIndex,
              sep="")

    def _resizeBlock(self):
        if self._dataCount == 0:
          newBlockCapacity = 3
          newDataStartIndex = 1
        else:
          newBlockCapacity = 3 * self._dataCount
          newDataStartIndex = self._dataCount
        newBlock = self._makeBlock(newBlockCapacity)
        for k in range(self._dataCount):
          newBlock[newDataStartIndex + k] = self._block[self._dataStartIndex + k]
        self._block = newBlock
        self._blockCapacity = newBlockCapacity
        self._dataStartIndex = newDataStartIndex

def main():
    help(CircularArray)
    print("See the docstrings?")
    print("Notice that private methods have not been listed.")
    print()

    print("Creating CircularArray with 9:")
    c = CircularArray([9])
    c._print()
    print()

    print("Appending 4:")
    c.append(4)
    c._print()
    print()

    print("Pre-appending 23:")
    c.preappend(23)
    c._print()
    print()

    print("Pre-appending 66:")
    c.preappend(66)
    c._print()
    print()

    print("Appending 8:")
    c.append(8)
    c._print()
    print()

    print("Removing last item:")
    c.removeLast()
    c._print()
    print()

    print("Removing first item:")
    c.removeFirst()
    c._print()
    print()

    print("Removing first item:")
    c.removeFirst()
    c._print()
    print()

    print("Removing item at index 1:")
    c.remove(1) 
    c._print()
    print()

    print("Appending 9:")
    c.append(9)
    c._print()
    print()

    print("Appending 4:")
    c.append(4)
    c._print()
    print()

    print("Removing item at index 2:")
    c.remove(2) 
    c._print()
    print()
    
    print("Insert 38 at index 1:")
    c.insert(1,38)
    c._print()
    print()

    print("Insert 67 at index 2:")
    c.insert(2,67)
    c._print()
    print()

    print("Inserting 8 at index 0:")
    c.insert(0,8)
    c._print()
    print()

    print("Accessing all items by the index:")
    for i in range(len(c)):
        print(c[i], " ", end="")
    print()

    print("Iterating over array:")
    for item in c:
        print(item, " ", end="")
    print()
    print()

    print("Testing 'repr' through 'print':")
    print(c)
    print()

    print("Creating copy through eval(repr(...)) and testing ==:")
    c2=eval(repr(c))
    c2._print()
    print(c==c2)


main()
    
