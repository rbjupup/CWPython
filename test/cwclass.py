from tkinter import *
import time
from tkinter import filedialog 

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
        
        
    def side_example():
        windows = Tk()
        frame = Frame(windows)
        frame.pack()
        
        label = Label(frame,text = 'name')
        label.pack(side = 'left' )
        entry = Entry(frame)
        entry.pack(side = 'left')
        
        windows.mainloop()
        
        
    def side_grid_example():
        '''rowspan columnspan use line num'''
        windows = Tk()
        frame = Frame(windows)
        frame.pack()
        
        label = Label(frame,text = 'name')
        label.grid(row = 0, column = 0)
        entry = Entry(frame)
        entry.grid(row = 1, column = 1)
        
        windows.mainloop()
        
        
    def cross(text):
        text.insert(INSERT,'x')
    def ctl_MulityLineEdit_example():
        window = Tk()
        frame = Frame(window)
        frame.pack()
        
        text = Text(frame,height = 3,width = 10)
        text.pack()
        
        button = Button(frame,text = 'add',command = lambda:cwclass.cross(text))
        button.pack()
        
        window.mainloop()
        

    def ctl_checkBox_example():
        window = Tk()
        frame = Frame(window)
        frame.pack()
              
        red = IntVar()
        blue = IntVar()
        green = IntVar()
        
        for (name,var) in (('R',red),('G',green),('B',blue)):
            check = Checkbutton(frame,text = name,variable = var)
            check.pack(side = 'left')
        def recolor(window,r,g,b):
            color = '#'
            for var in (r,g,b):
                color += 'FF' if var.get() else '00'
            window.config(bg = color)      
        label = Label(frame,text = '[    ]')
        button = Button(frame,text = 'Update',
                        command = lambda:recolor(label,red,green,blue))
        button.pack(side = 'left')
        label.pack(side = 'left')
        
        window.mainloop()   
        
    def ctl_menu_example():
        def save(root,text):
            data = text.get('0.0',END)
            filename = filedialog.asksaveasfilename(
            parent = root,
            filetype = [('text','*.txt')],
            title = 'save as ...')
            writer = open(filename,'w')
            writer.write(data)
            writer.close()
            
        def quit(root):
            root.destory()
        window = Tk()
        text = Text(window)
        text.pack()
        
        menubar= Menu(window)
        filemenu = Menu(menubar)
        filemenu.add_command(label = 'save',command = lambda:save(window,text))
        filemenu.add_command(label = 'quit',command = lambda:quit(window))
        
        menubar.add_cascade(label = 'File',menu = filemenu)
        window.config(menu = menubar)
        
        window.mainloop()
            
        