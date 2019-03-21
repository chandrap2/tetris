import time, pygame as pyg
import game_constants as g_const, util

from Square import Square
from Terrain import Terrain

class Shape():

	def __init__(self, terrain):
		self.screen = g_const.screen
		self.terrain = terrain

		self.squares = [Square(terrain), Square(terrain, 1, 0), Square(terrain, 1, 1), Square(terrain, 2, 1)] # second element is square of reference

		self.orient_state = g_const.SHAPE_ORIENT_1
		self.has_hit_bottom = False

	def update(self, events):
		if not self.has_hit_bottom:

			for event in events:
				# print()
				if event.type == g_const.WORLD_UPDATE_ID or event.type == g_const.PIECE_MANIP_DOWN_ID:
					self.move_down_one_block()

					if self.has_hit_bottom:
						pyg.event.post(pyg.event.Event(g_const.PIECE_HIT_BOTTOM_ID))

						for square in self.squares:
							pyg.event.post(pyg.event.Event(g_const.SQUARE_COOR_ID, x = square.x_block, y = square.y_block))

				if event.type == g_const.PIECE_MANIP_LEFT_ID:
					self.move_left_one_block()

				elif event.type == g_const.PIECE_MANIP_RIGHT_ID:
					self.move_right_one_block()

				elif event.type == g_const.PIECE_MANIP_CLOCK_ID:
					# print(event)
					self.rotate_clock()

	def rotate_clock(self):
		self.orient_state = (g_const.SHAPE_ORIENT_2 if self.orient_state == g_const.SHAPE_ORIENT_1 else g_const.SHAPE_ORIENT_1)

		origin_x, origin_y = self.squares[1].get_block_pos()

		if self.orient_state == g_const.SHAPE_ORIENT_1:
			if not self.squares[0].check_for_collision_coordinate(origin_x - 1, origin_y) and \
			not self.squares[2].check_for_collision_coordinate(origin_x, origin_y + 1) and \
			not self.squares[3].check_for_collision_coordinate(origin_x + 1, origin_y + 1):
				self.squares[0].move_to_block(origin_x - 1, origin_y)
				self.squares[2].move_to_block(origin_x, origin_y + 1)
				self.squares[3].move_to_block(origin_x + 1, origin_y + 1)
		else:
			if not self.squares[0].check_for_collision_coordinate(origin_x, origin_y - 1) and \
			not self.squares[2].check_for_collision_coordinate(origin_x - 1, origin_y) and \
			not self.squares[3].check_for_collision_coordinate(origin_x - 1, origin_y + 1):
				self.squares[0].move_to_block(origin_x, origin_y - 1)
				self.squares[2].move_to_block(origin_x - 1, origin_y)
				self.squares[3].move_to_block(origin_x - 1, origin_y + 1)

	def move_left_one_block(self):
		# self.move_blocks(-1, 0, terrain)

		for square in self.squares:
			if square.check_for_collision_to_left():
				return

		for square in self.squares:
			square.move_to_left(1)

	def move_down_one_block(self):
		# self.move_blocks(0, 1, terrain)

		for square in self.squares:
			if square.check_for_collision_below():
				self.has_hit_bottom = True
				return

		for square in self.squares:
			square.move_down(1)

	def move_right_one_block(self):
		# self.move_blocks(1, 0, terrain)

		for square in self.squares:
			if square.check_for_collision_to_right():
				return

		for square in self.squares:
			square.move_to_right(1)

	def draw(self):
		for square in self.squares:
			self.screen.blit(square.s_surface, square.get_pixel_pos())
