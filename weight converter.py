weight = float(input("enter your weight: "))
unit = input("kilograms(K) or pounds(L)? ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is {weight: .2f}{unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg"
    print(f"your weight is {weight: .2f}{unit}")
else:
    print("the unit is invalid!")
    
