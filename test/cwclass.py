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
        