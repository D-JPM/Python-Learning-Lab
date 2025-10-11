import time # Instruction flow
import getpass # To hide player input
""" OBJ - Exercise 08/40: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
 	compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
user_start = input("Ready to play Rock, Paper, Scissors [Y/n]: ").strip().lower()
# Game start/end conditional
if user_start == "y" or user_start == "":
	pass # continue program
else:
	print("You have decided not to play, this session will now end.")
	quit() # end program

# Game start selected
print("You have selected to play Rock, Paper, Scissors!")
time.sleep(2)

# Game rules
print("""These are the rules of the Game:
	- Rock beats scissors
	- Scissors beats paper
	- Paper beats rock""")
time.sleep(2)

# Play structure
print("Player 1 will select their item first, PLayer 2 follows.")
time.sleep(2)
print("Then we will see who is the Winner, Loser or if you both have the same taste - resulting in a draw")
time.sleep(2)

# Declaring player names
player1 = input("Player 1, please type your name: ")
print(f"{player1} is now Player 1")
time.sleep(1)
player2 = input("Player 2, please type your name: ")
print(f"{player2} is now Player 2")
time.sleep(1)
print(f"It's {player1} Vs {player2}! Game on!!")
time.sleep(1)
print("When selecting an item, type only the first letter.")
time.sleep(2)
print("""For example
	  'R' = Rock
	  'P' = Paper
	  'S' = Scissors
Don't worry about capitalisation, the letter will suffice.""")

# Item hierarchy 
win_dict = {
	"r": "p", # P beats R
	"p": "s", # S beats P
	"s": "r"  # R beats S
}

# Game Loop
while user_start == "y":
	player1_choice = getpass.getpass(f"{player1} pick your item: ").strip().lower()
	player2_choice = getpass.getpass(f"{player2} pick your item: ").strip().lower()
	
	# Player choice to quit game session.
	if player1_choice.lower() or player2_choice.lower() == "quit":
		print("Game session has ended.")
		break # exit loop	
		
	# Player Choice control flow
	if player1_choice == player2_choice:
		print("Draw")
	elif win_dict.get(player1_choice) == player2_choice:
		print(f"{player2} WINS!")
	elif win_dict.get(player2_choice) == player1_choice:
		print(f"{player1} WINS!")
	else:
		print( "Invalid item input")
