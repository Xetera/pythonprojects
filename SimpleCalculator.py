# name: Ali
# date: 06/07/2016
# description: calculator that lets you choose from 4 different operations using 2 given numbers
# issues: overflow issue on exponential operations.

import time
def add(a, b):
    print "Adding %d + %d" % (a, b)
    sleep(1)
    return a + b


def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    sleep(1)
    return a - b


def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    sleep(1)
    return int(a * b)


def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    sleep(1)
    return a / b

def power(a, b):
    print "Calculating %d ^ %d" %(a, b)
    sleep(1)
    return a**b

def print_result(operationResult):
    print "Your answer is %r" % operationResult

def sleep(multiplier):
    time.sleep(0.7*multiplier)


def valueError ():
    print "You did not enter a number."
    sleep(1)

def numberInput():
    while True:
        try:
            global promptNumber1
            promptNumber1= int(raw_input("Enter your first number.\n"))
            break
        except ValueError:
            valueError()
            continue
    while True:
        try:
            global promptNumber2
            promptNumber2 = int(raw_input("Enter your second number.\n"))
            break
        except ValueError:
            valueError()
            continue
        except ZeroDivisionError:
            print "You can't divide by zero."
            sleep(1)
            continue

print "*Multiplication (M) \n*Division (D) \n*Addition (A) \n*Subtraction (S)\n*Exponential (E)"
while True:
    print "Choose your desired operation."

    operationAnswer = raw_input("> ")
    if operationAnswer == "M":
        try:
            print "You have chosen multiplication, %r." % operationAnswer
            numberInput()
            operationResult = multiply(promptNumber1,promptNumber2)
            print_result(operationResult)
        except ValueError:
            valueError()
            continue
    elif operationAnswer == "D":
        try:
            print "You have chosen division, %r." % operationAnswer
            numberInput()
            operationResult = divide(promptNumber1, promptNumber2)
            print_result(operationResult)
        except ValueError:
            valueError()
        break
    elif operationAnswer == "A":
        try:
            print "You have chosen addition, %r." % operationAnswer
            numberInput()
            operationResult = add(promptNumber1, promptNumber2)
            print_result(operationResult)
        except ValueError:
            valueError()
    elif operationAnswer == "S":
        try:
            print "You have chosen subtraction, %r." % operationAnswer
            numberInput()
            operationResult = subtract(promptNumber1, promptNumber2)
            print_result(operationResult)
        except ValueError:
            valueError()
    elif operationAnswer == "E":
        try:
            print "You have chosen an exponential operation."
            numberInput()
            operationResult = power(promptNumber1, promptNumber2)
            print_result(operationResult)
        except ValueError:
            valueError()
    else:
        print "This is not a valid input"
        continue
    yesPrompt = raw_input("Any more operations? (y/n)")
    if yesPrompt == "n":
        print "Goodbye..."
        break
    elif yesPrompt == "y":
        continue
    else:
        print "Please type either 'y' or 'n'"

