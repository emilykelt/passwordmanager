#python backend

#MODULES
import random
from lists import * #words and common

#FUNCTIONS

def generatePassword():
    
    #local variables
    generated = ['']*3
    password = ''

    #generate three word password and add on num/ special characters inbetween
    
    #generate words
    for i in range(len(generated)):
        generated[i] = (words[random.randint(0,len(words)-1)]).capitalize()
        
    #add them to password
    for i in range(len(generated)):
        password += generated[i]
        
        for x in range(random.randint(0,3)):
            password += chr(random.randint(48,57))

    #makes sure password is greater than 12 characters
    if len(password) < 12:
        for x in range(12-len(password)):
            password += chr(random.randint(48,57))
            
    return password

def validatePass(password):

    valid = False
    
    while valid == False:
        # Checks if password generated matches any common passwords                                                         
        if any(common in password.lower() for common in common):        # and regenerates it if it does
            password = generatePassword()
        else:
            valid = True
    return password

def timeTaken(password):
    #update to make sure its accurate
    length = len(password)
    ways = (26*2 + 21)  ** length
    seconds = ways / 1000000000     # assuming a password cracker can attempt 1bn passwords per second
    days = seconds / 86400          # 86400 seconds in a day
    years = days / 365              # 365 days in a year, not including leap days

    timeToCrack = round(years,2)
    
    return timeToCrack


#MAIN
media = str(input("What is the password going to be used for? : "))

for i in range(10):
    password = validatePass(generatePassword())
    print(password)
print(timeTaken(password))


