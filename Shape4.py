import pygame as pyg
import game_constants as g_const, util

from Shape1 import Shape1
from Terrain import Terrain

class Shape4(Shape1):
	"""
	..3
	012
	...
	"""

	def __init__(self, terrain):
		self.terrain = None
		self.squares = [(0, 1), (1, 1), (2, 1), (2, 0)]
		self.origin_block = None # second element is square of reference

		self.orient_state = g_const.SHAPE_ORIENT_1
		self.has_hit_bottom = False

		self.init_shape(terrain, g_const.s4_surf, 1)

	def rotate_clock(self):
		if not self.check_for_collision_around_origin():
			self.orient_state = (self.orient_state + 1 if self.orient_state != g_const.SHAPE_ORIENT_4 else g_const.SHAPE_ORIENT_1)
			origin_x, origin_y = self.origin_block.get_block_pos()

			if self.orient_state == g_const.SHAPE_ORIENT_1:
				self.squares[0].move_to_block(origin_x - 1, origin_y)
				self.squares[2].move_to_block(origin_x + 1, origin_y)
				self.squares[3].move_to_block(origin_x + 1, origin_y - 1)
			elif self.orient_state == g_const.SHAPE_ORIENT_2:
				self.squares[0].move_to_block(origin_x, origin_y - 1)
				self.squares[2].move_to_block(origin_x, origin_y + 1)
				self.squares[3].move_to_block(origin_x + 1, origin_y + 1)
			elif self.orient_state == g_const.SHAPE_ORIENT_3:
				self.squares[0].move_to_block(origin_x + 1, origin_y)
				self.squares[2].move_to_block(origin_x - 1, origin_y)
				self.squares[3].move_to_block(origin_x - 1, origin_y + 1)
			else:
				self.squares[0].move_to_block(origin_x, origin_y + 1)
				self.squares[2].move_to_block(origin_x, origin_y - 1)
				self.squares[3].move_to_block(origin_x - 1, origin_y - 1)
