import pygame as pyg
import game_constants as g_const, util

from Shape1 import Shape1
from Terrain import Terrain

class Shape3(Shape1):
	"""
	0..
	123
	...
	"""
	def __init__(self, terrain):
		Shape1.__init__(self, terrain)
		for square in self.squares: square.set_surface(g_const.s3_surf)

		self.squares[1].move_to_block(0, 1)
		self.squares[2].move_to_block(1, 1)
		self.squares[3].move_to_block(2, 1)

		self.origin_block = self.squares[2]

	def rotate_clock(self):
		if not self.check_for_collision_around_origin():
			self.orient_state = (self.orient_state + 1 if self.orient_state != g_const.SHAPE_ORIENT_4 else g_const.SHAPE_ORIENT_1)
			origin_x, origin_y = self.origin_block.get_block_pos()

			if self.orient_state == g_const.SHAPE_ORIENT_1:
				self.squares[0].move_to_block(origin_x - 1, origin_y - 1)
				self.squares[1].move_to_block(origin_x - 1, origin_y)
				self.squares[3].move_to_block(origin_x + 1, origin_y)
			elif self.orient_state == g_const.SHAPE_ORIENT_2:
				self.squares[0].move_to_block(origin_x + 1, origin_y - 1)
				self.squares[1].move_to_block(origin_x, origin_y - 1)
				self.squares[3].move_to_block(origin_x, origin_y + 1)
			elif self.orient_state == g_const.SHAPE_ORIENT_3:
				self.squares[0].move_to_block(origin_x + 1, origin_y + 1)
				self.squares[1].move_to_block(origin_x + 1, origin_y)
				self.squares[3].move_to_block(origin_x - 1, origin_y)
			else:
				self.squares[0].move_to_block(origin_x - 1, origin_y + 1)
				self.squares[1].move_to_block(origin_x, origin_y + 1)
				self.squares[3].move_to_block(origin_x, origin_y - 1)
