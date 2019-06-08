import pygame as pyg
import game_constants as g_const, util

from Shape1 import Shape1
from Terrain import Terrain

class Shape7(Shape1):
	"""
	o0..
	.1..
	.2..
	.3..
	"""
	def __init__(self, terrain):
		Shape1.__init__(self, terrain)
		for square in self.squares: square.set_surface(g_const.s7_surf)

		self.squares[0].move_to_block(0, 0)
		self.squares[1].move_to_block(0, 1)
		self.squares[2].move_to_block(0, 2)
		self.squares[3].move_to_block(0, 3)

		self.ref_x_block, self.ref_y_block = -1, 0 # origin is top left of 4x4 bounding rect

	def rotate_clock(self):
		if not self.check_for_collision_around_origin():
			self.orient_state = (self.orient_state + 1 if self.orient_state != g_const.SHAPE_ORIENT_4 else g_const.SHAPE_ORIENT_1)

			if self.orient_state == g_const.SHAPE_ORIENT_1:
				self.squares[0].move_to_block(self.ref_x_block + 1, self.ref_y_block)
				self.squares[1].move_to_block(self.ref_x_block + 1, self.ref_y_block + 1)
				self.squares[2].move_to_block(self.ref_x_block + 1, self.ref_y_block + 2)
				self.squares[3].move_to_block(self.ref_x_block + 1, self.ref_y_block + 3)
			elif self.orient_state == g_const.SHAPE_ORIENT_2:
				self.squares[0].move_to_block(self.ref_x_block + 3, self.ref_y_block + 1)
				self.squares[1].move_to_block(self.ref_x_block + 2, self.ref_y_block + 1)
				self.squares[2].move_to_block(self.ref_x_block + 1, self.ref_y_block + 1)
				self.squares[3].move_to_block(self.ref_x_block, self.ref_y_block + 1)
			elif self.orient_state == g_const.SHAPE_ORIENT_3:
				self.squares[0].move_to_block(self.ref_x_block + 2, self.ref_y_block + 3)
				self.squares[1].move_to_block(self.ref_x_block + 2, self.ref_y_block + 2)
				self.squares[2].move_to_block(self.ref_x_block + 2, self.ref_y_block + 1)
				self.squares[3].move_to_block(self.ref_x_block + 2, self.ref_y_block)
			else:
				self.squares[0].move_to_block(self.ref_x_block, self.ref_y_block + 2)
				self.squares[1].move_to_block(self.ref_x_block + 1, self.ref_y_block + 2)
				self.squares[2].move_to_block(self.ref_x_block + 2, self.ref_y_block + 2)
				self.squares[3].move_to_block(self.ref_x_block + 3, self.ref_y_block + 2)

	def move_left_one_block(self):
		for square in self.squares:
			if self.terrain.check_for_collision_to_left(square):
				return

		self.ref_x_block -= 1
		for square in self.squares:
			square.move_to_left(1)

	def move_down_one_block(self):
		for square in self.squares:
			if self.terrain.check_for_collision_below(square):
				self.has_hit_bottom = True # updates shape state if any square is touching something below it
				return

		self.ref_y_block += 1
		for square in self.squares:
			square.move_down(1)

	def move_right_one_block(self):
		for square in self.squares:
			if self.terrain.check_for_collision_to_right(square):
				return

		self.ref_x_block += 1
		for square in self.squares:
			square.move_to_right(1)

	# used when trying to rotate
	def check_for_collision_around_origin(self):
		for col in range(self.ref_x_block, self.ref_x_block + 4):
			for row in range(self.ref_y_block, self.ref_y_block + 4):
				# can't rotate if something's inside bounding rect
				if (col < 0 or col >= g_const.arena_w_blocks) or \
				(row < 0 or row >= g_const.arena_h_blocks) or \
				self.terrain.game_map[row][col] != None:
					return True

		return False
