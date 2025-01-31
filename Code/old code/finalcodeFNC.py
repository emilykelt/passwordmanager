 #MODULES
import random
from lists import * #words and common, from another file
from RSA import *# imports 

#THE CLASS STRUCTURE(S)

class superLogin():
    def __init__(self):
        self._username = ""
        self._password = ""

    #getters
    def getUsername(self):
        return self._username
    
    def getPassword(self):
        #this is where RSA decryption will go
        temp = ''
        temp = self._password 
        return temp
    
    #setters
    def setUsername(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    #custom print function
    def __str__(self):
        outputstring = ""
        outputstring += str(self._username) + " " + str(self._password)
        return outputstring
    
class Password(superLogin):

    def __init__(self):
        superLogin.__init__(self)  
        
        self._service = ""         #service that the password is being stored for
        
        self._password = str(self.generatePassword()) 
        self.validatePassword()
        
        #autogenerated strength/time to crack (in years)
        self._strength = self.timeTaken()

    def generatePassword(self):
        
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

    def validatePassword(self):
        password = self._password
        
        valid = False
    
        while not valid:
            # Checks if password generated matches any common passwords or if it's empty, or if its too long and hard to memorise
            
            if any(substring in password.lower() for substring  in common) or password =="" or len(password)>20 or len(password)<12:
                # and regenerates it if it does
                password= self.generatePassword()
                self._password = password
            else:
                valid = True



    def timeTaken(self):
        
        password = self._password
        
        length = len(password)
        ways = (26*2 + 21)  ** length
        seconds = ways / 1000000000     # assuming a password cracker can attempt 1bn passwords per second
        days = seconds / 86400          # 86400 seconds in a day
        years = days / 365              # 365 days in a year, not including leap days

        timeToCrack = round(years,-4) 

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
    
    #CUSTOM PRINT FUNCTION POLYMORPHISM
    def __str__(self):
        outputstring = ""
        outputstring += str(self._username) + " " + str(self._service) + " " + str(self._password) + " " + str(self._strength)
        return outputstring

#FILE HANDLING
def readLoginCSV(file,privateKey):
    users = []
    with open(file) as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",")

            user= superLogin()
            
            username= str(items[0])
            password = int(items[1])
            length = int(items[2])

            #decrypt passwords
            password = decryptMessage(password, length, privateKey)

            user.setUsername(username)
            user.setPassword(password)

            users.append(user)
            line = readfile.readline().rstrip('\n')   

    return users  

def readPasswordsCSV(file, masterusername,privateKey): #master username is the current user that is active
    details = []
    with open(file) as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",") #splits items up
            
            #get username
            username= str(items[0])

            #see if password belongs to the user logged in (masterusername)
            if username == masterusername:
                
                #read in rest to array of objects
                password = int(items[1])
                service = str(items[2])
                strength = float(items[3])
                lengthPass = int(items[4])

                #decrypt the encrypted password stored in the file
                password = decryptMessage(password, lengthPass, privateKey)
                
                #create instance of object
                detail= Password()

                #use setter methods
                detail.setUsername(username)
                detail.setPassword(password)
                detail.setService(service)
                detail.setTimeTaken(strength)

                #add object to array
                details.append(detail)
            
            #next line
            line = readfile.readline().rstrip('\n')   

    return details  

#ALGORITHMS
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

def validateLogin(inputUser,inputPass,users):  
    valid = False
    for i in range(len(users)): 
        if users[i].getUsername() == inputUser and users[i].getPassword() == inputPass: #compare current username and password
            valid = True

    return valid


#NEW PASSWORD 
def addPasswordArray(masterusername,service,details,file,publicKey):  #test encryption here
    detail= Password()

    #use setter methods
    detail.setUsername(masterusername)
    detail.setService(service)
    #password and time taken will auto generate

    #encrypt generated password
    encryptedPass = encryptMessage(detail.getPassword(),publicKey)
    
    #add object to array
    details.append(detail)

    #write to file
    DataFile = open(file,'a')
    DataFile.write(detail.getUsername() + "," + str(encryptedPass) + "," + detail.getService() + "," + str(detail.getStrength())+ "," + str(len(detail.getPassword()))+"\n")
    DataFile.close()

    #sort password details into ascending password order, do this every time a new password is added
    details = sortArrayObjects(details)
    
    return details

#FIND PASSWORD
def findPassword(goal,details):
    details = sortArrayObjects(details) # insertion sorts the passwords first
    
    found = False
    startpos = 0
    endpos = len(details) -1

    while (startpos <= endpos) and found == False:
        
        middle = (startpos+endpos)//2 #// is integer div
        
        if details[middle].getService() == goal:
            found = True
            return middle
            
        elif details[middle].getService() <goal:
            startpos = middle + 1
        else:
            endpos = middle - 1

    if found == False:
        return -1

def regeneratePassword(index, details, masterusername, publicKey): 
    if index == -1:
        print("Cannot regenerate, service not found")
    else:
        password = details[index].generatePassword()
        details[index].setPassword(password)
        details[index].validatePassword()
        details[index].setTimeTaken(details[index].timeTaken()) 

        editPasswordFile('passwords.csv', details, masterusername, publicKey )

    return details

def editPasswordFile(file, details, masterusername, publicKey ): 
    lengths = [] #parralel 1D array to store the lengths of the passwords that are already stored in the CSV
    
    #get everything from file, not including the currently logged in user, decrypt the passwords
    unactive_details = []
    with open(file) as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",") #splits items up
            
            #get username
            username= str(items[0])

            #saves the data of all of the users who arent logged in
            #as if we read in user who was logged in, would be unable to save 
            if username != masterusername:
                
                #read in rest to array of objects
                password = str(items[1])
                service = str(items[2])
                strength = float(items[3])
                lengthPass = int(items[4])
                
                #create instance of object
                detail= Password()

                #use setter methods
                detail.setUsername(username)
                detail.setPassword(password)
                detail.setService(service)
                detail.setTimeTaken(strength)
                lengths.append(lengthPass)

                #add object to array
                unactive_details.append(detail)
            
            #next line
            line = readfile.readline().rstrip('\n')   

    #write the password details of those who aren't logged in
    DataFile = open(file, 'w')
    for i in range(len(unactive_details)):
        DataFile.write(unactive_details[i].getUsername() + "," + unactive_details[i].getPassword() + "," + unactive_details[i].getService() + "," + str(unactive_details[i].getStrength())+ "," + str(lengths[i])+"\n")  
 
    #write the details of the currently logged in user to file
    for i in range(len(details)):
        DataFile.write(details[i].getUsername() + "," + str(encryptMessage(details[i].getPassword(),publicKey)) + "," + details[i].getService() + "," + str(details[i].getStrength())+ "," + str(len(details[i].getPassword()))+"\n")  
    DataFile.close() 

#PasswordExample = Password()
#PasswordExample.setPassword('HelloHelloHelloHelloHello')
#print(PasswordExample.getPassword())



"""
#MAIN FOR TESTING

#read in data to array for login
file = "login.csv"

publicKey = readKey('publickey.csv')
privateKey = readKey('privatekey.csv')

users = readLoginCSV(file, privateKey)

for i in range(10): 
    print(users[i])

#set masterusername after login validation
main = True

while main == True: #main loop
    #recieve inputs
    inputUser = str(input("input username: "))
    inputPass = str(input("input password: "))
    
    valid = validateLogin(inputUser,inputPass,users)

    while valid != True:
        print("invalid. check username and password and try again.")
        continueLoop = str(input("continue running program? y/n :")) 
        
        while continueLoop!='y' and continueLoop != 'n':   #validation
            continueLoop = str(input("continue running program? y/n :"))
            
        if continueLoop == 'n':
            main = False
            break
        
        else:
            inputUser = str(input("input username: "))
            inputPass = str(input("input password: "))

            valid = validateLogin(inputUser,inputPass,users)

    while valid == True:  #login loop
        print("valid\n")
        masterusername = inputUser

        file = "passwords.csv"
        details = readPasswordsCSV(file,masterusername,privateKey)

        details = sortArrayObjects(details)
        for i in range(len(details)):
            print(details[i])

        #loop to simulate the program, able to keep repeating actions, add password or find password
        choice = ""
        while True: #interaction with passwords loop
            choice = str(input("---------------------\nn for new password \nf to display password\nr to regenerate\nl to logout\nq to quit\n---------------------\n"))
            
            if choice == "l":
                valid = False
                break
            
            if choice == 'q':
                valid = False
                main = False
                break
            
            elif choice == 'n':
                service = str(input("service to add a password to: "))
                details = addPasswordArray(masterusername,service,details,file,publicKey)

                #print out array
                for i in range(len(details)):
                    print(details[i].getService())
                    
            elif choice =='f':
                goal = str(input("What is the service of the password you are searching for?: "))
                index = findPassword(goal,details)
                print(str(index))
                if index != -1:
                    print("Your password is: ", details[index].getPassword(),"\nIt will take ", str(details[index].timeTaken()), " years to crack with bruteforce.")
                
            elif choice == 'r':
                goal = str(input("What is the service of the password you are wanting to regenerate?: "))
                index = findPassword(goal,details)
                if index != -1:
                    details = regeneratePassword(index,details,masterusername, publicKey )
                    print(details[index].getPassword())
                
            else:
                print("invalid choice")
        

notes to self:L

username is master username in all cases

username    password    service     strength    length of password
"""

