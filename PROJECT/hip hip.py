for row in range(1,8):

   for col in range(1,8):

      if col==7 or col==1 or (row==4 and( col<7 and col>1)) :

        print("*",end="")

      else:

        print(end=" ")

   print()

print()

for row in range(1,8):

  for col in range (1,8):

    if row==1 or row==7 or (col==4 and (row>1 and row<8)):                 

     print("*",end="")

    else:

     print(end=" ")

  print()
print()

for row in range(1,8):

  for col in range (1,8):

    if (row==1 and (col>1 and col<8)):                 
        print("*",end="")
    
    elif (col==1 and (row>=1 and row<8)):
        print("*",end="")
    
    elif (col==7 and(row>1 and row<5)):
        print("*",end="")

    elif (row==4 and (col>1 and col<7)):                 
        print("*",end="")

    else:
        print(end=" ")

  print()
print()
print('\n')

print('\n')

for row in range(1,8):

   for col in range(1,8):

      if col==7 or col==1 or (row==4 and( col<7 and col>1)) :

        print("*",end="")

      else:

        print(end=" ")

   print()

print()

for row in range(1,8):

  for col in range (1,8):

    if row==1 or row==7 or (col==4 and (row>1 and row<8)):                 

     print("*",end="")

    else:

     print(end=" ")

  print()
print()

for row in range(1,8):

  for col in range (1,8):

    if (row==1 and (col>1 and col<8)):                 
        print("*",end="")
    
    elif (col==1 and (row>=1 and row<8)):
        print("*",end="")
    
    elif (col==7 and(row>1 and row<5)):
        print("*",end="")

    elif (row==4 and (col>1 and col<7)):                 
        print("*",end="")

    else:
        print(end=" ")

  print()
print()
print('\n')
for row in range(1,8):

   for col in range(1,8):

      if col==7 or col==1 or (row==4 and( col<7 and col>1)) :

        print("*",end="")

      else:

        print(end=" ")

   print()
print()

for row in range(1,8):

   for col in range(1,8):

      if col==7 or col==1 or (row==7 and( col<7 and col>1)) :

        print("*",end="")

      else:

        print(end=" ")

   print()
print()

for row in range(1,8):

  for col in range (1,8):

    if (row==1 and (col>1 and col<8)):                 
        print("*",end="")
    
    elif (col==1 and (row>=1 and row<8)):
        print("*",end="")
    
    elif (col==7 and(row>1 and row<5)):
        print("*",end="")

    elif (row==4 and (col>1 and col<7)):                 
        print("*",end="")

    elif (row==5 and col==2):
        print("*",end="")
    elif (row==6 and col==3):
        print("*",end="")
    elif (row==7 and col==4):
        print("*",end="")
    else:
        print(end=" ")
  print()
print()

for row in range(1,8):

  for col in range (1,8):

    if (row==1 and (col>1 and col<8)):                 
        print("*",end="")
    
    elif (col==1 and (row>=1 and row<8)):
        print("*",end="")
    
    elif (col==7 and(row>1 and row<5)):
        print("*",end="")

    elif (row==4 and (col>1 and col<7)):                 
        print("*",end="")

    elif (row==5 and col==2):
        print("*",end="")
    elif (row==6 and col==3):
        print("*",end="")
    elif (row==7 and col==4):
        print("*",end="")
    else:
        print(end=" ")
  print()
print()

for row in range(1,8):

   for col in range(1,8):

      if col==7 or col==1 or (row==1 and( col<7 and col>1)) :

        print("*",end="")

      elif (row==4 and( col<7 and col>1)) :
        print("*", end="")

      else:

        print(end=" ")

   print()
print()
   
for Row in range(0,8):    
    for Col in range(0,8):     
        if (((Col == 1 or Col == 5) and Row < 2) or Row == Col and Col > 0 and Col < 4 or (Col == 4 and Row == 2) or ((Col == 3) and Row > 3)):  
            print("*", end="")    
        else:      
            print(end=" ")        
    print();    
print()