#! /usr/bin/env python3

# Bezawit Woldegebriel
# Dartboard

from graphics import *
from random import *

def circle(o1,o2,rad):
    return Circle(Point(o1,o2), rad)
    
def getnumthrows():
    throws = int(input("How many darts should be thrown? "))
    return throws
    
def darts(p1,p2, window):
    darts = Circle(Point(p1,p2), 0.001)
    darts.draw(window)

def randompoint():
    return 2 * random() - 1

def land(x,y):
    return (x*x)+(y*y)

def gray(circle):
    circle.setFill('grey')

def green(circle):
    circle.setFill('green')
    
def red(circle):
    circle.setFill('red')

def pi(hits,throws):
    return 4 * hits / throws

def output(hits,throws,pie):
    print("Based on", hits, "hits out of", throws,
          "darts, pi is about", pie)

def mouseclick(win):
    win.getMouse()
    win.close()

def main():

    win = GraphWin("Darts", 500, 500)
    win.setCoords(-1,-1,1,1)

    board = circle(0, 0, 1)
    board.draw(win)
    gray(board)
    throws = getnumthrows()
    hits = 0

    for i in range(throws):
        x = randompoint()
        y = randompoint()
        
        onedart = Circle(Point(x,y), 0.01)
        onedart.draw(win)
        
        if land(x,y) <= 1:
            green(onedart)
            hits = hits + 1
            
        else:
            red(onedart)
            
    pie = pi(hits,throws)
    output(hits,throws,pie) 
    mouseclick(win)
    print()
    
main()



    



    
