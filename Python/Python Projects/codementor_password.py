import string
import random
import time

# This is an exercise from the codementor website.
# The code generates a password after asking the user questions about the required composition of the password - how long, how many letters and how many numbers. 
# There should be a mix of upper and lower case letters and at least 6 characters. 

# I decided to restrict password length to 12 characters and mandate at least one symbol.
# I used string and random methods to create samples of x length for the different components of the password.
# Another option would be to iterate over a password string, appending chars x times.
# I would like to include error handling in this (eg prevent floats being entered), need to revisit this! 
# Next step is to think about test data. Can set up a database and call into an array?

"""
Name: passwordGenerator
Inputs: strings to hold password length "length", number of letters "letters" and number of numbers "numbers"
Outputs: string "passwordString"
Preconditions:  6<=length=>12, (letters + numbers + 1)<=length (where 1 represents at least one symbol)
Postconditions: the password contains randonly generated characters and composition and length is as defined by the user

Initial insights
- the function is called with a call with no argument
- a dialogue asks the user how long the password should be and saves to "length" variable
- a dialogue asks the user how many letters they want and saves to "letters" variable, checks if the numbers are possible and catches input errors. 
- a dialogue asks the user how many numbers they want and saves to "numbers" variable, checks if the numbers are possible and catches input errors. 
- the code calculates number of symbol chars

- use string methods to set up strings containing all of the possible letters, numbers and symbols. 
- use random.sample() to save to a list random characters from each string, number of each required from letters, numbers and symbols vars. 
- a while loop checks that the letters list contains both upper and lower case chars
- concatenate the three lists into one, use random.shuffle() to mix up the component parts and convert to a string. 

"""

def passwordGenerator():
    #set up variables to manage the number of characters the user can request at each stage
    lengthOk = False
    lettersOk = False
    numbersOk = False
    symbolsOk = False
    password = ""
    #enter the length of the password. Do not exit the loop until the entered number is within bounds.
    length = int(input("Hi. This is the password generator. How long would you like your password to be? Enter a whole number between 6 and 12 please: "))
    while lengthOk == False:
        if(length<6 or length>12):
            print ("Sorry - please make sure your password is a whole number between 6 and 12.")
        else:
            print("Great, thanks.")
            lengthOk = True
        
    #enter the number of letters in password.
    #Must be 2 or more as we need at least one uc and one lc,  and not greater than pasword length -2 to allow at least one number and one symbol.
    #Do not exit loop until condition is met       
    while lettersOk == False:
        letters = int(input("Now, let us know how many letters you want in your password:  "))
        if(letters <=1 or letters >(length-2)):
            print("Sorry -please make sure the number of letters is greater than 1 and less than", length-1)
        else:
            print("Great, thanks. Got the number of letters!")
            lettersOk = True
            
    #enter the number of numbers in password.
    #Must be >=1 and not greater than pasword length - letters - 1 to allow at least one symbol to be added
    #Do not exit loop until condition is met       
    while numbersOk == False:
        numbers = int(input("Now, let us know how many numbers you want in your password:  "))
        if(numbers <=0 or numbers >(length-letters-1)):
            print("Sorry -please make sure the number of numbers is greater than 0 and less than", length-letters)
        else:
            print("Great, thanks. Got the number of numbers!")
            numbersOk = True
    
    # now calculate how many symbols
    symbols = length-letters-numbers
    print("There will also be", symbols, "symbols in your password")
    

   # now to generate the password.
   # use String methods to put all of each sort of character in a suitably named list  
    allLetters= string.ascii_letters
    allNumbers = string.digits
    allSymbols = string.punctuation
    
    #take a random sample of the right size and save into letterList
    print("Now adding", letters, "letters to the password")
    #while loop to repeat creation of list until it meets mixed case condition
    mixed = False
    while mixed == False:
        letterList = random.sample(allLetters, letters)
        letterString =''.join(letterList)
    #if the chars are not all upper and not all lower
        if(letterString.isupper()==False) and (letterString.islower()==False):
            mixed = True
    print("Letters chosen at random:",letterList)
    
    #take a random sample of the right size and save into numberList
    print("Now adding", numbers, "numbers to the password")
    numberList = random.sample(allNumbers, numbers)

    print("Numbers chosen at random:",numberList)
 
    
    #take a random sample of the right size and save into symbolList
    print("Now adding", symbols, "symbols to the password")
    symbolList = random.sample(allSymbols, symbols)

    print("Symbols chosen at random:",symbolList)

    
    #now build and shuffle the password list then convert to string
    passwordList = letterList + numberList + symbolList
    print(passwordList)
    random.shuffle(passwordList)
    print("Shuffled password list is", passwordList)
    
    #now convert the list to a string with no spaces
    passwordString = ''.join(passwordList)
    print("Password string is:", passwordString)
    

print(passwordGenerator())




