import random

output_file = open('i206_placein_output2_morganjordan.txt', 'w')
with open('i206_placein_input_0.txt', 'r') as file_handle:
	games = file_handle.readlines()

p1_win_count = 0
p2_win_count = 0
play_total = (len(games)) # the total number of games that we will play. Ten games total (0-9) 
play = 0 # counter to count down the play_total as we go from game to game

move_list = [] # keeps track of the moves from each game for eventually writing to file

def game_flow(turn=-2):
	global play_total
	global play
	while play_total != play:
	    marble_count = 17
	    your_turn(marble_count, turn)
	    continue
	if play_total == play:
		output_file.write("Player 1 won {} times; Player 2 won {} times.".format(p1_win_count, p2_win_count))
		print("Player 1 won {} times; Player 2 won {} times.".format(p1_win_count, p2_win_count))
		exit()

def your_turn(marble_count, turn):
	global play
	global move_list
	global p2_win_count
	turn += 2
	guess = int(games[play][turn])
	if guess > marble_count:
		guess = marble_count # If the number of marbles in the jar is less than the next guess on the list, then remove the rest of the marbles
	move_list.append(str(guess))
	marble_count -= guess
	if marble_count > 0:
		computer_turn(marble_count, turn)
	else:
		output_file.write("Game #{}. Play sequence: {}. Winner: {}\n".format(play + 1, "-".join(move_list), "P2"))
		p2_win_count += 1
		play += 1
		move_list = []
		game_flow()


def computer_turn(marble_count, turn=0):
	global play
	global move_list
	global p1_win_count
	if marble_count > 3: 
		guess = random.randint(1, 3)
	else: 
		guess = random.randint(1, marble_count)
	# print("\nComputer's turn...\nComputer removed {} marbles.".format(guess))
	move_list.append(str(guess))
	marble_count -= int(guess)
# 	print("Number of marbles in jar: {}".format(marble_count))
	if marble_count > 0:
	    your_turn(marble_count, turn)
	else:
		output_file.write("Game #{}. Play sequence: {}. Winner: {}\n".format(play + 1, "-".join(move_list), "P1"))
		p1_win_count += 1
		play += 1
		move_list = []
		game_flow()



def main():
	(game_flow())
	output_file.close() # once play == play_total, the file closes and the game is over

if __name__ == "__main__":
	main()

# plays the Seventeen Game in batch mode.
# The program reads from an input file (named 'i206_placein_input.txt') 
# a sequence of comma delimited numbers representing 
# the sequence of moves made by Player 1. Each line of the input file represents a different game. 
# For example, the sample input file contains data for ten games. 
# In the first game, Player 1 removes 3 marbles during its first turn, 1 marble during its second turn,
# three marbles during its third turn, and so on.

# If the number of marbles left in the jar is fewer than the next number in the play sequence, 
# then Player 1 should remove all the remaining marbles. 

# For example, if there are two marbles left in the jar, and the next number in the sequence is 3, 
# then Player 1 should remove two marbles, not three.

# Player 2 will play the same marble-removal strategy as in Version 1.

# Note that not all numbers in each line may be used, depending on the progress of the game (which in turn depends on the strategy used by Player 2). Conversely, the play sequences are generated such that there will always be enough numbers for each game.

# # The program will play the game as many times as there are lines in the input file, 
# # printing the sequence of moves and the game winner into an output text file (named i206_placein_output2_<ischool_userid>.txt'), 
# # one line per game. At the end of all the games, the program will print the number of games won by each player. 
# # # See below for what an output file for ten games might look like.
# # Game #1. Play sequence: 3-1-1-1-3-1-2-1-3-1. Winner: P1
# # Game #2. Play sequence: 3-1-2-1-2-1-3-1-2-1. Winner: P1
# # Game #3. Play sequence: 2-1-1-1-3-1-3-1-2-1-1. Winner: P2
# # Game #4. Play sequence: 1-1-2-1-2-1-3-1-3-1-1. Winner: P2
# # Game #5. Play sequence: 3-1-2-1-1-1-2-1-2-1-2. Winner: P2
# # Game #6. Play sequence: 3-1-2-1-2-1-1-1-1-1-2-1. Winner: P1
# Game #7. Play sequence: 1-1-1-1-1-1-2-1-1-1-3-1-2. Winner: P2
# Game #8. Play sequence: 2-1-1-1-1-1-1-1-2-1-1-1-2-1. Winner: P1
# Game #9. Play sequence: 1-1-2-1-1-1-1-1-3-1-3-1. Winner: P1
# Game #10. Play sequence: 1-1-2-1-3-1-2-1-2-1-2. Winner: P2
# Player 1 won 5 times; Player 2 won 5 times.