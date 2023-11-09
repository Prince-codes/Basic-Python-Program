import os.path


def n_file():
    fn=input("Enter a name to your file : ")
    z=".txt"
    nf=fn+z
    
    f = open(nf, "w")
    f.close()
    print("\nYour file is successfully created....\n")

def w_file():
    fn=input("Enter your file name : ")
    z=".txt"
    nf=fn+z
    if os.path.isfile(nf):
            
            f=open(nf,'a')
            while True:
                    q=input("Want to enter text (Y/N) : ")
                    if q=='y' or q=='Y':
                        e=input("Enter text to write : ")
                        f.write(e)
                        f.write('\n')
                        print("\nYour data is written successfully....\n")
                        break
                    else:
                        f.close()
                        break
    else:
         print("This file doesnt exist.")
         print("Try again\n")
         w_file()
         

def enc_file():
    fn=input("Enter your file name : ")
    z=".txt"
    nf=fn+z
    if  os.path.isfile(nf):
            f=open(nf,'r')
            r=f.read()
            f.close()

            f=open(nf,'w')
            for c in r:
                c=str(ord(c))+' ' 
                f.write(c)
            print("\nYour File is Encrypted successfully....\n")
            print("You can check.")
    else:
         print("This file doesnt exist.")
         print("Try again\n")
         enc_file()

def dec_file():
    fn=input("Enter your file name : ")
    z=".txt"
    nf=fn+z
    if os.path.isfile(nf):
           
            f=open(nf,'r')
            r=f.read()
            f.close()

            l=r.split()
            f=open(nf,'w')
            f.write(''.join(chr(int(i)) for i in l))

            print("\nYour File is Decrypted successfully....\n")
            print("You can check.")
    else:
         
         print("This file doesnt exist.")
         print("Try again\n")
         dec_file()


print(" "*40,"Welcome\n")
print("\nPlease Create a File before Encryption/Decryption\n")
while True:
    print("\nEnter 1: To Create a file")
    print("Enter 2: To write data on your file")
    print("Enter 3: TO Encrypt your File")
    print("Enter 4: To Decrypt your File")
    print("Enter 0: To Exit\n")
    try:
         
        a=int(input("Enter your Choice : "))

        if a==1:
            n_file()
        elif a==2:
            w_file()
        elif a==3:
            enc_file()
        elif a==4:
            dec_file()
        elif a==0:
            print("\nThank you For Using\n")
            break
        
    except:
         print("Try again.")
         continue