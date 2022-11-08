#!/bin/python3
def dictpractice():
    answers = {}
    answers['name'] = input("What is your name?:")
    answers['age'] = int(input("How old are you?:"))
    answers['colour'] = input("what is your favorite color?:").upper()
    answers['like'] = input("Do you like Python?:").upper()
    answers['flat'] = input("The world is flat: True or False?:").upper()
    print("hello", answers['name'], "nice to meet you :)")
    print(answers['age'], "is quite the year, itsn't it?")
    if answers['colour'] == 'PURPLE' :
        print("you really chose a great colour!")
    else:
        print("Hmmm,", answers['colour'], "is nice, but purple is nicer ;P")
    if answers['like'] == 'YES' :
        print("I agree, python is pretty cool")
    else:
        better = input("well what language do yo prefer?:")
        print("To each their own,", better, "sounds like it could be cool")
    if answers['flat'] == 'FALSE' :
        print("Phew, I'm glad we don't need to address the flat earth stuff")
    else:
        print("Oh man, here are some resources you should read...")

dictpractice()
