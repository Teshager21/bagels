import random
def bagels():
    print('Bagels a deductive logic game.\nBy Al Sweigart al@inventwithpython.com')
    print('I am thinking of a 3-digit number. Try to guess what it is.')
    print('Here are some clues:\nWhen I say:    That means:\n Pico        One digit is correct but in the wrong position.')
    print(' Fermi       One digit is correct and in the right position')
    print(' Bagels      No digit is correct')
    num= random.randint(100,999)
    print('I have thought up a number.\n    You have 10 guesses to get it.')
    counter=0
    while(counter<10):
        print(f'Guess#{counter+1}')
        guess=input()
        counter+=1
    print(num)
bagels()