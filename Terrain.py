import game_constants as g_const

class Terrain:
	def __init__(self):
		self.game_map = []

		for x in range(g_const.screen_w_blocks): # each element is a column
			self.game_map.append([False for y in range(g_const.screen_h_blocks)]) # False if space is unoccupied

	def update(self, events):
		# has_landed = False

		for event in events:
			if event.type == g_const.SQUARE_COOR_ID:
				# has_landed = True
				self.game_map[event.x][event.y] = True # mark sqaure in map

		# if has_landed:
		# 	print(self.scans[0])
		#
		# 	for i in range(g_const.screen_h_blocks):
		# 		for j in range(g_const.screen_w_blocks):
		# 			print(("#" if self.game_map[j][i] else "+"), end = " ")
		# 		print()
