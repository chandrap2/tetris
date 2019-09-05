import pygame as pyg
import game_constants as g_const, util

from Square import Square
from Terrain import Terrain

class Shape1():
	"""
	...
	01.
	.23
	"""
	def __init__(self, terrain):
		# self.screen = g_const.screen
		self.terrain = terrain

		self.squares = [Square(), Square(1, 0), Square(1, 1), Square(2, 1)]
		# for square in self.squares:
		# 	square.move_up(1)

		self.origin_block = self.squares[1] # second element is square of reference
		self.set_init_origin_x(g_const.arena_w_blocks // 2)

		self.orient_state = g_const.SHAPE_ORIENT_1
		self.has_hit_bottom = False

	## NOTE: update update() overwritten in Shape6 after any edits here
	def update(self, events):
		if not self.has_hit_bottom:

			for event in events:
				if event.cus_event == g_const.WORLD_UPDATE_ID or event.cus_event == g_const.PIECE_MANIP_DOWN_ID or event.cus_event == g_const.PIECE_MANIP_FALL_DOWN_ID:
					if event.cus_event != g_const.PIECE_MANIP_FALL_DOWN_ID: self.move_down_one_block()
					else: self.fall_down()

					if self.has_hit_bottom:
						util.post_custom_event(g_const.PIECE_HIT_BOTTOM_ID, [square for square in self.squares])
						break # stop processing any other commands if fallen

				elif event.cus_event == g_const.PIECE_MANIP_LEFT_ID:
					self.move_left_one_block()

				elif event.cus_event == g_const.PIECE_MANIP_RIGHT_ID:
					self.move_right_one_block()

				elif event.cus_event == g_const.PIECE_MANIP_CLOCKWISE_ID:
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
			if self.terrain.check_for_collision_to_left(square):
				return

		for square in self.squares:
			square.move_to_left(1)

	def move_down_one_block(self):
		for square in self.squares:
			if self.terrain.check_for_collision_below(square):
				self.has_hit_bottom = True # updates shape state if any square is touching something below it
				return

		for square in self.squares:
			square.move_down(1)

	def fall_down(self):
		dy = g_const.arena_h_blocks
		for square in self.squares:
			dy = min(dy, self.terrain.highestBelow(square) - square.y_block)

		for square in self.squares:
			square.move_down(dy)

		self.has_hit_bottom = True

	def move_right_one_block(self):
		for square in self.squares:
			if self.terrain.check_for_collision_to_right(square):
				return

		for square in self.squares:
			square.move_to_right(1)

	# used when trying to rotate, checking that 1-block radius around origin block is completely free
	def check_for_collision_around_origin(self):
		for col in range(self.origin_block.x_block - 1, self.origin_block.x_block + 2):
			for row in range(self.origin_block.y_block - 1, self.origin_block.y_block + 2):
				if col == self.origin_block.x_block and row == self.origin_block.y_block: continue # ignore pos of origin block

				# can't rotate if something's inside bounding rect
				if (col < 0 or col >= g_const.arena_w_blocks) or \
				(row < 0 or row >= g_const.arena_h_blocks) or \
				self.terrain.game_map[row][col] != None:
					return True

		return False

	def set_init_origin_x(self, x):
		if self.origin_block == None: return

		dx = x - self.origin_block.x_block
		for square in self.squares:
			if not (self.origin_block.x_block == square.x_block and \
			self.origin_block.y_block == square.y_block):
				square.move_to_block(square.x_block + dx, square.y_block)

		self.origin_block.move_to_block(x, self.origin_block.y_block)

	def draw(self):
		for square in self.squares:
			if square.y_block >= 0:
				square.draw()
