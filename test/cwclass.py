from tkinter import *
import time

class cwclass(object):
    def ctl_edit_example():
        print("test of edit")
    def ctl_label_example():
        window = Tk()
        label = Label(window,text = "test label")
        label.pack()   
        time.sleep(2)
        label.config(text = "test change")
        window.mainloop()     
    def var_label_example():
        window = Tk()
        data = StringVar()
        data.set("data to display")
        label = Label(window,textvariable = data)
        label.pack()   
        window.mainloop()     
    def ctl_Frame_example():
        window = Tk()
        frame = Frame(window)
        frame.pack()
        first = Label(frame,text = "first")
        first.pack()
        second = Label(frame,text = "second")
        second.pack()
        third = Label(frame,text = "third")
        third.pack()
        window.mainloop()
    def ctl_Entry_example():
        window = Tk()
        data = StringVar()
        data.set("data to display")
        label = Label(window,textvariable = data)
        label.pack()   
        entry = Entry(window,textvariable = data)
        entry.pack()
        window.mainloop()     
    
    def click_add_diff(var,val):
        var.set(var.get() + val)
    def ctl_button_example():
        window = Tk()
        counter = IntVar()
        counter.set(0)
        frame = Frame(window)
        frame.pack()
        buttonup = Button(frame,text = "Up",command = lambda:cwclass.click_add_diff(counter,1))
        buttonup.pack()
        buttondown = Button(frame,text = "Down",command = lambda:cwclass.click_add_diff(counter,-1))
        buttondown.pack()
        label = Label(frame,textvariable = counter)
        label.pack()
        window.mainloop()    
    def Look_feel_example():
        window = Tk()
        button = Button(window,text = "helllo",font = ('Courier',14,"bold italic"),
                        bg = "green",fg =  "white")
        button.pack()
        window.mainloop()
            
        