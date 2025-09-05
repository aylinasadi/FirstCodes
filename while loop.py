name = input("please enter your name: ")

while name == "" or not name.isalpha():
    print("please enter your name. it cant contain numbers.")
    name = input("try again: ")

name = str(name)

age = input("please enter your age: ")

while not age.isdigit() or int(age) <= 0:
    print("thats not correct!")
    age = input("try again: ")

print(f"hello {name} :)")

food = input("enter a food you like: ")

while food == "" or food.isdigit():
    print(f"oh come on {name}, dont be like that :(")
    food = input("enetr a food you like (enter q to quit): ")

while not food == "q":
    print(f"you like {food}!")
    food = input("enter another food you like (enter q to quit): ")
    
print("bye! :)")
