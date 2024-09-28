import random

def assess(num,guess):
    hint=''
    for i in range(len(str(guess))):
        if  str(guess)[i] in str(num):
            if str(num)[i]==str(guess)[i]:
                hint+= ' Fermi'
            else: hint+= ' Pico'
        else: hint+=' '
    if hint=='   ': print("Bagels")
    elif(hint==' Fermi Fermi Fermi'): 
        print('You got it!',hint)
        return 'win'
    else: print(hint)


def bagels():
    print('''
    Bagels a deductive logic game.
<<<<<<< HEAD
    I am thinking of a 3-digit number. Try to guess what it is.
=======
    By Al Sweigart al@inventwithpython.com
    'I am thinking of a 3-digit number. Try to guess what it is.
>>>>>>> ffc9d503e87a0a22e0401acdcb5ab8f4c9189e9b
        Here are some clues:
        When I say:    That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position
        Bagels      No digit is correct
    I have thought up a number.\n    You have 10 guesses to get it.''')
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
        if continuePlaying=='no' : 
            print('Thank you for playing, See you!')
            break
bagels()
