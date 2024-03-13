# passwordmanager
AH Computing Project: RSA Password Manager

The aim of my project is to make a program that can store, retrieve, and update saved passwords for different websites. The password manager will be made for a group of 10 people, who have login details already stored in a file. The project is a software design project which integrates with the web design element of the course.

The project will aim to tackle the problem that many internet users have: they cannot remember very many secure passwords. Modern password managers are often locked behind a paywall and are overcomplicated. 
It will use Object oriented programming. It will have an array of password objects to store the passwords, and an array of login objects to store the logins, and these arrays of objects are  stored and modified with a class called Manager. The python program is connected to a front-end website through Flask, to input login details and passwords and display the user’s saved passwords.
The Password object inherits from the Login object.

When generating passwords, the program will generate the password to be secure (appropriate character length, mixture of uppercase, lowercase, and numbers). The passwords are generated using three random words and random numbers to make them secure and memorable, as recommended by NCSC (NCSC, n.d.). The passwords will not include any common passwords (stored in an array in a separate file and used for validation when generating the password). The password will be between 12 and 20 characters inclusive, in order for it to be secure and memorable, this will also be validated. The user can only have one password per service. If the user tries to add a password for a service that already exists, the program will display the existing password instead. 

The users will be able to log in using a pre-generated username and pre-generated master password associated with their username. The user will be faced with a login screen, and the program will validate the username and password entered to ensure that they match. If they don’t match, an error message will be displayed. The user will only be able to access stored passwords associated with their username if their login username and password match in the CSV file.  The password will be encrypted for the login details, so must be decrypted before being compared to the inputted password. The user can logout by navigating to the main page. 

On the main page they will have to select from the options to: add a password, retrieve a password, or log out. They will have the option to regenerate the password when the password is being displayed.  
The program will use insertion sort to sort the passwords alphabetically (from A to Z)  according to their service. When retrieving specific passwords, the program will use binary search to search for the password by the service they are to be used for.

When regenerating the password, the program will replace the old password with the regenerated password in the passwords CSV file and array of objects data structure. The user can regenerate a password for any of their services as many times as they would like.   

The python backend will integrate with a web frontend. The website will collect the user’s input for login details and service, and display the output provided by the python code. It will use Flask, a web framework, to connect the website to the python code. 

There will be an array of Login objects that will store the login details, and an array of Password objects to store the password details. The encrypted passwords are stored in a csv file which is read into the array of objects and decrypted at the start of the program and will only store the passwords of the currently logged in user in the Password object. As the program reads in the login details, the passwords are decrypted before being stored in the Login object.

The project will also include RSA encryption which ensures that passwords are stored securely. They will be encrypted before being stored in the csv file on device and decrypted before being stored in the program. The project uses on-device storage as at this level, this is less likely to be breached (via man-in-the-middle) than if it was transmitted to the device from an external server. The RSA encryption is limited by the processing power of the machine it is being run on. The computer may also limit the number of passwords that are to be stored, as more passwords would mean that a significant number of passwords are to be stored in memory which could have an impact on the program’s performance. 

The program will only accept user input for username, master password, and service the password is being stored for, as well as the option for what the user wants to do with the password. The username stored in the password file is the login username, the username for the individual services are not being stored. The password will be generated automatically, to ensure it is secure. When adding a password, you can only add one password and one service at a time.
The user will not be able to create a new username and master password. In order to log in they must be already in the file.
Constraints
•	Processing power of the computer – may limit strength of RSA encryption
•	Deadline of 21st March 2024 for submission; Start date 4th September 2023. 6.5 months to complete the whole project
•	CSV file for data storage (as project does not integrate with Database Design and Development)
•	Cost: must be completed using equipment already owned 
