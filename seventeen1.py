# can remove 1, 2, or 3 marbles
# last marble loses
# The human always goes first. If the human enters incorrect input  
# an error message should be displayed, and the human is prompted to try again.
# The computer player can choose to remove marbles according to any strategy of your choosing. Some examples include: (i) always choose the same number as the human player, (ii) choose randomly. Note that it is possible, though not required for this exam, to devise a straightforward strategy for the computer such that it will never lose, as long as the human player goes first.

# Exceptions
# 1) numbers over 3
# 2) guesses that exceed the number of marbles in jar
# 3) non-integers

import random
def game_flow():
	marble_count = 17
	print("Let's play the game of Seventeen!\nNumber of marbles left in jar: 17")
	your_turn(marble_count)

def your_turn(marble_count):
	guess = ''
	while type(guess) != int:
		try: 
			guess = int(input("\nYour turn: How many marbles will you remove (1-3)? "))
			if guess <= marble_count and 0 < guess < 4:
				break
			elif guess > marble_count:
				guess = ''
				print("Sorry, that is not a valid option. Try again!")
				print("Number of marbles left in jar: ", marble_count)
			else:
				guess = '' 
				raise ValueError
		except ValueError:
			print("Sorry, that is not a valid option. Try again!")
			print("Number of marbles left in jar: ", marble_count)
			continue
	marble_count -= int(guess)
	print("You removed {} marbles.".format(guess))
	print("Number of marbles in jar: {}".format(marble_count))
	if marble_count > 0:
		computer_turn(marble_count)
	else:
		print("\nThere are no marbles left. Computer wins!")
		exit()

def computer_turn(marble_count):
	if marble_count > 3: 
		guess = random.randint(1, 3)
	else: 
		guess = random.randint(1, marble_count)
	print("\nComputer's turn...\nComputer removed {} marbles.".format(guess))
	marble_count -= int(guess)
	print("Number of marbles in jar: {}".format(marble_count))
	if marble_count > 0:
		your_turn(marble_count)
	else:
		print("\nThere are no marbles left. You win!")
		exit()

def main():
	(game_flow())

if __name__ == "__main__":
	main()
# At the end of each turn, the program should print out the number of marbles removed in the previous turn,
# and print the number of marbles that remain in the jar. 
# Once there are no more marbles in the jar, the program should declare the winner of the game.

# Sample Output for Version 1

# % python i206_placein_source1_chuang.py

# Let's play the game of Seventeen!
# Number of marbles left in jar: 17

# Your turn: How many marbles will you remove (1-3)? 3
# You removed 3 marbles.
# Number of marbles left in jar: 14

# Computer's turn...
# Computer removed 1 marbles.
# Number of marbles left in jar: 13

# Your turn: How many marbles will you remove (1-3)? 2
# You removed 2 marbles.
# Number of marbles left in jar: 11

# Computer's turn...
# Computer removed 2 marbles.
# Number of marbles left in jar: 9

# Your turn: How many marbles will you remove (1-3)? 2
# You removed 2 marbles.
# Number of marbles left in jar: 7

# Computer's turn...
# Computer removed 2 marbles.
# Number of marbles left in jar: 5

# Your turn: How many marbles will you remove (1-3)? 4
# Sorry, that is not a valid option. Try again!
# Number of marbles left in jar: 5

# Your turn: How many marbles will you remove (1-3)? 1
# You removed 1 marbles.
# Number of marbles left in jar: 4

# Computer's turn...
# Computer removed 3 marbles.
# Number of marbles left in jar: 1

# Your turn: How many marbles will you remove (1-3)? 0
# Sorry, that is not a valid option. Try again!
# Number of marbles left in jar: 1

# Your turn: How many marbles will you remove (1-3)? 1
# You removed 1 marbles.

# There are no marbles left. Computer wins!