from random import choice, shuffle
import sqlite3

# conn = sqlite3.connect('quiz.db')
# c = conn.cursor()
#c.execute("sqlite statement")

english = ["mouse", "keyboard", "speaker", "internet", "monitor", 
           "computer", "email", "virus", "memory", "backup", 
           "microphone", "copy", "paste", "cursor", "floppy disk", 
           "download", "spreadsheet", "toolbar", "format", "database"]
maori = ["kiore rorohiko", "papapāhuti", "tukuoro", "ipurangi", "kaupane", 
         "rorohiko", "karere hiko", "ngārara", "pūmahara", "tārua", 
         "hopuoro", "tārua", "tāpia", "kaitiri", "kōpae ngohe", 
         "tango iho", "whārangi-hora", "paeutauta", "whakatakoto", "pūpāhīhī"]
spanish = ["ratón", "teclado", "altoparlante", "internet", "monitor", 
           "computadora", "correo electrónico", "virus", "memoria", "apoyo", 
           "micrófono", "dupdo", "pegar", "cursor", "disco flexible", 
           "descargar", "hoja de cálculo", "barra de herramientas", "formato", "base de datos"]

#maori = c.execute("SELECT * FROM languages WHERE language_name = ?", ())

def getQuestion(qnumber, language):
    if language == "maori":
        return maori[qnumber]
    if language == "spanish":
        return spanish[qnumber]

def getAnswer(qnumber):
    return english[qnumber]

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