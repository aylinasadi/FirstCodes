code = "3104"
guess = []

for num in range (10000):
    guess1 = num // 1000
    guess2 = (num // 100) % 10
    guess3 = (num // 10) % 10
    guess4 = num % 10

    if 7 in [guess1, guess2, guess3, guess4]:
        continue
    if guess3 % 2 != 0:
        continue
    if guess1 + guess2 != guess4:
        continue

    guess.append(f"{guess1}{guess2}{guess3}{guess4}")

print(f"there are {len(guess)} possible options")
print("cracking the code...")

import time
timer = 5
for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

for i in guess:
    if i == code:
        print(f"the code was {i}")
        print('ACCESS GRANTED')
    else:
        continue