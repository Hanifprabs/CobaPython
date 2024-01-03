from tkinter import*
import tkinter as tk
from tkinter import ttk

window =Tk()
        
def my_upd(*args):
    Entry.config(text=var.get() +' :'+str(cb.current()))
def my_insert():
    if Entry.get() not in cb['values']:
        cb['values'] +=(Entry.get(),)
        Entry.delete(0,'end')
def my_delete():
    my_new=[]
    for opt in cb['values']:
        if (opt!= cb.get()):
            print(opt)
            my_new.append(opt)
    cb['values']=my_new
    cb.delete(0,'end')
    
data=["one","two","three","four"]

var= StringVar()
var.set(data[0])

cb=ttk.Combobox(window,values=data,textvariable=var)

label1= Label(window,text="Number")
label1.place(x=20,y=150)

Entry= Entry(window,bg="yellow")
Entry.place(x=70,y=150)

button1=Button(window,text="Add",command=lambda:my_insert())
button1.place(x=150,y=210)
button2=Button(window,text="Delete",command=lambda:my_delete())
button2.place(x=100,y=210)
cb.set("search")
cb.bind('<<ComboboxSelected>>')
cb.pack()
cb.place(x=70, y=180)



lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

def showSelected():
    number= []
    cnumber=lb.curselection()
    for i in cnumber:
        op =lb.get(i)
        number.append(op)
    for val in number:
        print(val)

v0=StringVar()
button = Button(window, text="Show Selected", command=showSelected)
button.place(x=250,y=240)

r1=Radiobutton(window, text="male",variable=v0,value=1)
r2=Radiobutton(window, text="female",variable=v0,value=2)
r1.place(x=100,y=50)
r2.place(x=180,y=50)


v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window,text = "Football",variable = v1)
C2 = Checkbutton(window,text = "Tennis",variable = v2)
C1.place(x=100,y=100)
C2.place(x=180,y=100)

var.trace('w',my_upd)
window.title('Hello Python')
window.geometry("400x400+10+10")
window.mainloop()
