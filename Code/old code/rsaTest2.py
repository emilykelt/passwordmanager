#imports
import math, makePublicPrivateKeys


#calculate block integer
symbols="abcdefghijklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZ1234567890 "
#set size = 61
#block max size = 172 

def getBlocksFromText(message):
    blockInteger = 0
    for i in range(len(message)):   #will work as block max size is much greater than password size
        blockInteger += symbols.index(message[i])*(len(symbols)**i) #how does the .index function work? could i replace it with binary search?
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


publicKey = readKey('publickey.csv')
privateKey = readKey('privatekey.csv')

message = 'naima says hi'
messageLength = len(message)

encryptedMessage = encryptMessage(message,publicKey)
print(encryptedMessage)
decryptedMessage = decryptMessage(encryptedMessage,messageLength,privateKey)
print(decryptedMessage)

if message != decryptedMessage:
    print("Error: Decryption didn't work")

#MAIN

"""
message = 'naima says hi'
messageLength = len(message)

publicKey, privateKey = makePublicPrivateKeys.generateKey(1024) # TODO: find a way to save keys so that the encryption and decryption is the same every time it is run
print(publicKey)
print(privateKey)

encryptedMessage = encryptMessage(message,publicKey)
print(encryptedMessage)
decryptedMessage = decryptMessage(encryptedMessage,messageLength,privateKey)
print(decryptedMessage)

if message != decryptedMessage:
    print("Error: Decryption didn't work")
"""

#publickey.csv
#first line n
#second line e

#privatekey.csv
#first line n
#second line d
