#import math

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))
num4 = float(input("enter the fourth number: "))
num5 = float(input("enter the fifth number: "))

av = (num1 + num2 + num3 + num4 + num5) / 5
variance = ((num1 - av) ** 2 + (num2 - av) ** 2 + (num3 - av) ** 2 + (num4 - av) ** 2 + (num5 - av) ** 2) / 5
#stan_dev = math.sqrt(variance)
stan_dev = variance ** 0.5

print("the standard deviation is: ", format(stan_dev, '.2f'))
#print(f"the average is: {av: .2f}")