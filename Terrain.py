import game_constants as g_const
from Square import Square

class Terrain:
	def __init__(self):
		self.game_map = []

		for x in range(g_const.arena_w_blocks): # each element is a column
			self.game_map.append([None for y in range(g_const.arena_h_blocks)]) # None if space is unoccupied

	def update(self, events):
		# has_landed = False

		for event in events:
			if event.cus_event == g_const.PIECE_HIT_BOTTOM_ID:
				for square_pos in event.params:
					# has_landed = True
					x = square_pos[0]
					y = square_pos[1]
					self.game_map[x][y] = Square(x, y)  # mark square in map
			elif event.cus_event == g_const.ROW_FULL_ID:
				self.collapse(event.params[0])
				# self.print_map()
				# print("..............")

	def collapse(self, y):
		for col in self.game_map:
			for row in range(y, -1, -1):
				if row != 0:
					col[row] = col[row - 1]
					if col[row] != None: col[row].move_down(1)
				else:
					col[row] = None

	def check_for_collision_to_left(self, square):
		return (square.x_block == 0 or self.game_map[square.x_block - 1][square.y_block] != None)

	def check_for_collision_below(self, square):
		return (square.y_block == g_const.arena_h_blocks - 1 or self.game_map[square.x_block][square.y_block + 1] != None)

	def check_for_collision_to_right(self, square):
		return (square.x_block == g_const.arena_w_blocks - 1 or self.game_map[square.x_block + 1][square.y_block] != None)

	# return index of highest FREE block below a given row in any given column
	def highestBelow(self, square):
		for row in range(square.y_block + 1, g_const.arena_h_blocks):
			if self.game_map[square.x_block][row] != None: return row - 1
		return g_const.arena_h_blocks - 1

	def print_map(self):
		for row in range(g_const.arena_h_blocks):
			for col in range(g_const.arena_w_blocks):
				print("#" if self.game_map[col][row] != None else "*", end = "")
			print()
		print()
