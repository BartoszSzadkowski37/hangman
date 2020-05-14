# hangman Python 3
# MAIN POINTS
# PASSWORD SHOULD BE STORE IN SOME FILE, USER CAN ADD NEW PASSWORD FROM THE PROGRAM LEVEL
# USER CAN PRINT AMOUNT OF PASSWORDS
# USER CAN PLAY IN HANGMAN

# MAIN MENU

# WELCOME IN HANGMAN GAME
# 1. PLAY HANGMAN
# 2. ADD NEW PASSWORD
# 3. DISPLAY PASSWORDS AMOUNT 


# 1. PLAY HANGMAN
# RANDOMIZE PASSWORD AND DISPLAY
# GET LETTERS FROM THE USER
# IF CORRECT --> CHANGE SIGN, ELSE --> DISPLAY THE HANGMAN

# IMPORT MODULES
import shelve
import pyinputplus as pyip

# FUNCTIONS
def printMenu():
    print('\n')
    print('1. PLAY HANGMAN')
    print('2. ADD NEW PASSWORD')
    print('3. DISPLAY PASSWORDS AMOUNT')
    print('4. EXIT')
    print('\n')

game = True

menuChoice = ''


while game:
    printMenu()
    menuChoice = pyip.inputChoice(['1', '2', '3', '4', 'PLAY HANGMAN', 'HANGMAN', 'ADD NEW PASSWORD', 'NEW PASSWORD', 'PASSWORD', 'ADD PASSWORD', 'DISPLAY PASSWORDS AMOUNT', 'DISPLAY PASSWORDS', 'DISPLAY', 'EXIT'], prompt='')
    print(menuChoice)
    if menuChoice == '4' or menuChoice == 'EXIT':
        game = False
    elif menuChoice == '2' or menuChoice == 'ADD NEW PASSWORD', 'NEW PASSWORD', 'PASSWORD', 'ADD PASSWORD':
        newPassword = inputStr('Provide new password: ')
