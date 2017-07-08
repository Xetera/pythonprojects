# name: Ali
# date: 07/08/2016
# description: guessing game for a randomly generated number. not retardproof
# issues: lacks module for setting difficulty, if implemented needs a way to
#         scale the gettlingclose() function parameters accordingly but i
#         can't be bothered to math
#
import random

guesstimes = 0
generatednumber = True
totalwins = 0
def generaterandom (difficulty): #implementing difficutly later
    global randomnumber
    randomnumber = random.randint(1,difficulty)

def gettingclose():
    if (10 >= guess - randomnumber > 0) or (
                    10 >= randomnumber - guess > 0):
        print "But you're getting close!\n"
    else:
        pass

def gettingreallyclose():
        if (5 > guess - randomnumber > 0) or (5 > randomnumber - guess > 0):
            print "YOU'RE GETTING INCREDIBLY CLOSE!\n"

        else:
            gettingclose()
            pass

print "\n\nWelcome to the number guessing game."
print "A random number will be generated that you have to guess."

while True:
    generaterandom(100)
    randomnumberstr = str(randomnumber)
    generatednumber = True
    print "\nWould you like to enable noob mode? (y/n)"
    print "This will let you see the first digit of the number."
    easymode = raw_input("> ")
    if easymode == "y":
        print "The number you're guessing starts with a %r " % randomnumberstr[:1]
    else:
        pass
    while generatednumber == True:
        guess = int(raw_input("Guess the number\n"))
        guesstimes += 1
        if guess < randomnumber:
            print "Your guess is too low."
            gettingreallyclose()
            continue
        elif guess > randomnumber:
            print "Your guess is too high."
            gettingreallyclose()
            continue
        else:
            totalwins += 1
            print "You win!"
            if easymode == 1:
                print "But you're kind of a noob"
            else:
                pass
            if guesstimes == 1:
                print "You got it on your first guess."
            else:
                print "You guessed the number in %d tries."%guesstimes
            print "Total victories = %d."%totalwins
        guesstimes = 0
        playagain = raw_input("Play again? (y/n)")
        if playagain == "y":
            generatednumber = False
            continue
        else:
            break
        break