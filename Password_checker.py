 #importing modules , these are inbuilt modules from python
import random #to get random chars in a password
import string #to produce all ascii letters
import time #to use sleep function


from tkinter import * #for GUI
import os.path #to check whether the file exist or not
#=======================================================
#defining variables just to be safe
tmp=""  
password=""
#====================================================
#defining functions
# 1.Click function , this is a button's function to check whether the input string is correct or not.
def click():
    global User
    user=pass_entry.get()
    
    if user==password:
        
        for i in range(1,4):
             print("Checking"+"."*i)
             time.sleep(0.5)
        print("Logged in Succesfully")
        window.destroy()
        print("Lets pretend that you logged in ok")
        print(";)")
        
        
        
    else:
        print("Invalid Password")
        print("You might wanna generate new password.")
# this is a button's function to generate new password.
def gen():
     pass_gen()
     print("New Password Generated.")
     print("you can try again now.")

#this is a function to perform GUI, It opens a dialogue box and ask for Password and after verifying it disappears......thats it for now :/      
          
def wind():
        global window

        window=Tk()
        window.config(background="black")
        global  instruct_label
        instruct_label=Label(window,text="Enter the password",bg="black",fg="#00FF00")
        instruct_label.pack(side=TOP)
        global  pass_entry
        global  sub_button
        global gen_button
        gen_button=Button(window,text='Gen',command=gen,bg="black",fg="#00FF00",activeforeground="#00FF00",activebackground="black")

        pass_entry=Entry(window,bg="black",fg="#00FF00",show="*")
        pass_entry.pack(side=LEFT)
        sub_button=Button(window,text="Submit",command=click,bg="black",fg="#00FF00",activeforeground="#00FF00",activebackground="black")
        gen_button.pack(side=RIGHT)
        sub_button.pack(side=RIGHT)
        
        window.mainloop()
       

#this Function's role is to generate new password with random module and write them in a txt file called passes.txt 
def pass_gen():
    global password
    password=""
    tmp=""
    tmp = random.choices(string.ascii_letters+string.digits, k=8)
    for i in tmp:
        password+=i
   
    f=open("passes.txt","a")
    f.write(f"\n{password}")#password\n was giving me error some of the times :(
    f.close()

#this is the main loop which calls all the function.
# the main thing in this is that it makes a new file if there isnt before.
# and they update the password with the latest line in passes.txt.

while True:
        if not os.path.isfile('passes.txt'):
             pass_gen()
        
        f=open("passes.txt",'r')
        lines=f.readlines()
        f.close()
        password=lines[-1]
        print("Enter the password in the dialogue box.")
        print("Click gen to generate a new password.")
        wind()
        break

       #("Thanks for checking this prototype of an idea.")
        #("There will be more updates on this soon.")