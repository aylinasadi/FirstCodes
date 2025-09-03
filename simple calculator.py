operator = input("enter an operator (+ - * /): ")

num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator!")