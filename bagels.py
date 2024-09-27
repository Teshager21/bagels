import random

def assess(num,guess):
    hint=''
    for i in range(len(str(guess))):
        if  str(guess)[i] in str(num):
            if str(num)[i]==str(guess)[i]:
                hint+= ' Fermi'
            else: hint+= ' Pico'
        else: hint+=' '
    if hint=='': print("Bagels")
    elif(hint==' Fermi Fermi Fermi'): 
        print('You got it!',hint)
        return 'win'
    else: print(hint)
    print(num)


def bagels():
    print('Bagels a deductive logic game.\nBy Al Sweigart al@inventwithpython.com')
    print('I am thinking of a 3-digit number. Try to guess what it is.')
    print('Here are some clues:\nWhen I say:    That means:\n Pico        One digit is correct but in the wrong position.')
    print(' Fermi       One digit is correct and in the right position')
    print(' Bagels      No digit is correct')
    print('I have thought up a number.\n    You have 10 guesses to get it.')
    status='loss'
    while True:
        num= random.randint(100,999)
        counter=0
        while(counter<10):
            guess=int(input(f'Guess#{counter+1}\n'))
            while not 100<=guess<=999: 
                print('The number must be three digits')
                guess=int(input(f'Guess#{counter+1}\n'))
            if assess(num,guess)=='win': 
                status='win'
                break
            counter+=1
        if status=='loss' :print(f"You lost this round!, The correct number was {num}")
        continuePlaying= input('Would you like to continue playing: (yes/no)').lower()
        if continuePlaying=='no' : break
bagels()
