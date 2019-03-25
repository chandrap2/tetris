import pygame as pyg
import game_constants as g_const, util

from Square import Square
from Terrain import Terrain

class Shape1():

	"""
	01.
	.23
	...
	"""

	def __init__(self, terrain):
		self.screen = g_const.screen
		self.terrain = terrain

		self.squares = [Square(terrain), Square(terrain, 1, 0), Square(terrain, 1, 1), Square(terrain, 2, 1)]
		self.origin_block = self.squares[1] # second element is square of reference

		self.orient_state = g_const.SHAPE_ORIENT_1
		self.has_hit_bottom = False

	def update(self, events):
		if not self.has_hit_bottom:

			for event in events:
				if event.type == g_const.WORLD_UPDATE_ID or event.type == g_const.PIECE_MANIP_DOWN_ID:
					self.move_down_one_block()

					if self.has_hit_bottom:
						pyg.event.post(pyg.event.Event(g_const.PIECE_HIT_BOTTOM_ID))

						for square in self.squares:
							pyg.event.post(pyg.event.Event(g_const.SQUARE_COOR_ID, x = square.x_block, y = square.y_block)) # events holding coords of each square

					break

				elif event.type == g_const.PIECE_MANIP_LEFT_ID:
					self.move_left_one_block()

				elif event.type == g_const.PIECE_MANIP_RIGHT_ID:
					self.move_right_one_block()

				elif event.type == g_const.PIECE_MANIP_CLOCK_ID:
					# print("rotate")
					self.rotate_clock()

	def rotate_clock(self):
		if not self.check_for_collision_around_origin():
			self.orient_state = (g_const.SHAPE_ORIENT_2 if self.orient_state == g_const.SHAPE_ORIENT_1 else g_const.SHAPE_ORIENT_1)
			origin_x, origin_y = self.origin_block.get_block_pos()

			if self.orient_state == g_const.SHAPE_ORIENT_1:
				self.squares[0].move_to_block(origin_x - 1, origin_y)
				self.squares[2].move_to_block(origin_x, origin_y + 1)
				self.squares[3].move_to_block(origin_x + 1, origin_y + 1)
			else:
				self.squares[0].move_to_block(origin_x, origin_y - 1)
				self.squares[2].move_to_block(origin_x - 1, origin_y)
				self.squares[3].move_to_block(origin_x - 1, origin_y + 1)

	def move_left_one_block(self):
		for square in self.squares:
			if square.check_for_collision_to_left():
				return

		for square in self.squares:
			square.move_to_left(1)

	def move_down_one_block(self):
		for square in self.squares:
			if square.check_for_collision_below():
				self.has_hit_bottom = True # updates shape state if any square is touching something below it
				return

		for square in self.squares:
			square.move_down(1)

	def move_right_one_block(self):
		for square in self.squares:
			if square.check_for_collision_to_right():
				return

		for square in self.squares:
			square.move_to_right(1)

	# used when trying to rotate
	def check_for_collision_around_origin(self):
		for col in range(self.origin_block.x_block - 1, self.origin_block.x_block + 2):
			for row in range(self.origin_block.y_block - 1, self.origin_block.y_block + 2):
				if col == self.origin_block.x_block and row == self.origin_block.y_block: continue

				if (col < 0 or col >= g_const.screen_w_blocks) or \
				(row < 0 or col >= g_const.screen_h_blocks) or \
				self.terrain.game_map[col][row]:
					return True
		return False

	def draw(self):
		for square in self.squares:
			self.screen.blit(square.s_surface, square.get_pixel_pos())
