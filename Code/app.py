#IMPORTS
from flask import Flask, request, render_template, session
from finalcode import * 

#instantiase object
Program = Manager()

#set up flask
app = Flask(__name__)
app.secret_key = "7ae0e9e033b5" #flask needs this for the session variables

#on run open the login screen
@app.route("/")
def home():
    return render_template('index.html')


#when you submit the login HTML form you are redirected here
@app.route('/submit',methods=['GET','POST'])

def submit():
    #makes sure it is getting the right form data
    if request.method == 'POST':

        #get username and password from form
        username = request.form['username']
        password = request.form['password']

        #validate login using function
        valid = Program.validateLogin(username,password)

        #if the username and password match then session variables are stored for username and logged_in 
        if valid == True:

            #set session variables
            session['username'] = username
            session['logged_in'] = True

            return render_template('landingpage.html')
        else:
            return render_template('index.html',valid=valid)

#when the user selects that they want to retrieve a stored password
@app.route("/retrieve.html")

def retrieve():
    #get session username
    username = session.get('username')

    Program.setCurrentUser(username)

    #set details array of records up by reading in from current user
    Program.readPasswordsCSV()
    Program.sortArrayObjects()

    #get services as an array in order to display them as options for the user to choose from
    services = []

    passwords = Program.getDetails()
    for i in range(len(passwords)):
        services.append(passwords[i].getService())

    return render_template('retrieve.html', services=services)

#when the form is submitted to retrieve a password
@app.route('/find',methods=['GET','POST'])

def find():
    if 'logged_in' in session and session['logged_in']: #validate that user is logged in 
        if request.method == 'POST':

            username = session.get('username')

            Program.setCurrentUser(username)
            Program.readPasswordsCSV()
            Program.sortArrayObjects()

            #get service from form
            service = request.form['service']
            #store it as a session variable
            session['displayedService'] = service

            #find password to display, validate that it exists and if it doesnt' then display an error message
            index = Program.findPassword(service)
            if index == -1:
                password = 'Not Found. Return to home page to create a new Password'
                timeTaken = 0
            else:
                passwords = Program.getDetails()
                password = passwords[index].getPassword()
                timeTaken = passwords[index].getStrength()

            return render_template('displayPass.html',service=service,password=password,timeTaken=timeTaken)


#when the user wants to generate a new password
@app.route("/newpassword.html")

def newpass():
    return render_template('newpassword.html')

#when the user submits the form to generate a new password
@app.route('/add',methods=['GET','POST'])

def add():
    if 'logged_in' in session and session['logged_in']: #checks that they are logged in
        if request.method == 'POST':

            username = session.get('username')

            Program.setCurrentUser(username)
            Program.readPasswordsCSV()
            Program.sortArrayObjects()

            service = request.form['service']
            session['displayedService'] = service

            #checks if the password already exists, and if it doesn't then it creates a new password
            if Program.findPassword(service) == -1:
                Program.addPasswordArray(service)
            
            #display the password using the find function
            index = Program.findPassword(service)

            #displays either error message or password
            if index == -1:
                password = 'Error creating password. Please try again'
                timeTaken = 0
            else:
                passwords = Program.getDetails()
                password = passwords[index].getPassword()
                timeTaken = passwords[index].getStrength()

            return render_template('displayPass.html',service=service,password=password,timeTaken=timeTaken)


@app.route("/logout")

def logout():
    Program.logOut()
    session.clear() #clears all of the session variables, so the user must log in again
    return render_template('index.html')

@app.route("/landing")

def landing():
    #clears the current service being displayed
    session['displayedService'] = ''

    return render_template('landingpage.html')

#when the user selects the option to regenerate the displayed password
@app.route("/regenerate")

def regen():
    username = session.get('username')

    Program.setCurrentUser(username)
    Program.readPasswordsCSV()
    Program.sortArrayObjects()

    service = session.get('displayedService')

    #find the password that is displayed currently
    index = Program.findPassword(service)

    #regenerate and display
    if index == -1:
        password = 'Not Found. Return to home page to create a new Password'
        timeTaken = 0
    else:   
        Program.regeneratePassword(index)    #regenerate the password by calling a function
        passwords = Program.getDetails()
        password = passwords[index].getPassword()
        timeTaken = passwords[index].getStrength()

    return render_template('displayPass.html',service=service,password=password,timeTaken=timeTaken)


if __name__ == '__main__':  #if this is the current file being run, run the flask app
    app.run()