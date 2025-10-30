username = "admin"
password = "12345"

input_username = input('username: ')
input_password = input('password: ')

if input_username == username:
    if input_password == password:
        print('Access Granted.')
    else:
        print('Incorrect password.')
else:
    print('User not found.')