import sys

#Custom game error
class GameError(Exception):
	pass

# ------------- INPUT CHECK FUNCTIONS --------------- #
# => Handling format and other errors on input

# check_next_player => Checking that players take their appropriate turns
#	and don't play twice straight and also that players are 'X' or 'Y',
#	which are the only authorized players

def check_next_player(current_player, next_player):
	if (current_player == next_player or (current_player != 'X' and current_player != 'O')):
		return 1
	return 0

# check_moves => check that a move respects the map range, and that each line of input
#	is well formatted ('X/O x y\n'), each space and EOL (except the last one) are essential otherwise
#	the input will not be considered as valid if it's valid, it returns the current_move
#	as a list of ['X/O', x, y] 'X/O' being a char and x and y ints

def check_moves(current_move, map_range):
	try:
		x, y = [int(coord) for coord in current_move[1:].split()] # get x and y from current_move
		if not ((0 <= x < map_range) and (0 <= y < map_range)):
			raise GameError
		return [current_move[0], x, y]
	except:
		raise GameError

# check entry => called in the main function, it calls all different checks,
#	for each line on the input it makes a call to check_moves and fill
#	a list with all the moves wich is returned

def check_entry(game_turns, map_range):
	all_moves = []
	for idx, turn_data in enumerate(game_turns):
		try:
			if check_next_player(turn_data[0], game_turns[idx + 1][0]):
				raise GameError
		except IndexError:
			pass
		new_move = check_moves(turn_data, map_range)
		if new_move[1:] in [x[1:] for x in all_moves]: #check if the new move has already been made
			raise GameError
		all_moves.append(new_move)
	return all_moves

# ------------- PLAYING FUNCTIONS --------------- #

# make_moves => fills the game_map with the moves given as an input
#	and calls check_for_winner after each move and check_equality
#	after they all have been made

def make_moves(all_moves, map_range):
	game_map = [[' '] * map_range for i in range(map_range)]
	for move in all_moves:
		print('%s plays:\n' % move[0])
		game_map[move[1]][move[2]] = move[0]
		print_map(game_map, map_range)
		if check_for_winner(game_map, map_range):
			return
	check_equality(game_map)
	return


# ------------- WINNER CHECK FUNCTIONS --------------- #

# check_if_full => returns 1 if the tested_list is filled
#	only by player_to_check, list is created in one of 4 the next functions

def check_if_full(tested_list, player_to_check):
	for tested_value in tested_list:
		if tested_value != player_to_check:
			return 0
	return 1

# the 4 next functions generate a list epresenting a col, a row or
#	a diagonal and send it to check_if_full to check if one of the players have won.

# check_diag_lr => testing the diagonal from left top corner to right bottom corner
	
def check_diag_lr(game_map, map_range):
	diag_lr = [x[i] for i, x in enumerate(game_map)]
	if (check_if_full(diag_lr, game_map[0][0])):
		print("player %s won" % game_map[0][0])
		return 1
	return 0

# check_diag_lr => testing the diagonal from left bottom corner to right top corner

def check_diag_rl(game_map, map_range):
	diag_rl = [x[map_range - i] for i, x in enumerate(game_map, start=1)]
	if (check_if_full(diag_rl, game_map[map_range - 1][0])):
		print("player %s won" % game_map[map_range - 1][0])
		return 1
	return 0

# check_column => testing the ith column of the game_map

def check_column(game_map, map_range, i):
	col_to_check = [x[i] for x in game_map]
	if check_if_full(col_to_check, game_map[0][i]):
		print("player %s won" % game_map[0][i])
		return 1
	return 0

# check_row => testing the ith row of the game_map

def check_row(game_map, map_range, i):
	row_to_check = game_map[i]
	if check_if_full(row_to_check, game_map[i][0]):
		print("player %s won" % game_map[i][0])
		return 1
	return 0

# check_for_winner => after each move is done, make_moves function calls 
#	check_for_winner to see if the game is done, and if so, this function
#	tells who did

def check_for_winner(game_map, map_range):
	if ((game_map[0][0] != ' ') and check_diag_lr(game_map, map_range)):
		return 1
	if ((game_map[map_range - 1][0] != ' ') and check_diag_rl(game_map, map_range)):
		return 1
	for i in range(map_range):
		if ((game_map[0][i] != ' ') and check_column(game_map, map_range, i)):
			return 1
		if ((game_map[i][0] != ' ') and check_row(game_map, map_range, i)):
			return 1
	return 0

# check_equality => check if all the map have been filled

def check_equality(game_map):
	for row in game_map:
		if ' ' in row:
			print('game not over')
			return 0
	print('no winner')
	return 1

# ------------- OUTPUT FUNCTION --------------- #

# print_map => print the map after each move

def print_map(game_map, map_range):
	print("\t" + "-" * (map_range * 2 + 1))
	for row in game_map:		
		print("\t|", end='')
		for element in row:
			print("%s|" % element, end='')
		print()
	print("\t" + "-" * (map_range * 2 + 1))

# In the main, we open the input file and check for a third argument,
#	which is, if present the map_range, representing the size of the map
#	default is 3 which means default map is 3 * 3 we then get the
#	list of moves from check_entry and send it to make_moves to start the party

def main():
	all_moves = []
	try:
		map_range = 3 if len(sys.argv) != 3 else int(sys.argv[2])
		if (map_range <= 1):
			raise GameError
		with open(sys.argv[1], 'r') as input_file:
			all_moves += check_entry(input_file.readlines(), map_range)
			make_moves(all_moves, map_range)
	except Exception as e:
		print(e)
		print('invalid input')


if __name__ == '__main__':
	main()