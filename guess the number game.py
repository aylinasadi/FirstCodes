import random

low = 0
high = 100
guesses = 0

number = random.randint(low, high)

print("guess what number im thinking of!")

while True:
    guess = int(input(f"enetr a number between {low} and {high}: "))
    guesses += 1
    
    if guess < number:
        print(f"{guess} is too low!")
    elif guess > number:
        print(f"{guess} is to high!")
    else:
        print(f"you found it! {guess} was the number!")
        break
    
print(f"it took you {guesses} guesses to find the number.")