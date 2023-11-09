from tkinter import *
root=Tk()

root.geometry("644x344")

Label(root, text="Welcome", font="comicsansms 13 bold").grid(row=0, column=3)

name=Label(root, text="Name")
phone=Label(root, text="Phone")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)

nameval=StringVar()
phoneval=IntVar()

nameentry= Entry(root, textvariable=nameval)
phoneentry= Entry(root, textvariable=phoneval)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)




root.mainloop()