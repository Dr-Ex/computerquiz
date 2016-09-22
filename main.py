import qanda
import addlanguage
from time import sleep
import hashlib
import sqlite3

conn = sqlite3.connect('quiz.db')

def hashPassword(password):
    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
    return hashed_password

def getPassword(user):
    c = conn.cursor()
    c.execute('SELECT password from users where username=?', (user,))
    userpass = str(c.fetchone())
    return userpass

def createUser():
    while True:
        print("Choose a username (type 'e' to escape this screen)")
        username = input("--> ")
        if username == 'e':
            return False
        if "('{}',)".format(username) in users:
            print("Sorry, that user already exists!")
            continue
        print()
        print("Choose a password")
        password = input("--> ")
        print("Type your password again")
        password2 = input("--> ")
        if password != password2:
            print("The passwords didn't match! Try again.")
            continue
        while True:
            print("Are you sure you want to create user {}? (y/n)".format(username))
            sure = input("--> ").lower()
            if sure == "y" or sure == "yes":
                break
            if sure == "n" or sure == "no":
                return False
            else:
                print("Sorry, that was not a valid input. Try again.")
        hpass = hashPassword(password)
        c = conn.cursor()
        c.execute('INSERT INTO users(username, password) VALUES(?,?)', (username, hpass))
        conn.commit()
        print("Created user {}".format(username))
        break
    return False

def changePassword(username):
    while True:
        print("Please enter your old password")
        oldpass = input("--> ")
        if "('{}',)".format(hashPassword(oldpass)) != getPassword(username):
            print("Sorry, that password was incorrect. Try again.")
            continue
        print("Choose a password")
        password = input("--> ")
        print("Type your password again")
        password2 = input("--> ")
        if password != password2:
            print("The passwords didn't match! Try again.")
            continue
        while True:
            print("Are you sure you want to change {}'s password? (y/n)".format(username))
            sure = input("--> ").lower()
            if sure == "y" or sure == "yes":
                break
            if sure == "n" or sure == "no":
                return False
            else:
                print("Sorry, that was not a valid input. Try again.")
        hpass = hashPassword(password)
        c = conn.cursor()
        c.execute('UPDATE users SET password=? WHERE username=?', (hpass, username))
        conn.commit()
        print("Updated {}'s password.".format(username))
        break
    return False

def getScores(username, language):
    if username == "all":
        c = conn.execute("SELECT score from scores where user=?", (username,))
    else:
        c = conn.execute("SELECT score from scores where user=? and language=?", (username, language))
    scores1 = c.fetchall()
    for i in range(len(scores1)):
        scores1[i] = str(scores1[i])
    scores = []
    for i in range(len(scores1)):
        x = scores1[i][1:len(scores1[i])-2]
        scores.append(int(x))
    return scores

def deleteUser(username):
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    c.execute("DELETE FROM scores WHERE user=?", (username,))
    conn.commit()

def getGraph(data):
    data = list(reversed(data))
    linelist = []
    if len(data) >= 10:
        for i in range(10):
            if data[i] < 10:
                line = " Game {}: {}   {}".format(i+1, data[i], "#"*data[i]) if i<9 else "Game {}: {}   {}".format(i+1, data[i], "#"*data[i])
            else:
                line = " Game {}: {}  {}".format(i+1, data[i], "#"*data[i]) if i<9 else "Game {}: {}  {}".format(i+1, data[i], "#"*data[i])
            linelist.append(line)
    else:
        print("You need to have played more than 10 games to see this!")
        pass

    return "\n".join(linelist)

def cleanSQL(string):
    string = str(string)
    string = string[2:]
    string = string[:len(string)-3]
    return string



menu = 1
game = 0
loggedin = 0
runno = 0
languages = qanda.getLanguages()

print()
print("######################################")
#print("#                                    #")
print("# Welcome to the Computer Term Quiz! #")
print("#                v1.0                #")
print("######################################")
print()
print("You choose a language and then try to translate computer terms")
print("from the chosen language into english!")



#MAIN GAME START
while True:
    menu = 1
    while menu == 1:
        while True:
            if loggedin == 1:
                break
            print()
            print("Would you like to log in to save your ")
            print("scores and keep your statistics? (y/n)")
            sure = input("--> ").lower()
            if sure == "y" or sure == "yes":
                break
            if sure == "n" or sure == "no":
                menu = 0
                game = 1
                break
            else:
                print("Sorry, that was not a valid input. Try again.") 
        if menu == 0:
            break
        
        
        
        #LOG IN SCREEN
        while True:
            if loggedin == 1:
                break
            users = []
            attempt = 1
            #get list of usernames from the database
            c = conn.execute("SELECT username from users")
            for row in c:
                users.append(str(row))
            print("Please enter your username. (Type 'e' to escape)")
            print("To create a new user type 'n'")
            username = input("--> ")
            if username == "e":
                break
            if username == 'n':
                createUser()
                continue
            #check if the username exists
            if "('{}',)".format(username) in users:
                print()
                print("Please enter your password:")
                password = input("--> ")
                if "('{}',)".format(hashPassword(password)) == getPassword(username):
                    print("You are now logged in.")
                    loggedin = 1
                    break
                else:
                    print("The password was incorrect. Try again")
            else:
                while True:
                    print("That user doesn't exist. Would you like to create a new one? (y/n)")
                    sure = input("--> ").lower()
                    if sure == "y" or sure == "yes":
                        createUser()
                        break
                    if sure == "n" or sure == "no":
                        break
                    else:
                        print("Sorry, that was not a valid input. Try again.") 
                        
                        
                        
        #MAIN USER SCREEN
        if loggedin == 1:
            print()
            if runno == 0:
                print("Welcome {}!".format(username))
            runno = 1
            print("Please choose a user action.")
            print("1. Play Quiz")
            print("2. Show all previous scores")
            print("3. View recent scores graph")
            print("4. View Statistics")
            print("5. Add a new language")
            print("6. Change your password")
            print("7. Delete your account")
            print("8. Logout")
            useraction = input("--> ")
            

            #play quiz
            if useraction == "1":
                menu = 0
                game = 1
                break
            
            #print all users previous scores
            if useraction == "2":
                print()
                for i in range(len(languages)):
                    qlang = languages[i]
                    intscores = getScores(username, qlang)
                    print("Your scores for {} are: ".format(qlang.title()))
                    if len(intscores) == 0:
                        print("You haven't played a game yet!")
                    else:
                        strscores = []
                        for j in range(len(intscores)):
                            strscores.append(str(intscores[j]))
                        print(", ".join(strscores))
                    print()

            #generate last 10 scores graphs for each language
            if useraction == "3":
                print()
                for i in range(len(languages)):
                    qlang = languages[i]
                    intscores = getScores(username, qlang)
                    print("Last 10 {} scores".format(qlang.title()))
                    print(getGraph(intscores))
                    print()
                    
            #calculate users statistics from the database
            if useraction == "4":
                for i in range(len(languages)):
                    print()
                    scores = getScores(username, languages[i])
                    avg = 0.0
                    for j in range(len(scores)):
                        avg = avg+scores[j]
                    if len(scores) > 0:
                        avg = avg/len(scores)
                    else:
                        avg = 0
                    print("{} Language Stats".format(languages[i].title()))
                    print("Your highest score is: ", max(scores) if len(scores) > 0 else "0")
                    print("Your average score is: ", avg)
               
            #add a new language
            if useraction == "5":
                addlanguage.addLanguage()

            #change password
            if useraction == "6":
                changePassword(username)
                loggedin = 0
            
            #delete account
            if useraction == "7":
                
                while True:
                    print()
                    print("Are you sure you want to delete your account {}?".format(username))
                    print("There is no turning back. (y/n")
                    sure = input("--> ").lower()
                    if sure == "y" or sure == "yes":
                        deleteUser(username)
                        loggedin = 0
                        break
                    if sure == "n" or sure == "no":
                        break
                    else:
                        print("Sorry, that was not a valid input. Try again.")

            #logout
            if useraction == "8":
                loggedin = 0
                print("You have been logged out.")
            input("Press enter to continue.")
            
    
    
    
    #QUIZ START
    while game == 1:
        score = 0
        while True:
            print()
            print("What language would you like to try today?")
            #print list of languages to choose
            languageList = qanda.getLanguages()
            languageNoList = []
            for i in range(len(languageList)):
                languageNoList.append(i+1)

            for i in range(len(languageList)):
                print("{}: {}".format(i+1, languageList[i]).title())

            try:
                language = int(input("-->"))
            except ValueError:
                print("That is not a valid option. Try again.")
                continue
            if language in languageNoList:
                language = languageList[language-1]
                break
            else:
                print("That is not a valid option. Try again.")
                continue

        
        dloop = 1
        while dloop == 1:
            print()
            print("Please choose a difficulty number:")
            print("1 - easy     (10 questions)")
            print("2 - medium   (15 questions)")
            print("3 - hard     (20 questions)")
            print("4 - hardcore (no errors allowed!)")     
            print("975 - debug")   
            try:
                difficulty = int(input("--> "))
            except ValueError:
                print("Sorry, that was not a valid input. Try again.")
                continue
            
            if difficulty == 4:
                while True:
                    print()
                    print("Are you sure you want to play on hardcore mode? (y/n)")
                    sure = input("--> ").lower()
                    if sure == "y" or sure == "yes":
                        dloop = 0
                        break
                    if sure == "n" or sure == "no":
                        break
                    else:
                        print("Sorry, that was not a valid input. Try again.")
            debug = False
            if difficulty == 975:
                difficulty = 4
                debug = True
                dloop = 0
            if difficulty < 1 or difficulty > 5:
                print("Sorry, that was not a valid input. Try again.")
                continue
            else:
                dloop = 0
        for i in range(5):
            print()
            
        qnumber = 0
        while qnumber < 20:
            question = qanda.getQuestion(qnumber, language)
            answer = qanda.getAnswer(qnumber)
            answers = qanda.generateAnswers(qnumber)
            while True:
                print()
                print("Question {}:".format(str(qnumber+1)))
                print("What does {} mean?".format(question))
                print("1. {}, 2. {}, 3. {}, 4. {}".format(
                    answers[0], answers[1], answers[2], answers[3]))
                if qnumber == 0:
                    print("(Type in the number that corresponds to the word you choose)")
                if debug == True:
                    print("Hint, it's {}".format(answer))
                try:
                    uanswer = int(input("--> "))
                except ValueError:
                    print("Sorry, that was not a valid input. Try again.")
                    continue
                if uanswer < 1 or uanswer > 4:
                    print("Sorry, that was not a valid input. Try again.")
                else:
                    break
            if uanswer == answers.index(answer.title()) + 1:
                score += 1
                print("That was correct! Your score is now {}.".format(score))
            else:
                print("Sorry, that was incorrect. Your score is{} {}.".format(
                    "" if qnumber==0 else " still", score))
            if difficulty == 4 and uanswer != answers.index(answer.title()) + 1:
                break
            qnumber += 1
            if difficulty == 1 and qnumber == 10:
                break
            if difficulty == 2 and qnumber == 15:
                break     
            else:
                sleep(1.5)
        print()
        print("You finished the game with a score of {}!".format(score))
        if loggedin == 1:
            c = conn.cursor()
            #if the user is logged in add their score to their database under their username
            c.execute('INSERT INTO scores(score, user, language) VALUES(?,?,?)', (score, username, language))
            conn.commit()
        while True:
            print("Would you like to play again? (y/n)")
            sure = input("--> ").lower()
            if sure == "y" or sure == "yes":
                break
            if sure == "n" or sure == "no":
                game = 0
                break
            else:
                print("Sorry, that was not a valid input. Try again.")    
    if loggedin == 0:
        break
#exit gracefully
conn.close()
print("Thank you for playing!")