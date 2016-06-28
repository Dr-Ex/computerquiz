import sqlite3
conn = sqlite3.connect('quiz.db')

users = []

c = conn.execute("SELECT username from users")
for row in c:
    users.append(str(row))
#print(users)

for i in range(len(users)):
    print("('{}',)".format(users[i]))
if "('{}',)".format("henry") in users:
    print('yay')