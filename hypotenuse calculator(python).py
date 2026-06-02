import math

a = float(input("enter side a of the triangle: "))
b = float(input("enter side b of the triangle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"the hypotenuse of the triangle is: {c}")