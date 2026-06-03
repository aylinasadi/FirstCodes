username = input("please enter a username: ")

if len(username) > 12:
    print("your username cant be more than 12 characters!")
elif not username.find(" ") == -1:
    print("your username cant contain spaces!")
elif not username.isalpha():
    print("your username cant contain numbers!")
else:
    print(f"welcome {username}!")