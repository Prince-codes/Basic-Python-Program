import random as r
print('='*100)
print(' '*35,"WELLCOME EMPLOYEE MANAGEMENT",' '*36)
print('='*100)

eid=1000
mp=2    #manager post
lp=10   #labour post available 
el=[]    #employee list
ed=[]    #employee detail
pl=[]    #to store payment detail
adpass=1234
while True:  

    print("\nENTER 1 : TO NEW EMPLOYEEMENT")
    print("ENTER 2 : OFFICE")
    print("ENTER 3 : EXIT\n")

    ch=int(input("ENTER YOUR CHOICE : "))

    if ch==1:
        while True:
            print("\nENTER 1 : POST AVAILABLE")
            print("ENTER 2 : EMPLOYEE LOGIN")
            print("ENTER 3 : EXIT\n")

            ch2=int(input("ENTER YOUR CHOICE : "))

            if ch2==1:
                while True:
                    print("\nENTER 1 : TO APPLY FOR MANAGER POST")
                    print("ENTER 2 : TO APPLY FOR LABOUR")
                    print("ENTER 3 : EXIT\n")

                    ch3=int(input("ENTER YOUR CHOICE : "))

                    if ch3==1:   
                        if mp>0:

                            n=input("ENTER YOUR NAME : ")
                            pn=int(input("ENTER YOUR PHONE NUMBER : "))
                            dob=input("ENTER YOUR AGE  : ")
                            eid=r.randint(1000,9999)

                            ed=[n,pn,dob,eid,'MANAGER']
                            el.append(ed)
                            mp-=1

                            print(f"\nYOUR EMPLOYEE ID IS '  {eid}  ' KEEP THIS FOR FUTURE REFFERENCE")
                            print("\n...................YOUR DATA HAS BEEN STORED...................\n")

                            if len(pn)!=10:
                                print("\nYOUR PHONE NUMBER CONTAINS LESS OR MORE DIGIT..................\n")
                                break

                            else:
                                continue
                    
                            
                        else:
                            print("\n.................NO POSTS ARE AVAILABLE................\n")
                            break
                    
                    elif ch3==2:
                        
                        if lp>0:
                            n=input("ENTER YOUR NAME : ")
                            pn=int(input("ENTER YOUR PHONE NUMBER : "))
                            dob=input("ENTER YOUR AGE  : ")
                            eid=r.randint(1000,9999)
                            ed=[n,pn,dob,eid,"LABOUR"]
                            el.append(ed)
                            lp-=1

                            print(f"\nYOUR EMPLOYEE ID IS '  {eid}  ' KEEP THIS FOR FUTURE REFFERENCE")
                            print("\n...................YOUR DATA HAS BEEN STORED...................\n")


                            if len(pn)!=10:
                                print("\nYOUR PHONE NUMBER CONTAINS LESS OR MORE DIGIT..................\n")
                                break

                            else:
                                continue
                    
                            
                        else:
                            print("\n.................NO POSTS ARE AVAILABLE................\n")
                            break
                        
                    elif ch3==3:
                        break
                    
                    else:
                        print("\n.........WRONG INPUT__RETRY.........\n")

            elif ch2==2:
                nm=input("ENTER YOUR REGESTERED NAME : ")
                eeid=int(input("ENTER YOUR EMPLOYEE ID : "))
                for i in el:
                    if i[3]==eeid and i[0]==nm:
                        print("\n..............YOUR DATA IS PRESNT..............\n")
                        break
                    else:
                        print("\n..............DATA NOT FOUND..............\n")
                        break
            
            elif ch2==3:
                break
            
            else:
                print("\n..............WROND INPUT-RETRY..............\n")

    elif ch==2:
        paswd=int(input("ENTER PASSWORD : "))
        if paswd==adpass:

            print('='*30)
            print("-----------wecome-----------")
            print('='*30)

            print("\nENTER 1 : TO GET DEATAIL OF EMPLOYEES")
            print("ENTER 2 : TO DISTRIBUTE PAYMENTS")
            print("Enter 3 : TO GET ALL PAYMENT DISTRIBUTION DETAIL")
            print("ENTER 4 : TO LOGOUT\n")

            ac=int(input("ENTER YOUR CHOICE : "))

            if ac==1:

                print("Name","Phone Number","Age","Employee id","Post",sep='\t')
                for i in el:
                    print(i[0],i[1],i[2],i[3],i[4],sep='\t')


            elif ac==2:

                p=int(input("Enter employee id to proceed with payments : "))

                for i in el:

                    if p==i[3]:

                        s=int(input("Enter amount to be paid : "))
                        print("\nPayment paid sucessfull\n")
                        pl.append(p)
                    else:
                        print("\nNOT A VALID EMPLOYEE ID.................\n")

            elif ac==3:
                for i in pl:
                    print("Payements done on these employee-id's : ")
                    print(i)

            elif ac==4:
                break

            else:
                print("\nWRONG INPUT\n")
    elif ch==3:
        print(".........SUCCESSFULLY LOGED-OUT.........")
        break

    else:
        print("\nWRONG INPUT..........\n")              