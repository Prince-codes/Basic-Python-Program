import time
pas='1234'

# Timer module
def countdown(t): 



        while t: 

            mins, secs = divmod(t, 60) 

            timer = '{:02d}:{:02d}'.format(mins, secs) 

            print(timer, end="\r") 

            time.sleep(1) 

            t -= 1

#set accordingly to lock
t = 10 


#Passworf entering module
def pa():
    pa=input("Enter password : ")
    return pa


a=0

while True:

    x=pa()

    if x!=pas:
        a+=1

        if a==3:
             countdown(t)
             a=0