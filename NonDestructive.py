#! /usr/bin/env python3

# Bezawit Woldegebriel
# Non-Destructive list
# April 18, 2015

class Node(object):
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next
        
#-------------------------------------------------------------------------------
    
class List(object):
    def __init__(self):
        self._nodes = None

    def isEmpty(self):
        return self._nodes == None
        
    def cons(self, item):
        l = List()
        l._nodes = Node(item, self._nodes)
        return l

    def first(self):
        if not self.isEmpty():
            return self._nodes._data
        else:
            raise Exception

    def rest(self):
        if not self.isEmpty():
            l = List()

            l._nodes = self._nodes._next
            return l
        else:
            raise Exception
    
#--------------------------------------------------------------------------------

def member(item, aNonDistList):
    if aNonDistList is aNonDistList.isEmpty():
       raise Exception
    if item == aNonDistList.first():
        print("FOUND")
        return True
    else:
        return member(item, aNonDistList.rest())

def member2(item, aList):
    if aList == []:
        raise Exception
    if item == aList[0]:
        print("FOUND")
        return True
    else:
        return member2(item, aList[1:])

def makeNonDistList(n):
    current = List()
    for i in range(1, n+1):
        current = current.cons(i)
    return current        

def makePythonList(n):
    bList = []
    for i in range (n+1):
        bList.append(i)
    return bList

def main():
    aList = makePythonList(500)
    nondist = makeNonDistList(500)

    member(500, nondist)
    member2(500, aList)

main()

# Observation
# The functions member and member2 search for the last element of their
# respective types of lists. If they found the item, they would print out
# 'FOUND'. makeNonDistList, and makePythonList create a non-distructive
# and a typical Python list respectfully.From the test run in main(),
# it looks like non-distructive lists take a shorter time than Python's
# for searching the last items of their list's.

