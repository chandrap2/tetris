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
	
	def move_down_one_block(self):
		self.move_blocks(0, 1)

	def move_left_one_block(self):
		self.move_blocks(-1, 0)

	def move_right_one_block(self):
		self.move_blocks(1, 0)

	def move_blocks(self, dx, dy):
		self.x_block = self.x_block + dx
		self.y_block = self.y_block + dy

		self.has_hit_bottom = self.y_block == g_const.screen_h_blocks - 1
		self.update_pixel_pos()

	def move_to_block(self, x, y):
		self.x_block = x
		self.y_block = y

		self.has_hit_bottom = self.y_block == g_const.screen_h_blocks - 1
		self.update_pixel_pos()

	def update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size
		self.s_rect.y = self.y_block * g_const.square_size

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)
