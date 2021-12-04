import sys
import numpy as np

class Board:
	def __init__(self, board, id):
		self.board = board
		self.winner = np.zeros((5,5))
		self.id = index

	def mark_integer(self, val):
		index = np.where(self.board == val)
		self.winner[index[0], index[1]] = 1

	def determine_win(self):
		won = False
		# Rows:
		for r in range(5):
			if np.sum(self.winner[r,:]) == 5:
				won = True
		# Columns
		for c in range(5):
			if np.sum(self.winner[:,c]) == 5:
				won = True
		# Diaganol
		d_sum = np.sum([self.winner[x, x] for x in range(5)])
		if d_sum == 5:
			won = True

		return won

	def sum_unmarked(self):
		result_array = np.where(self.winner == 0, self.board, 0)
		result_array = result_array.astype(int)
		s = np.sum(result_array)
		return s

	def get_id(self):
		return self.id

	def get_winner_str(self):
		return str(self.winner)

	def get_board(self):
		return self.board

	def __repr__(self):
		return str(self.board)

# Input data

with open('4.input.txt', 'r') as fh:
	data = fh.read().split('\n\n')

called_numbers = data[0].split(',')
game_boards = list()

# Process Boards
for index, b in enumerate(data[1:], start=1):
	board = b.split('\n')
	board = [x.split() for x in board]
	game_boards.append(Board(np.matrix(board), index))

for c in called_numbers:
	for g in game_boards:
		#print(g)
		g.mark_integer(c)
		#print(g.get_winner_str())
		winning_number = g.determine_win()
		if winning_number:
			print('Winning Number', c)
			print(g.get_winner_str())
			print(g.get_board())
			s = g.sum_unmarked()
			print('Unmarked Sum', s)
			print('Final Value', s * int(c))
			sys.exit()