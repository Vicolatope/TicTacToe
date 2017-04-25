import sys

#Custom game error
class GameError(Exception):
	pass

def check_next_player(current_player, next_player):
	try:
		if (current_player == next_player or (current_player != 'X' or current_player != 'O')):
			return 1
		return 0
	except:
		return 0

def check_moves(current_moves):
	map_range = [0, 1, 2]
	if 

def check_entry(game_turns):
	for idx, turn_data in enumerate(game_turns):
		try:
			if not check_next_player(turn_data, game_turns[idx + 1]):
				raise GameError

		except IndexError as e:
			break

def main():
	try:
		with open(sys.argv[1], 'r') as input_file:
			check_entry(input_file.readlines())
	except Exception as game_error:
		print(game_error)
		print('invalid input')


if __name__ == '__main__':
	main()