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
import random

# FUNCTIONS

# this function randomize password from DB and return this password
def randomizePassword():
    randomPassword = ''
    passwordsDB = shelve.open('passwords')
    if 'passwords' not in list(passwordsDB.keys()):
        print('Passwords DB is empty')
    
    else:
        randomPassword = passwordsDB['passwords'][random.randint(0, len(list(passwordsDB['passwords'])) - 1)]
    
    passwordsDB.close()
    return randomPassword

# this function takes password as argument and hash it and return secret password
def hidePassword(password):
    secretPassword = ''
    for i in range(len(password)):
        if password[i] != ' ':
            secretPassword += '_'
        else:
            secretPassword += ' '
    return secretPassword

# this function check user answer with password, if correct change secretPassword element for this answer and return True, else return False 
def checkAnswer(password, hidePassword, answer):
    
    correct = False    
    for i in range(len(password)):

        if password[i] == answer.upper():
            hidePassword[i] = answer.upper()
            correct = True

    return correct

def playHangman():
    # randomize password and hide it
    password = randomizePassword()
    password = password.upper()
    secretPassword = hidePassword(password)

    game = True

    # amount of mistakes
    mistakes = 0

    printHangman(mistakes)
    print(secretPassword)

    answersAppeared = []


    # main loop when mistakes will be more than 5 game over
    while game:

        userAnswer = pyip.inputStr('Provide letter: ')
        userAnswer = userAnswer.upper()
        # if userAnswer was not in answers which have already appeard, append it by this answer
        if userAnswer not in answersAppeared:
            answersAppeared.append(userAnswer)

        # change secretPassword to list, because function cannot change string ref by value, 
        secretPassword = list(secretPassword)
        # function checking answer and assign True or False to the correct var
        correct = checkAnswer(password, secretPassword, userAnswer)

        # if answer was incorrect, mistakes amount increase by one
        if correct == False:
            mistakes += 1

        # back secretPassword to string
        secretPassword = ''.join(secretPassword)
        
        printHangman(mistakes)
        print(secretPassword)
        print('This letters you provided: ', answersAppeared)
        print('Chances you have left: ', 6 - mistakes)

        if secretPassword == password:
            print('Congratulations! You win!')
            game = False

        if mistakes > 5:
            print('You loooose')
            game = False
        

def printHangman(mistakes):
    if mistakes == 0:
      print(''' 
**************
*            |
*
*
*
*
*
*
*
************************
                ''')
    elif mistakes == 1:
        print(''' 
**************
*            |
*            @
*
*
*
*
*
*
************************
                ''')

    elif mistakes == 2:
        print(''' 
**************
*            |
*            @
*            |
*
*
*
*
*
************************
                ''')

    elif mistakes == 3:
        print(''' 
**************
*            |
*            @
*           /|
*
*
*
*
*
************************
                ''')

    elif mistakes == 4:
        print(''' 
**************
*            |
*            @
*           /|\\
*
*
*
*
*
************************
                ''')

    elif mistakes == 5:
        print(''' 
**************
*            |
*            @
*           /|\\
*           /
*
*
*
*
************************
                ''')
    elif mistakes == 6:
        print(''' 
**************
*            |
*            @
*           /|\\
*           / \\
*
*
*
*
************************
                ''')
def addNewPassword():
    # this function get password from the user and add to passwords database
    passwordsDB = shelve.open('passwords')
    newPassword = pyip.inputStr('Provide new password: ')
    # check if passwords key in DB exist, if no create it
    if 'passwords' not in list(passwordsDB.keys()):
        passwordsDB['passwords'] = []
        # add new password
    temp = passwordsDB['passwords']
    temp.append(newPassword)
    passwordsDB['passwords'] = temp
    print('Passwords database has been updated')
    passwordsDB.close()    

def printMenu():
    print('\n')
    print('1. PLAY HANGMAN')
    print('2. ADD NEW PASSWORD')
    print('3. MANAGE PASSWORDS')
    print('4. EXIT')
    print('\n')

    '''
    MANAGE PASSWORDS
    1. SHOW PASSWORDS LIST
    2. ASK IF YOU WANT TO DELETE SOME PASSWORD? (Y/N)
    3. IF YES PROVIDE PASSWORD TO DELETE
    4. 

    '''

def managePasswords():
    print('\n')
    # Open shelve file and check if passwords DB exist
    passwordsDB = shelve.open('passwords')
    if 'passwords' not in list(passwordsDB.keys()):
        print('Passwords DB is empty')
    else:
        # if exist print numbered list of passwords
        for i in range(len(list(passwordsDB['passwords']))):
            print(i + 1, passwordsDB['passwords'][i])
        # ask if delete some password
        ifDelete = pyip.inputYesNo('Do you want to delete some password?')
        if ifDelete == 'yes':
            # get number of password to delete
            passwordDel = pyip.inputInt('Provide number of password to delete: ', min = 0, max = len(list(passwordsDB['passwords'])))
            # it has to be temp value used because deleting on original shelve value doesn't work
            temp = passwordsDB['passwords']
            del temp[passwordDel - 1]
            passwordsDB['passwords'] = temp
        print('Passwords database has been updated')

    passwordsDB.close()


game = True

menuChoice = ''


while game:
    printMenu()
    menuChoice = pyip.inputChoice(['1', '2', '3', '4', 'PLAY HANGMAN', 'HANGMAN', 'ADD NEW PASSWORD', 'NEW PASSWORD', 'PASSWORD', 'ADD PASSWORD', 'DISPLAY PASSWORDS AMOUNT', 'DISPLAY PASSWORDS', 'DISPLAY', 'EXIT'], prompt='')
    if menuChoice == '4' or menuChoice == 'EXIT':
        game = False
    elif menuChoice == '2' or menuChoice == 'ADD NEW PASSWORD' or menuChoice == 'NEW PASSWORD' or menuChoice == 'PASSWORD' or menuChoice == 'ADD PASSWORD':
        addNewPassword()
    elif menuChoice == '3' or menuChoice == 'MANAGE PASSWORDS' or menuChoice == 'MANAGE':
        managePasswords()
    elif menuChoice == '1' or menuChoice == 'PLAY' or menuChoice == 'HANGMAN' or menuChoice == 'PLAY HANGMAN':
        playHangman()
