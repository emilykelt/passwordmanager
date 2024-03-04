#imports
import math, makePublicPrivateKeys


#calculate block integer
symbols="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
#set size = 61
#block max size = 172 

def getBlocksFromText(message):
    blockInteger = 0
    for i in range(len(message)):   #will work as block max size is much greater than password size
        blockInteger += symbols.index(message[i])*(len(symbols)**i) 
    return blockInteger

def getTextFromBlocks(blockInteger,messageLength):
    message = ""
    for i in range(messageLength):
        indexOfCharacter = blockInteger//(len(symbols)**(messageLength-1-i))
        #to decrypt the block integer you divide it by set size, and by the index of the last character moving backwards
        character = symbols[indexOfCharacter]
        message += character
        blockInteger = blockInteger % (len(symbols)**(messageLength-1-i))
        #figures out the characters in reverse
    return message[::-1]    #reverses the string

def encryptMessage(message,key):
    n,e = key[0],key[1]
    block = getBlocksFromText(message)
    return pow(block,e,n)

def decryptMessage(encryptedMessage,messageLength,key):
    n,d = key[0],key[1]
    block = pow(encryptedMessage,d,n)
    return getTextFromBlocks(block,messageLength)

def readKey(file):
    #n first then either e or d
    key = []
    with open(file) as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",") #splits items up
            
            #get username
            partOfKey= int(items[0])

            key.append(partOfKey)
            
            #next line
            line = readfile.readline().rstrip('\n')
        return key

#use this code to generate the keys
"""
publicKey = readKey('publickey.csv')
privateKey = readKey('privatekey.csv')

message = 'abcdefghijklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZ1234567890 '
messageLength = 20


encryptedMessage = encryptMessage(message,publicKey)
print(encryptedMessage)

encryptedMessage = 332159251659504692591020472218941848952727781939705877042961237353981027042605920910131606445598755314374307678341082299217351244439184065522191602695956560767791696812859881428271351905649782193857101213015240061476397945578651586133677192700184749344531825531859746164136968384087920443789577209838322995737967051206619192999097233273721676388518153659670463755093051710449748657318148448093391841429979453029067081372141608279815403831002752564520661098757050825159246884982942343319819446943521996554297667261748915724193967679180264351057747534600315792696090321777519787702819829679700186296819288894507219908

decryptedMessage = decryptMessage(encryptedMessage,messageLength,privateKey)
print(decryptedMessage)


#MAIN


message = 'naima says hi'
messageLength = len(message)

publicKey, privateKey = makePublicPrivateKeys.generateKey(1024) <- put in report as this is the code used to generate the public/private keys
print(publicKey)
print(privateKey)



if message != decryptedMessage:
    print("Error: Decryption didn't work")

#TEST - this code prints out all of the encrypted passwords

publicKey = readKey('publickey.csv')
privateKey = readKey('privatekey.csv')

with open('login.csv') as readfile:    #prepares to read data from text file 
        line = readfile.readline().rstrip('\n')

        while line: #repeats for every line
            items = line.split(",") #splits items up
            
            #get username
            print(str(items[0]))
            temp = items[1]
            encryptedMessage = encryptMessage(temp,publicKey)
            print(str(encryptedMessage))
            decryptedMessage = decryptMessage(encryptedMessage,len(temp),privateKey)
            print(decryptedMessage)
            print("length:", len(decryptedMessage))
            print("\n")

            
            #next line
            line = readfile.readline().rstrip('\n') 
"""

#publickey.csv
#first line n
#second line e

#privatekey.csv
#first line n
#second line d
