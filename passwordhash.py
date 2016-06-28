import hashlib, uuid

password = input("Please type a new password: ")
hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

print(password)
print(hashed_password)

ipassword = input("Please type in the password you just typed to check it: ")
hashed_ipassword = hashlib.sha512(ipassword.encode('utf-8')).hexdigest()
if hashed_ipassword == hashed_password:
    print(hashed_ipassword)