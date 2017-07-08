# name: Ali
# date: 07/07/2016
# description: small program that lets you choose between flipping a coin and rolling dice with sides
# and roll amounts controlled. Im

import random
import time

coinordice = ""
randomnumber = 0
userchoicerolls = 1
totalheads = 0
totaltails = 0
cumulativeheads = 0 # remove this when implementing on discord
cumulativetails = 0 # remove this when implementing on discord
def generatenumber(randomY):
    global randomnumber
    global iteratingroll
    global totalheads, cumulativeheads
    global totaltails, cumulativetails
    randomnumber = random.randint(1, randomY)
    if randomnumber == 1:
        totalheads += 1
        cumulativeheads += 1
        print "Flip %d >  Heads"%iteratingroll
    else:
        totaltails += 1
        cumulativetails += 1
        print "Flip %d >  Tails "%iteratingroll
    iteratingroll += 1
    time.sleep(0.08)


def generatenumberprint(randomX):
    global randomnumber
    global iteratingroll
    randomnumber = random.randint(1, randomX)
    print "roll %d >   %d" %(iteratingroll, randomnumber)
    iteratingroll += 1
    time.sleep(0.08)


def rollamounts(userchoicerolls, functiontype, userchoicesides): #rollamounts(#ofrolls,type of function being called, #of sides)
    global i
    global iteratingroll
    iteratingroll = 1
    for i in range(userchoicerolls):
        functiontype(userchoicesides)

def cleartotals(): #eval function for resetting cum. statistics in discord
    cumulativetails = 0
    cumulativeheads = 0

while coinordice != "coin" and coinordice != "dice":
    coinordice = raw_input("Coin flip or dice roll? (coin,dice)")
    if coinordice == "dice":
        while True:
            try:
                userchoicesides = int(raw_input("How many sided die?\n> "))
                break
            except ValueError:
                print "Not a valid input"
                continue
        while True:
            try:
                userchoicerolls = int(raw_input("How many rolls?\n> "))
                break
            except ValueError:
                print "Not a valid input"
                continue
        rollamounts(userchoicerolls, generatenumberprint, userchoicesides)

    elif coinordice == "coin":
        while True:
            try:
                flipamounts = int(raw_input("How many coin flips?"))
                rollamounts(flipamounts, generatenumber, 2)
            except ValueError:
                print "Please enter a number."
            print "Heads fliped = %d"%totalheads
            print "Tails flipped = %d"%totaltails
            print "Total amount of heads flipped = %d" % cumulativeheads
            print "Total amount of tails flipped = %d" % cumulativetails
            returnprompt = raw_input("Flip again? (y/n)")
            if returnprompt == "y":
                totaltails = 0
                totalheads = 0
                continue
            else:
                break
    else:
        print "Please enter 'coin' or 'dice'."
        continue