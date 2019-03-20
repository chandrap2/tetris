import game_constants as g_const

from Square import Square

class Terrain:
	def __init__(self):
		self.scans = []
		self.scans.append([g_const.screen_h_blocks for x in range(g_const.screen_w_blocks)]) # top-most block in each column
		self.scans.append([-1 for y in range(g_const.screen_h_blocks)]) # left-most block in each column relative to right edge of screen
		self.scans.append([g_const.screen_w_blocks for y in range(g_const.screen_h_blocks)]) # right-most block in each column relative to left edge of screen

		self.game_map = []
		for x in range(g_const.screen_w_blocks): # each element is a column
			self.game_map.append([False for y in range(g_const.screen_h_blocks)]) # False if space is unoccupied

	def update(self, events):
		# has_landed = False

		for event in events:
			if event.type == g_const.SQUARE_COOR_ID:
				has_landed = True

				self.scans[0][event.x] = min(self.scans[0][event.x], event.y)
				self.scans[1][event.y] = min(self.scans[1][event.y], event.y)
				self.scans[2][event.y] = max(self.scans[2][event.y], event.y)

				self.game_map[event.x][event.y] = True

		# if has_landed:
		# 	print(self.scans[0])
		#
		# 	for i in range(g_const.screen_h_blocks):
		# 		for j in range(g_const.screen_w_blocks):
		# 			print(("#" if self.game_map[j][i] else "+"), end = " ")
		# 		print()

	def get_bottom_below_y(self, x, y):
		if self.scans[0][x] == g_const.screen_h_blocks:
			return g_const.screen_h_blocks

		for i in range(y, g_const.screen_h_blocks):
			if i == g_const.screen_h_blocks - 1 or (not self.game_map[x][i] and self.game_map[x][i + 1]):
				return i + 1

	def get_left_of_x(self, x, y):
		if self.scans[1][y] == -1:
			return -1

		for i in range(x, -1, -1):
			if i == 0 or (not self.game_map[i][y] and self.game_map[i - 1][y]):
				return i - 1

	def get_right_of_y(self, x, y):
		if self.scans[2][y] == g_const.screen_w_blocks:
			return g_const.screen_w_blocks

		for i in range(x, g_const.screen_w_blocks):
			if i == g_const.screen_w_blocks - 1 or (not self.game_map[i][y] and self.game_map[i + 1][y]):
				return i + 1

	def check_collision(self, square):
		coll_map = (self.check_for_collision_to_left(square), self.check_for_collision_below(square), self.check_for_collision_to_right(square))
		return coll_map

	def check_for_collision_to_left(self, square):
		return (square.x_block == 0 or self.game_map[square.x_block - 1][square.y_block] == True)

	def check_for_collision_below(self, square):
		return (square.y_block == g_const.screen_h_blocks - 1 or self.game_map[square.x_block][square.y_block + 1] == True)

	def check_for_collision_to_right(self, square):
		return (square.x_block == g_const.screen_w_blocks - 1 or self.game_map[square.x_block + 1][square.y_block] == True)
