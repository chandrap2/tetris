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
			if event.cus_event == g_const.SQUARE_COOR_ID:
				# has_landed = True
				x = event.params[0]
				y = event.params[1]
				self.game_map[x][y] = Square(x, y) # mark square in map
			elif event.cus_event == g_const.ROW_FULL_ID:
				self.collapse(event.params[0])
				print("collapsed")

	def collapse(self, y):
		for col in self.game_map:
			for row in range(y, -1, -1): col[row] = col[row - 1] if row != 0 else None

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
