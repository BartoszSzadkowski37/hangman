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
