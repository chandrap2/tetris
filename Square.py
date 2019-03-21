import time, pygame as pyg
import game_constants as g_const, util

from Terrain import Terrain

class Square():

	def __init__(self, terrain, init_x_block = 0, init_y_block = 0):
		# uses screen dimensions for player placement
		self.screen_dim = g_const.screen_dim
		self.terrain = terrain

		# surface to be displayed, rect to be transformed
		self.s_surface = g_const.face_surface
		self.s_surface = pyg.transform.scale(self.s_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect() # pos is (0, 0)

		self.x_block, self.y_block = init_x_block, init_y_block
		self.has_hit_bottom = False
		self.update_pixel_pos()

	def move_to_left(self, dx):
		# if not terrain.check_for_collision_to_left(self):
		self.x_block -= abs(dx)
		self.update_pixel_pos()

			# return True
		# return False

	def move_down(self, dy):
		# if not terrain.check_for_collision_below(self):
		self.y_block += abs(dy)
		self.update_pixel_pos()

		self.has_hit_bottom = self.check_for_collision_below()

		# 	return True
		#
		# self.has_hit_bottom = True
		# return False

	def move_to_right(self, dx):
		# if not terrain.check_for_collision_to_right(self):
		self.x_block += abs(dx)
		self.update_pixel_pos()
		#
		# 	return True
		# return False

	def move_blocks(self, dx, dy, terrain):
		self.x_block = self.x_block + dx
		self.y_block = self.y_block + dy

		bottom = terrain.get_bottom_below_y(self.x_block, self.y_block)

		self.has_hit_bottom = self.y_block == bottom - 1
		self.update_pixel_pos()

	def move_to_block(self, x, y, terrain):
		self.x_block = x
		self.y_block = y

		bottom = terrain.get_bottom_below_y(self.x_block, self.y_block)

		self.has_hit_bottom = self.y_block == bottom - 1
		self.update_pixel_pos()

	def update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size
		self.s_rect.y = self.y_block * g_const.square_size

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)

	# def check_collision_neighbors(self):
	# 	coll_map = (self.check_for_collision_to_left(square), self.check_for_collision_below(square), self.check_for_collision_to_right(square))
	# 	return coll_map

	def check_for_collision_to_left(self):
		return (self.x_block == 0 or self.terrain.game_map[self.x_block - 1][self.y_block] == True)

	def check_for_collision_below(self):
		return (self.y_block == g_const.screen_h_blocks - 1 or self.terrain.game_map[self.x_block][self.y_block + 1] == True)

	def check_for_collision_to_right(self):
		return (self.x_block == g_const.screen_w_blocks - 1 or self.terrain.game_map[self.x_block + 1][self.y_block] == True)

	def check_for_collision_coordinate(self, x, y):
		return self.terrain.game_map[x][y]
