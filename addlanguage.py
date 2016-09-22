# to add a new language log into main.py and select add language from the menu

import sqlite3

conn = sqlite3.connect('quiz.db')
c = conn.cursor()

english = ["mouse", "keyboard", "speaker", "internet", "monitor", 
           "computer", "email", "virus", "memory", "backup", 
           "microphone", "copy", "paste", "cursor", "floppy disk", 
           "download", "spreadsheet", "toolbar", "format", "database"]

newLanguage = []

def addLanguage():
	print()
	print("What is the name of the language that you will be adding? (one word only)")
	print("(type 'a' at any time to abort)")
	languageName = input("-->").lower()
	if languageName == 'a':
		pass

	print()

	for i in range(20):
		print()
		print("Please enter the {} word for {}".format(languageName, english[i]))
		currentWord = input("-->").lower()
		if currentWord == 'a':
			pass
		newLanguage.append(currentWord)

	c.execute("INSERT INTO languages (language_name, mouse, keyboard, speaker, internet, monitor, "
		"computer, email, virus, memory, backup, microphone, copy, paste, cursor, floppy_disk, "
		"download, spreadsheet, toolbar, format, database) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		(languageName, newLanguage[0], newLanguage[1], newLanguage[2], newLanguage[3], newLanguage[4], newLanguage[5], 
			newLanguage[6], newLanguage[7], newLanguage[8], newLanguage[9], newLanguage[10], newLanguage[11], newLanguage[12], newLanguage[13], 
			newLanguage[14], newLanguage[15], newLanguage[16], newLanguage[17], newLanguage[18], newLanguage[19]))

	conn.commit()

	print("Your language has been added.")
