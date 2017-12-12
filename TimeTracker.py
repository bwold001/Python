import sys
from tkinter import filedialog
from tkinter import *
import time, datetime
from math import *

def loginpage():

    def myentry():
        musr = usrname.get()
        root.destroy()
        return mainpage()

    def mysign():
        mpass = passwrd.get()
        root.destroy()
        return loginpage()
        pass
        return

    
    root = Tk()
    usrname = StringVar()
    passwrd = StringVar()               

    root.geometry("450x450+200+200") #Create window 450x450
    root.title("Time Tracker")

    userlabel = Label(text='Username').place(x=100, y=150)  #create label
    passlabel = Label(text='Password').place(x=100, y=180)

    mlogin = Entry(root, textvariable=usrname).place(x=170, y=150) #create entry box
    mpass = Entry(root, textvariable=passwrd).place(x=170, y=180) 

    logbut = Button(root,text='Login', command=myentry)
    logbut.place(x=150, y=220)
    signbut = Button(root,text='Sign Up', command=mysign)
    signbut.place(x=220, y=220)


    root.mainloop()


time1 = ''

def mainpage():

    def nNew():
        nlabel=Label(text='You clicked New').pack()
        return
    
    def nAbout():
        messagebox.showinfo(title="About", message='Time Tracker Tool \n Version 1.0')
        return
    
    def mExit():
        mQ = messagebox.askyesno(title="Exit", message="Are you sure?")
        if mQ > 0:
            root.destroy()
            return

    def nOpen():
        
        fileName = filedialog.askopenfilename(filetypes=(("", "*.py"),("All files", "*.*")))
        contents = open(fileName, "r")
        
        m.insert(END, contents)

    def savefile():

        savefile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        
        if savefile is None:
            return
        texttosave= str(m.get(1, END))
        savefile.write(texttosave)
    
    def start():
        global  strthr, strtmin, strtsec, starttime
        act = activity.get()

        starttime =time.time()

        showstarttime = time.strftime('%H:%M:%S')
        strthr = int(time.strftime('%H'))
        strtmin = int(time.strftime('%M'))
        strtsec= int(time.strftime('%S'))
        
        m.insert(END, act, 'Start time: ',showstarttime)


    def stop():
        global  endtime
        global  elapsed
        
        endtime = time.time()
        showendtime = time.strftime('%H:%M:%S')

        
        endhr = int(time.strftime('%H'))
        endmin = int(time.strftime('%M'))
        endsec= int(time.strftime('%S'))

        duration = endtime-starttime
        showduration = str(datetime.timedelta(seconds=int(duration)))
        
        m.insert(END, 'End time: ', showendtime)
        m.insert(END, 'Activity duration: ', showduration)
        

    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2, anchor=N)
        clock.after(200, tick)



    root = Tk() 
    root.geometry("450x450+200+200")
    root.title("Time Tracker")
    
    
    #Menu construction

    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='New', command=nNew)
    filemenu.add_command(label='Open', command=nOpen)
    filemenu.add_command(label='Save', command=savefile)
    filemenu.add_command(label='Save As...')
    filemenu.add_command(label='Exit', command = mExit)
    menubar.add_cascade(label='File', menu=filemenu)

    #Edit Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Undo')
    filemenu.add_command(label='Redo')
    filemenu.add_command(label='Copy')
    filemenu.add_command(label='Paste')
    menubar.add_cascade(label='Edit', menu=filemenu)

    # Display Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='View as table')
    filemenu.add_command(label='View as PDF')
    filemenu.add_command(label='Exit')
    menubar.add_cascade(label='Display', menu=filemenu)

    #Options Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Customise')
    filemenu.add_command(label='Add manually')
    filemenu.add_command(label='Save As')
    filemenu.add_command(label='Exit')
    menubar.add_cascade(label='Options', menu=filemenu)

    #Help Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Help Docs')
    filemenu.add_command(label='About', command=nAbout)
    menubar.add_cascade(label='Help', menu=filemenu)

    root.config(menu=menubar)

    activity = StringVar()

    #Display current time

    clock = Label(font=('times', 20, 'bold'))
    clock.pack(fill=BOTH, expand=1)

    tick()


    #Create field for activity entry
    activ = Label(text='Activity:').place(x=100, y=75)
    mactiv = Entry(textvariable=activity).place(x=150, y=75)

    #Record buttons
    startbut = Button(root,text='Start', command=start).place(x=150, y=110)
    pausebut = Button(root,text='Stop', command=stop).place(x=240, y=110)

    #save = Button(root, text='Save',command=save).place(x=190, y=110)

    #Display box & scrollbar
    scrollbar = Scrollbar(root, orient=VERTICAL)
    m = Listbox(root,selectmode=EXTENDED, width=30,height = 10, yscrollcommand=scrollbar.set)
    m.pack(side=LEFT, fill=BOTH, expand=1, pady=1, padx=1)
    scrollbar.config(command=m.yview)
    scrollbar.pack(side=RIGHT, fill=Y) 

   
    root.mainloop()



#loginpage()
mainpage()



