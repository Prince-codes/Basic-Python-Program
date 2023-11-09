#snake water gun game

import random
import time as t

while True:
    print('1:"Snake", 2:"Water", 3:"Gun", 0:"To Exit"\n')
    ci=random.randint(1,3)          #computer input
    ui=int(input("Enter your choice : "))      #user input
    if ci==1:
        t.sleep(1)
        print("\nComputer get's SNAKE\n")

        if ui==1:
            print("\nDraw..........\n")

        elif ui==2:
            print("\nComputer wins..........\n")

        elif ui==3:
            print("\nUser wins..........\n")

    elif ci==2:
        t.sleep(1)
        print("\nComputer get's WATER\n")

        if ui==1:
            print("\nUser wins...........\n")

        elif ui==2:
            print("\nDraw..........\n")

        elif ui==3:
            print("\nComputer wins..........\n")

    elif ci==3:
        t.sleep(1)
        print("\nComputer get's GUN\n")
        if ui==1:
            print("\nComputer wins..........\n")

        elif ui==2:
            print("\nUser wins...........\n")

        elif ui==3:
            print("\nDraw..........\n")

    elif ui==0:
        t.sleep(1)
        print("\nThank you8 for using...........\n")
        break
    else:
        t.sleep(1)
        print("\nWrong Input....\n")