import sqlite3
from random import randint

conn = sqlite3.connect('quiz.db')

users = []
c = conn.execute('SELECT username from users')
for row in c:
	users.append(str(row))
while True:
	user = input('Please enter a username to add random scores to: ')

	if "('{}',)".format(user) not in users:
		print("User doesn't exist")
	else:
		break

c = conn.cursor()
for i in range(15):
	c.execute('INSERT INTO scores(score, user, language) VALUES(?,?,?)', (randint(0,20), user, "maori"))
	conn.commit()

for i in range(15):
	c.execute('INSERT INTO scores(score, user, language) VALUES(?,?,?)', (randint(0,20), user, "spanish"))
	conn.commit()

