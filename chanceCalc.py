from random import randint
import time


total = 500
bet = 1
cycles = 0;

while(1):

    randomNum = randint(0, 100)
    print("bet: ", bet)
    #time.sleep(1)
    cycles += 1

    if(randomNum < 48):
        print("WON")
        total += (bet *2)
        bet = 1
    else:
        print("LOST")
        total -= bet
        bet = bet * 2

        if (total <= 0 ):
            print("LOST THE GAME")
            print("cycles: ", cycles)
            break

    print("total: ", total)
