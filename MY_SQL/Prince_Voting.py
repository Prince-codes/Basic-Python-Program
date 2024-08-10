import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
# Admin Password
pas="4321"
# connect to MySQL database
db = mysql.connector.connect( host="localhost", user="root", password="1234", database="election" )
# create a cursor
cursor = db.cursor()
# function to store vote
def vote(candidates_name):
    cursor.execute("INSERT INTO votes (candidates_name) VALUES (%s)", (candidates_name,))
    db.commit()
    print("Your vote for", candidates_name, "has been stored. \n")
# function to show the total number of votes for each Candidate
def get_vote_count():
    passs=simpledialog.askstring("Admin","Type in the Password")
    if passs==pas:
        pw=Tk()
        pw.title("RESULT PANNEL")
        cursor.execute("SELECT candidates_name, COUNT(*) as count FROM votes GROUP BY candidates_name")
        results = cursor.fetchall()
        for row in results:
            Label(pw,text=f"{row[0]} : {row[1]} votes",font="Calibri 28 bold").pack()
            print()
        pw.mainloop()
    elif passs==None:
         return
    elif passs!=pas:
         messagebox.showerror("Retry","Wrong Password")
         get_vote_count()
def qui():
    passs=simpledialog.askstring("Admin","Type in the Password")
    if passs==pas:
        win.destroy()
    elif passs==None:
        return
    elif passs!=pas:
        messagebox.showerror("Retry","Wrong Password")
        qui()
# #Main Programs :-
def vote_call():
            root=Tk()
            root.geometry("1440x900")
            root.attributes("-fullscreen",True)
            root.title("WELCOME IN VOTING PANNEL")
            #title
            hed=Label(root,text="VIDYA JYOTI SCHOOL",font="Calibri 32 bold", pady=20)
            hed.pack()
            hed=Label(root,text="ELECTING POST : PRESIDENT",font="Calibri 16 bold")
            hed.pack()
            txt=Label(root, text="Please Proceed Voting :-",font="Calibri 24 bold",pady=25)
            txt.pack(anchor="nw")
            txty=Label(root, text="Copyright © 2023 SILENCE | PRESENTED BY : CODEWORLD.UNAUX.COM",font="Calibri 14 bold")
            txty.pack(side=BOTTOM, anchor="se")
            cmbobox=ttk.Combobox(root,state="readonly",width=25, font="Verdana 16 bold")
            cmbobox["values"]=("Prince raj Singh","Harish","Ayush Gorai","Mohit Prahdhan","Krishna gope","Anshuman Tiwari")
            cmbobox.pack()
            def push():
                if cmbobox.get()=="":
                    root.destroy()
                    vote_call()
                else:
                    vote(cmbobox.get())
                    messagebox.showinfo('Success!',f" You have voted : {cmbobox.get()}")
                    root.destroy()
                    vote_call()
            submit=Button(root,text="VOTE",command=push,width=25,pady=15,background='green',fg='white').pack()
            button = tk.Button(root,background='black',fg='white', text='End Voting', width=25,padx=10,pady=10, command=root.destroy)
            button.pack(side=BOTTOM, anchor="sw")
            root.mainloop()
win=Tk()
win.attributes("-fullscreen",True)
win.geometry("1440x900")
win.title("HOME")
#logo
mp=PhotoImage(file="x.png")
p_label=Label(win,image=mp)
p_label.pack(side=TOP)
#title
mhed=Label(win,text="VIDYA JYOTI SCHOOL",font="Calibri 32 bold").pack()
#Main buttons
l1=Label(win,text="Button 1 for Voting ",font="Calibri 24 bold").pack()
b1=Button(win,text='Vote',command=vote_call, width=20,padx=10,pady=10,background='green',fg='white').pack()
l2=Label(win,text="Button 2 for Results",font="Calibri 24 bold").pack()
b2=Button(win,text="Results",command=get_vote_count, width=20,padx=10,pady=10,background='green',fg='white').pack()
l3=Label(win,text="Button 3 to Exit",font="Calibri 24 bold").pack()
b3=Button(win,text="Exit",command=qui, width=20,padx=10,pady=10,background='green',fg='white').pack()
#creidts
mtxt=Label(win, text="Copyright © 2023 SILENCE | PRESENTED BY : CODEWORLD.UNAUX.COM",font="Calibri 14 bold").pack(side=BOTTOM, anchor="se")
win.mainloop()
# close the database
db.close()