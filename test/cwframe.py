from tkinter import *
def change(widget,colors):
    new_val = '#'
    for name in ('red' , 'green' , 'blue'):
        new_val += colors[name].get()
    widget['bg'] = new_val

window = Tk()
frame = Frame(window)
frame.pack()

colors = {}
for (name, col) in (('red','#FF0000'),
                    ('green','#00FF00'),
                    ('blue','#0000FF')):
    colors[name] = StringVar()
    colors[name].set('00')
    entry =Entry(frame,textvariable = colors[name],bg = col,fg = "white")
    entry.pack()
current = Label(frame, text = '   ' , bg = "#FFFFFF")
current.pack()
update = Button(frame,text = 'Update',command = lambda:change(current,colors))
update.pack()
mainloop()
    