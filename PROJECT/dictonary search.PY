d={}
l=[]
for i in range (5):
    ke=input("Enter names : ")
    val=int(input("Enter marks : "))
    print('\n')
    d[ke]=val

#appending dictionary values in list.
for key in d.keys():
    l.append(d[key])

#checking palindrome number and appending in new list
for i in l:
    temp=i
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
        if (temp==rev and temp>50):
            print(temp)
