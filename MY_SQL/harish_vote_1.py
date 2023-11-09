import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog as fd
import sqlite3 as sqltor
conn=sqltor.connect('main.db') #main database
cursor=conn.cursor() #main cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS poll
                    (name)""")
def pollpage(): #page for polling
     def proceed():
        answer=messagebox.askokcancel(title="Confirmation",message="You sure?")
        if answer:
            chose=choose.get()
            print(chose)
            command='update polling set votes=votes+1 where name=?'
            pd.execute(command,(chose,))
            pd.commit()
            ppage.destroy()
            messagebox.showinfo('Success!','You have voted')
            pollpage()
        else:
            pollpage()
            
     choose=StringVar()
     names=[]
     pd=sqltor.connect(plname+'.db') #poll database
     pcursor=pd.cursor() #poll cursor
     pcursor.execute('select name from polling')
     data=pcursor.fetchall()
     for i in range(len(data)):
         data1=data[i]
         ndata=data1[0]
         names.append(ndata)
     print(names)
     ppage=Toplevel(takefocus = True)
    
     ppage.resizable(False,False)
     ppage.geometry("600x480")
     ppage.geometry("+%d+%d" %(380,80))
     
     ppage.title('Poll')
     var=IntVar()
     main_frame=Frame(ppage)
     main_frame.pack(fill=BOTH,expand=1)
     #creating a canvas
     my_canvas=Canvas(main_frame,bg="white")
     my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
     #add a scrollbar to the Canvas
     my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
     my_scrollbar.pack(side=LEFT,fill=Y)
     #cofigure the canvas
     my_canvas.configure(yscrollcommand=my_scrollbar.set)
     my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
     #create ANother frame in canvas
     second_frame=Frame(my_canvas,bg="white")
     my_canvas.create_window((0,0),window=second_frame,anchor="nw")
  
     
     for i in range(len(names)):
         Label(second_frame,text=i+1,font=("Serif",20,"bold"),background="white").grid(row=i,column=0)
      
         Radiobutton(second_frame,text=f"              {names[i]}               ",value=names[i],variable=choose,font="Arial 20 bold",indicatoron=0,command=proceed,activebackground="white").grid(row=i,column =3,sticky = W,pady=5,padx=5)
         
        
def polls(): #mypolls
    def proceed():
        global plname
        plname=psel.get()
        if plname=='-select-':
            return messagebox.showerror('Error','select poll')
        else:
             
            mpolls.destroy()
            pollpage()
    cursor.execute('select name from poll')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    psel=StringVar()
    mpolls=Toplevel()
    mpolls.attributes("-topmost", True)
    mpolls.geometry("+%d+%d" %(300,200))
    mpolls.resizable(False,False)
    mpolls.title('Voting Program')
    Label(mpolls,text='Select Poll',font='Helvetica 12 bold').grid(row=1,column=3)
    select=ttk.Combobox(mpolls,values=pollnames,state='readonly',textvariable=psel)
    select.grid(row=2,column=3)
    select.current(0)
    ttk.Button(mpolls,text='Proceed',command=proceed).grid(row=2,column=4)
def create():
    def proceed():
        global pcursor
        pname=name.get() #pollname
        can=cname.get()   #candidatename
        if pname=='':
            return messagebox.showerror('Error','Enter poll name')
        elif can=='':
            return messagebox.showerror('Error','Enter candidates')
        else:
            candidates=can.split(',') #candidate list
            command='insert into poll (name) values (?);'
            cursor.execute(command,(pname,))
            conn.commit()
            pd=sqltor.connect(pname+'.db') #poll database
            pcursor=pd.cursor() #poll cursor
            pcursor.execute("""CREATE TABLE IF NOT EXISTS polling
                 (name TEXT,votes INTEGER)""")
            for i in range(len(candidates)):
                command='insert into polling (name,votes) values (?, ?)'
                data=(candidates[i],0)
                pcursor.execute(command,data)
                pd.commit()
            pd.close()
            cr.destroy()
            messagebox.showinfo('Success!','Poll Created')  
    passs=simpledialog.askstring("Admin","                Type in the password.              ") 
    if passs==op:
            name=StringVar()
            cname=StringVar()
            cr=Toplevel()
            cr.attributes("-topmost", True)
            cr.geometry("+%d+%d" %(300,200))
            cr.resizable(False,False)
            cr.title('Create a new poll')
            Label(cr,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=2)
            Label(cr,text='Enter Poll name: ').grid(row=2,column=1)
            Entry(cr,width=30,textvariable=name).grid(row=2,column=2) #poll name
            Label(cr,text='(eg: captain elections)').place(x=354,y=25)
            Label(cr,text='Enter Candidates: ').grid(row=5,column=1)
            Entry(cr,width=45,textvariable=cname).grid(row=5,column=2) #candidate name
            Label(cr,text='Note: Enter the candidate names one by one by putting commas').grid(row=6,column=2)
            Label(cr,text='eg: candidate1,candidate2,candidate3....').grid(row=7,column=2)
            ttk.Button(cr,text='Proceed',command=proceed).grid(row=15,column=6)
    
def quits():
    passs=simpledialog.askstring("Quit","                Type in the password.              ")
    if passs==op:
        home.destroy()
    elif passs==None:
         return     
    elif passs!=op:
         messagebox.showerror("Retry","Wrong Password")
         quits()
def selpl(): #pollresults
    def results():
             sel=sele.get()  #selected option
             if sel=='-select-':
                 return messagebox.showerror('Error','Select Poll')
             else:
                 passs=simpledialog.askstring("Admin_Results","                Type in the password.              ")
                 if passs==op:
                    pl.destroy()
                    
                    res=Toplevel() #result-page
                    
                    res.attributes("-topmost", True)
               
                    res.geometry("+%d+%d" %(300,200))
                    res.title('Results!')
                    con=sqltor.connect(sel+'.db')
                    pcursor=con.cursor()
                    pcursor.execute('select * from polling')
                    r=pcursor.fetchall() #data-raw
                    main_frame=Frame(res)
                    main_frame.pack(fill=BOTH,expand=1)
                    #creating a canvas
                    my_canvas=Canvas(main_frame,bg="white")
                    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                    #add a scrollbar to the Canvas
                    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                    my_scrollbar.pack(side=LEFT,fill=Y)
                    #cofigure the canvas
                    my_canvas.configure(yscrollcommand=my_scrollbar.set)
                    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                    #create ANother frame in canvas
                    second_frame=Frame(my_canvas,bg="white")
                    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                    for i in range(len(r)):
                        data=r[i]
                        Label(second_frame,text=data[0]+': '+str(data[1])+' votes',font="Arial 14 bold",background="white").grid(row=2+i,column=6)
                    
                      
    cursor.execute('select name from poll')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    sele=StringVar()
    pl=Toplevel()
    pl.attributes("-topmost", True)
    pl.geometry("+%d+%d" %(300,200))
    pl.resizable(False,False)
    pl.title('Voting System')
    Label(pl,text='Select Poll',font='Helvetica 12 bold').grid(row=1,column=1)
    sel=ttk.Combobox(pl,values=pollnames,state='readonly',textvariable=sele)
    sel.grid(row=2,column=1)
    sel.current(0)
    ttk.Button(pl,text='Get Results',command=results).grid(row=2,column=2)
op="007"
home=Tk()
home.attributes("-fullscreen",True)
home.geometry("1440x900")
home.title('Election')

#logo
mp=PhotoImage(file="x.png")
p_label=Label(home,image=mp)
p_label.pack(side=TOP)
home["bg"]="white"
Label(home,text='VIDYA JYOTI SCHOOL',font=("Arial black",40,'bold'),bg='white').pack()

l1=Label(home,text="Button 1 for Voting pannel",font="Calibri 24 bold").pack()
ss=Button(home,text='Polls',command=polls, width=25,padx=20,pady=15, bg='green',fg='white').pack()

l4=Label(home,text="Button 2 to Create new Poll",font="Calibri 24 bold").pack()

aa=Button(home,text='Create new Poll +',command=create, width=25,padx=20,pady=15, bg='green',fg='white').pack()

l2=Label(home,text="Button 3 for Results",font="Calibri 24 bold").pack()
ww=Button(home,text='Poll Results',command=selpl, width=25,padx=20,pady=15, bg='green',fg='white').pack()

l3=Label(home,text="Button 4 to Exit",font="Calibri 24 bold").pack()
qu=Button(home,text="Quit",command=quits, width=25,padx=20,pady=15, bg='green',fg='white').pack()
mtxt=Label(home, text="Copyright © 2023 SILENCE | PRESENTED BY : CODEWORLD.UNAUX.COM",font="Calibri 14 bold").pack(side=BOTTOM, anchor="se")
home.mainloop()