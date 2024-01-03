from tkinter import*
window=Tk()


#Fungsi button
def fungsinya():
    Hasil.configure(text=txtfld.get())
    
    
btn=Button(window, text="This is Button widget", fg='blue',command=fungsinya)
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60,y=50)
txtfld= Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

Hasil = Label(window, bg="red", width=17, bd=5)
Hasil.place(x=80, y=200)

window.title('Hello Python')
window.geometry("300x400+10+10")
window.mainloop()



    
