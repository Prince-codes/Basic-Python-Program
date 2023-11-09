for i in range(1, 10):
    for j in range(1, 10):
        if (i == 1 or i == 9 or j == 1 or j == 9):
            print('5', end=' ')
        elif (i==2 or i==8 or j==2 or j==8):
            print('4', end=' ')
        elif (i==3 or i==7 or j==3 or j==7):
            print('3', end=' ')
        elif (i==4 or i==6 or j==4 or j==6):
            print('2', end=' ')
        else:
            print('1',end=' ')
    print()