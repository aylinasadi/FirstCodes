#list [] and tuple () are ordered but set {} is not

foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("what food do you want to buy?(enetr q when done): ")
    if food.lower() == "q": #incase the user entered Q
        break
    else:
        price = float(input(f"enter the price of one {food}: "))
        quantity = int(input(f"how many {food}/s do you want?: "))
        
        foods.append(food)
        prices.append(price)
        quantities.append(quantity)
        
print("\n~YOUR SHOPPING CART~")

for food in range(len(foods)):
    subtotal = prices[food] * quantities[food]
    total += subtotal
    print(f"{foods[food]}: {quantities[food]}")
    #print(f"{foods[food]}: {quantities[food]}, end=", ") to display horizontally


print()
print(f"your total is: {total}")