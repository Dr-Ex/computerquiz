from random import choice, shuffle
import sqlite3

conn = sqlite3.connect('quiz.db')
c = conn.cursor()

english = ["mouse", "keyboard", "speaker", "internet", "monitor", 
           "computer", "email", "virus", "memory", "backup", 
           "microphone", "copy", "paste", "cursor", "floppy disk", 
           "download", "spreadsheet", "toolbar", "format", "database"]


#cleans output from an sqlite query and converts to string
def cleanSQL(string):
    string = str(string)
    string = string[2:]
    string = string[:len(string)-3]
    return string

def getLanguages():
    languageList = []
    languages = c.execute("SELECT language_name FROM languages")
    for language in languages:
        languageList.append(cleanSQL(language))
    return languageList


def getQuestion(qnumber, language):
    questionList = []
    question = c.execute("SELECT %s FROM languages WHERE language_name=?;" % (english[qnumber]), (language,))
    for word in question:
        questionList.append(cleanSQL(word))
    return questionList[0]

def getAnswer(qnumber):
    return english[qnumber]

# generates a list of 4 english words which contains one correct and 3 incorrect
def generateAnswers(qnumber):
    answers = []
    answers.append(english[qnumber])
    for i in range(3):
        while True:
            item = choice(english)
            if item in answers or item == english[qnumber]:
                continue
            else:
                break
        answers.append(item)
    shuffle(answers)
    for i in range(len(answers)):
        answers[i] = answers[i].title()
    return answers