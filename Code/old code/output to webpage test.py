from finalcode import *
import webbrowser

def displayPasswordonWeb(password):
    with open("test.html","w") as fileout:
        html_str = """ 
        <!DOCTYPE html>
    <head>

        <link rel="stylesheet" href="stylepage.css">

    <html>
        <title>Password</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body>
    <div class="'containter">
    <div class ='head'>
    <h1>password</h1>
    </div>
    <div class="inner">

        """ 
        fileout.write(html_str)

    #put in your change to the web page

    with open("test.html","a") as fileout:
        html_str = """
        <p>%s</p> """% (password)
        fileout.write(html_str)

    #close the HTML document
    with open("test.html","a") as fileout:
        html_str = """
        </div>
        </div>
        </table>
        </body>
        </html>
        """
        fileout.write(html_str)

    #open the page on the web
    webbrowser.open('test.html', new=1, autoraise = True)

#read in data to array for login
file = "login.csv"

publicKey = readKey('publickey.csv')
privateKey = readKey('privatekey.csv')

users = readLoginCSV(file, privateKey)


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
        for i in range(len(details)):
            print(details[i].getService())

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
                if index != -1:
                    print("Your password is: ", details[index].getPassword(),"\nIt will take ", str(details[index].timeTaken()), " years to crack with bruteforce.")
                    displayPasswordonWeb(details[index].getPassword())
            elif choice == 'r':
                goal = str(input("What is the service of the password you are wanting to regenerate?: "))
                index = findPassword(goal,details)
                if index != -1:
                    details = regeneratePassword(index,details,masterusername, privateKey, publicKey )
                    print(details[index].getPassword())
                
            else:
                print("invalid choice")
        
