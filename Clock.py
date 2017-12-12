import sys
from tkinter import *
import time

the_time=''

class Window(Frame):
    def __init__(self,master):
        super(Window,self).__init__(master)
        self.grid()
        self.create_widgets() 

    def create_widgets(self):

        #Create a hello button:
        hey=self.hellobttn=Button(self,text="Hey")
        self.hellobttn.grid(row=0, column=0)

        #Create a label that displays time:
        self.display_time=Label(self, text=the_time)
        self.display_time.grid(row=1, column=1)

        def change_value_the_time():
            global the_time
            newtime = time.strftime('%H:%M:%S')
            if newtime != the_time:
                the_time= newtime
                self.display_time.config(text=the_time, font="40")
            self.display_time.after(20, change_value_the_time)

        change_value_the_time()

root=Tk()
root.title("Test")
root.geometry("200x200")
app=Window(root)
root.mainloop()
