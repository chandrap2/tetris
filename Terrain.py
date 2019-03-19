import game_constants as g_const

class Terrain:
	def __init__(self):
		self.scans = [[g_const.screen_h_blocks for x in range(g_const.screen_w_blocks)]]
		self.game_map = []

		for x in range(g_const.screen_w_blocks):
			self.game_map.append([False for y in range(g_const.screen_h_blocks)])

	def update(self, events):
		has_landed = False

		for event in events:
			if event.type == g_const.SQUARE_COOR_ID:
				has_landed = True

				self.scans[0][event.x] = min(self.scans[0][event.x], event.y)
				self.game_map[event.x][event.y] = True

		if has_landed:
			print(self.scans[0])

			for i in range(g_const.screen_h_blocks):
				for j in range(g_const.screen_w_blocks):
					print(("#" if self.game_map[j][i] else "+"), end = " ")
				print()

	def get_bottom_below_y(self, x, y):
		if self.scans[0][x] == g_const.screen_h_blocks:
			return g_const.screen_h_blocks

		for i in range(y, g_const.screen_h_blocks):
			if i == g_const.screen_h_blocks - 1 or (not self.game_map[x][i] and self.game_map[x][i + 1]):
				return i + 1
