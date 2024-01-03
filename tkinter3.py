#Membuat form login
from tkinter import*
TkObject = Tk()

#Membuat widget label header
Header = Label(TkObject, text="Login Here")
#Memasukkan label header kedalam Grid
Header.grid(columnspan=2)

#Membuat widget label serta entry untuk username dan password
label1 = Label(TkObject, text="Username")
label2 = Label(TkObject, text="Pasword")
Entry1 = Entry(TkObject)
Entry2 = Entry(TkObject)

#Memasukkan widget label dan entry dari username dan password ke dalam grid
label1.grid(row=2, column=0, sticky=E)
label2.grid(row=3, column=0, sticky=E)
Entry1.grid(row=2, column=1)
Entry2.grid(row=3, column=1)

#Membuat widget check button
check = Checkbutton(TkObject, text="Remember me")
# Memasukkan widget check button kedalam grid
check.grid(row=4, columnspan=2)

#Membuat widget button
button = Button(TkObject, text="Login")
#Memasukkan widget button ke dalam grid
button.grid(row=5, columnspan=2)
#Menjalankan program
TkObject.mainloop()


