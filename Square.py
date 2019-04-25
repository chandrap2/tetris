import pygame as pyg
import game_constants as g_const, util

from Terrain import Terrain

class Square():

	def __init__(self, terrain, init_x_block = 0, init_y_block = 0):
		self.screen_dim = g_const.screen_dim
		self.terrain = terrain

		# surface to be displayed, rect to be transformed
		self.s_surface = g_const.face_surface
		self.s_surface = pyg.transform.scale(self.s_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect() # pos is (0, 0)

		self.x_block, self.y_block = init_x_block, init_y_block
		self.update_pixel_pos()

	def move_to_left(self, dx):
		self.x_block -= abs(dx)
		self.update_pixel_pos()

	def move_down(self, dy):
		self.y_block += abs(dy)
		self.update_pixel_pos()

	def move_to_right(self, dx):
		self.x_block += abs(dx)
		self.update_pixel_pos()

	def move_to_block(self, x, y):
		self.x_block = x
		self.y_block = y
		self.update_pixel_pos()

	# update pixel position of Rect instance
	def update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size
		self.s_rect.y = self.y_block * g_const.square_size

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)

	def check_for_collision_to_left(self):
		return (self.x_block == 0 or self.terrain.game_map[self.x_block - 1][self.y_block] == True)

	def check_for_collision_below(self):
		return (self.y_block == g_const.screen_h_blocks - 1 or self.terrain.game_map[self.x_block][self.y_block + 1] == True)

	def check_for_collision_to_right(self):
		return (self.x_block == g_const.screen_w_blocks - 1 or self.terrain.game_map[self.x_block + 1][self.y_block] == True)

	# return index of highest free block below a given row in any given column
	def highestBelow(self):
		for row in range(self.y_block + 1, g_const.screen_h_blocks):
			if self.terrain.game_map[self.x_block][row]: return row - 1
		return g_const.screen_h_blocks - 1
