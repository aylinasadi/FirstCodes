import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    player = input("enter a choice (rock, paper, scissors): ")
    
    while player not in options:
        print(f"{player} is not valid.")
        player = input("enter a choice (rock, paper, scissors): ")
    
    print(f"you: {player}")
    print(f"computer: {computer}")
    
    if player == computer:
        print("its a tie!")
    elif player == "rock" and computer == "scissors":
        print("you won!!!")
    elif player == "paper" and computer == "rock":
        print("you won!!!")
    elif player == "scissors" and computer == "paper":
        print("you won!!!")
    else:
        print("you lost :(")
        
    play_again = input("play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
        
print("thanks for playing :)")