age = int(input("enter your age: "))

print(f"{age} is a positive number!" if age > 0 else f"hey! you cant be {age}!")
print(f"{age} is an even number!" if age % 2 == 0 else f"{age} is an odd number!")
print("you are an adult!" if age >= 20 else "you are not an adult yet!")