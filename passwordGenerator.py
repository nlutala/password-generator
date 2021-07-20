import random
import string

characters = str(1234567890) + string.ascii_letters + "!£$%&@#?"

def checkNumber(userInput):
    '''
        parameter: userInput (a string)
        Checks whether the input has entered a valid value (an integer).
    '''
    try:
        integer = int(userInput) * 1
        return integer
    except:
        TypeError
        return -1
        # Returned as it is a number that will not work when passed to the 
        # generatePassword(integer) function

def containsNumber(password):
    '''
        parameter: password (a string)
        return True if the password generated contains a number.
    '''
    for i in range(0,len(password)):
        try:
            return int(password[i]) * 1 == int(password[i])
        except:
            ValueError
            continue
    return False

def generatePassword(integer):
    '''
        parameter: integer (a whole number to indicate how many
                   characters the user wants their generated
                   password to be)
        Generates a random password between 6 and 15 characters.
    '''
    password = ""
    if checkNumber(integer) >= 6 and checkNumber(integer) <= 15:
        for i in range(checkNumber(integer)):
            password += characters[random.randint(0, len(characters)-1)]
        if containsNumber(password) == True:
            print("\nYour generated password is: " + password + "\n")
        else:
            password = password[0:len(password)-1] + str(random.randint(0,9))
            print("\nYour generated password is: " + password + "\n")
    else:
        print("Please enter a number between 6 and 15.\n")

print("To generate a random password, enter a number between 6 and 15 e.g. '7'")
isDone = False
while True:
    try:
        amountOfChars = int(input("Please enter the amount of characters for your password: "))
        generatePassword(amountOfChars)
    except:
        TypeError
        print("\nThere was an error. Please try again.\n")
    finally:
        while isDone == False:
            userInput = input("Do you want to generate a new password? Enter 'yes' (y) or 'no' (n): ")
            if userInput.upper() == "YES" or userInput.upper() == "Y":
                isDone = True
                continue
            elif userInput.upper() == "NO" or userInput.upper() == "N":
                isDone = True
                input("Press the Enter key to quit ")
                exit()
            else:
                print("There was a problem with your input.\n")
        isDone = False