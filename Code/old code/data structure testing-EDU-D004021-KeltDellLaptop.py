#MODULES
import random
from lists import * #words and common, from another file

#THE CLASS STRUCTURE(S)

#TODO: Potentially master username/password and inherit username into class password
class superLogin():
    def __init__(self):
        self._username = ""
        self._password = ""

    #getters
    def getUsername(self):
        return self._username
    
    def getPassword(self):
        temp = ''
        temp = self._password 
        return temp 
    
    #setters
    def setUsername(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    #polymorphism custom print function
    def __str__(self):
        outputstring = ""
        outputstring += str(self._username) + " " + str(self._password)
        return outputstring
    

class Password(superLogin):

    def __init__(self):
        superLogin.__init__(self)  
        
        self._service = ""         #service that the password is being stored for
        
        self._password = str(self.generatePassword()) #TODO: add validate password function
        
        #autogenerated strength/time to crack (in years)
        self._strength = self.timeTaken()

    def generatePassword(self):
        """ commented out because the code wouldnt working if regenerating a password. this code now just returns the generated password
        password = self.getPassword()
        
        if password != '':     #checks if it is empty - unless regenerating?
            return password
        else:
        """
        
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

        #TODO: make sure it isnt too long
            
        return password

    def validatePassword(self):
        password = self._password
        
        valid = False
    
        while valid == False:
            # Checks if password generated matches any common passwords or if it's empty                                                       
            if any(common in password.lower() for common in common) or password =="":
                # and regenerates it if it does
                self._password = self.generatePassword()
            else:
                valid = True


    def timeTaken(self):
        password = self._password
        length = len(password)
        ways = (26*2 + 21)  ** length
        seconds = ways / 1000000000     # assuming a password cracker can attempt 1bn passwords per second
        days = seconds / 86400          # 86400 seconds in a day
        years = days / 365              # 365 days in a year, not including leap days

        timeToCrack = round(years,2)

        return timeToCrack
        
    #GETTER METHODS

    def getService(self):
        return self._service
    
    def getStrength(self):
        return self._strength

    #SETTER METHODS
    
    def setService(self, service):
        self._service = service

    def setTimeTaken(self, timeTaken):
        self._timeTaken = timeTaken
    
    #CUSTOM PRINT FUNCTION
    def __str__(self):
        outputstring = ""
        outputstring += str(self._username) + " " + str(self._service) + " " + str(self._password) + " " + str(self._strength)
        return outputstring

#ARRAY OF OBJECTS TESTING
"""
#create object
login = superLogin()
userPassword = Password()
print(userPassword.getPassword())

#create array of objects
Passwords = [userPassword for i in range(10)]
Logins = [login for i in range(10)]
"""
#READING FILE CODE FOR LATER????????????????

def readLoginCSV(file):
    users = []
    with open("login.csv") as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",")

            user= superLogin()
            
            username= str(items[0])
            password = str(items[1])

            user.setUsername(username)
            user.setPassword(password)

            users.append(user)
            line = readfile.readline().rstrip('\n')   

    return users  

def readPasswordsCSV(file):
    passwords = []
    with open("login.csv") as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",")

            password= Password()
            
            username= str(items[0])
            password = str(items[1])
            service = str(items[2])
            strength = float(items[3])

            user.setUsername(username)
            user.setPassword(password)

            users.append(user)
            line = readfile.readline().rstrip('\n')   

    return users  

def sortArrayObjects(list):
    value = 0
    index = 0
    for i in range(1,len(list)):
        value = list[i]   #double check oop sorting
        index = i
        while index > 0 and value.getService() < list[index-1].getService():
            list[index]=list[index-1]  
            index = index-1
        list[index] = value

    return list
    

#MAIN

file = "login.csv"
users = readLoginCSV(file)


#TODO:
"""
-login check thing
- make sure password is validated
- inputs?????????????????????????????????????????????????
- array of user objects? array of array of objects? <- viable
- RSA
- integration with WEB not calculus you fool
-getter and setter methods

okay so the array is going to be filled on user log in, so that it only stores the details for the current active user
will check the first element read in from file and see if it matches the master username
"""
