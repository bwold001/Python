# /usr/bin/env python3

# Bezawit Woldegebriel
# 30 bouncing balls

from random import *
from graphics import*
class Ball:
    def __init__ (self, win):
        
        self.dx = randrange(1,5)
        self.dy = randrange(1,5)
        c1 = Circle(Point(randrange(win.getWidth()),
                          randrange(win.getHeight())),5)
        c1.draw(win)
        self.c1 = c1
        self.win = win
      
    def move (self):
        self.c1.move(self.dx, self.dy)
                
        if self.c1.getCenter().getX()< 0 :
            self.dx *= -1
        elif self.c1.getCenter().getX() > self.win.getWidth():
            self.dx *= -1
        if self.c1.getCenter().getY() < 0:
            self.dy *= -1
        elif self.c1.getCenter().getY() > self.win.getHeight():
            self.dy *= -1     
         
def main():
    win = GraphWin("Bouncing balls", 400, 400)
       
    balls =[Ball(win)]
    
    for i in range(30):
       balls.append(Ball(win))
    while True:
       for ball in balls:
           ball.move()

        
main()

    
