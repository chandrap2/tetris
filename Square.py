import time, pygame as pyg
import game_constants as g_const, util

class Square():

	def __init__(self, init_x_block = 0, init_y_block = 0):
		# uses screen dimensions for player placement
		self.screen_dim = g_const.screen_dim

		# surface to be displayed, rect to be transformed
		self.s_surface = g_const.face_surface
		self.s_surface = pyg.transform.scale(self.s_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect() # pos is (0, 0)

		self.x_block, self.y_block = init_x_block, init_y_block
		self.has_hit_bottom = False
		self.update_pixel_pos()

	# def update(self, events):
	# 	self.square_event_handler(events)
	#
	# def square_event_handler(self, events):
	# 	for event in events:
	# 		if event.type == g_const.WORLD_UPDATE_ID or event.type == g_const.PIECE_MANIP_DOWN_ID:
	# 			if self.y_block == g_const.screen_h_blocks - 1 and not self.has_hit_bottom:
	# 				self.has_hit_bottom = True
	# 				pyg.event.post(pyg.event.Event(g_const.PIECE_HIT_BOTTOM))
	# 			else:
	# 				self.move_down_one_block()
	#
	# 		if not self.has_hit_bottom:
	# 			if event.type == g_const.PIECE_MANIP_LEFT_ID:
	# 				self.move_left_one_block()
	# 			if event.type == g_const.PIECE_MANIP_RIGHT_ID:
	# 				self.move_right_one_block()

	def move_down_one_block(self):
		self.move_blocks(0, 1)

	def move_left_one_block(self):
		self.move_blocks(-1, 0)

	def move_right_one_block(self):
		self.move_blocks(1, 0)

	def move_blocks(self, dx, dy):
		self.x_block = util.clamp(0, g_const.screen_w_blocks - 1, self.x_block + dx)
		self.y_block = util.clamp(0, g_const.screen_h_blocks - 1, self.y_block + dy)

		self.has_hit_bottom = self.y_block == g_const.screen_h_blocks - 1
		self.update_pixel_pos()

	def move_to_block(self, x, y):
		self.x_block = util.clamp(0, g_const.screen_w_blocks - 1, x)
		self.y_block = util.clamp(0, g_const.screen_h_blocks - 1, y)

		self.has_hit_bottom = self.y_block == g_const.screen_h_blocks - 1
		self.update_pixel_pos()

	def update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size
		self.s_rect.y = self.y_block * g_const.square_size

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)
