temp = float(input("enter the temperature: "))
unit = input("Fahrenheit(F) or Celsius(C)? ")

if unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f"the temperature is {temp: .2f}°C")
elif unit == "C":
    temp = (temp * 9) / 5 + 32
    print(f"the temperature is {temp: .2f}°F")
else:
    print("the unit is invalid!")