import time, pygame as pyg
import game_constants as g_const, util

class Square():

	def __init__(self):
		# uses screen dimensions for player placement
		self.screen_dim = g_const.screen_dim

		# surface to be displayed, rect to be transformed
		self.s_surface = g_const.face_surface
		self.s_surface = pyg.transform.scale(self.s_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect() # pos is (0, 0)

		self.x_block, self.y_block = 0, 0

	def update(self, events):
		self.player_event_listener(events)

	def player_event_listener(self, events):
		for event in events:
			if event.type == g_const.WORLD_UPDATE_ID or event.type == g_const.PIECE_MANIP_LEFT_ID or event.type == g_const.PIECE_MANIP_RIGHT_ID:
				print(event)

			if event.type == g_const.WORLD_UPDATE_ID:
				self.move_down_one_block()
			elif event.type == g_const.PIECE_MANIP_LEFT_ID:
				self.move_blocks(-1, 0)
			elif event.type == g_const.PIECE_MANIP_RIGHT_ID:
				self.move_blocks(1, 0)

	def move_down_one_block(self):
		self.move_blocks(0, 1)

	def move_blocks(self, dx, dy):
		self.x_block = util.clamp(0, g_const.screen_w_blocks - 1, self.x_block + dx)
		self.y_block = util.clamp(0, g_const.screen_h_blocks - 1, self.y_block + dy)
		self.__update_pixel_pos()

	def move_to_block(self, x, y):
		self.x_block = util.clamp(0, g_const.screen_w_blocks - 1, x)
		self.y_block = util.clamp(0, g_const.screen_h_blocks - 1, y)
		self.__update_pixel_pos()

	def __update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size
		self.s_rect.y = self.y_block * g_const.square_size

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)
