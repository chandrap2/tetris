import game_constants as g_const

class Terrain:
	def __init__(self):
		self.scans = [[g_const.screen_h_blocks for x in range(g_const.screen_w_blocks)]]
		print(self.scans)
		self.has_landed = False

	def update(self, events):
		self.has_landed = False

		for event in events:
			if event.type == g_const.SQUARE_COOR_ID:
				# print(event)
				self.scans[0][event.x] = max(self.scans[0][event.x], event.y)
