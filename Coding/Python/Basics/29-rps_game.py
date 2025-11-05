#Rock, Paper, Scissors Game (done by myself, just for less time spent coding, arguably)
import random

options = ("rock", "paper", "scissors")
outcomes = {"rock": "paper",
            "scissors": "rock",
            "paper": "scissors"}
player = None
is_playing = True
play_choosing = True
print("============ ROCK, PAPER, SCISSORS ============ ")


while is_playing:
    player = input("Enter your choice (rock, paper or scissors): ")

    computer = random.choice(options)

    if player not in options:
        print("Please enter a valid choice")
        play_choosing = False
    elif outcomes.get(computer) == player:
        print(f"You won! The computer's guess was {computer}")
        play_choosing = True
    elif computer == player:
        print(f"You tied. The computer had {computer}")
        play_choosing = True
    elif not (outcomes.get(computer) == player):
        print(f"You lose. The computer had {computer}")
        play_choosing = True
    

    while play_choosing:
        still_play = input("Play again? (Y / N): ").upper()
        
        if still_play == "Y":
            play_choosing = False
        elif still_play == "N":
            is_playing = False
            play_choosing = False
        else:
            print("Please enter a valid choice")
       
print("Goodbye!")