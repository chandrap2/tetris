import time, pygame as pyg
import game_constants as g_const, util

from Square import Square

class Shape():

	def __init__(self):
		self.screen = g_const.screen

		self.squares = [Square(), Square(1, 0), Square(1, 1), Square(2, 1)]

		self.orient_state = g_const.SHAPE_ORIENT_1
		self.has_hit_bottom = False

	def update(self, events):
		if not self.has_hit_bottom:

			for event in events:
				if event.type == g_const.WORLD_UPDATE_ID or event.type == g_const.PIECE_MANIP_DOWN_ID:
					for square in self.squares:
						if square.has_hit_bottom:
							self.has_hit_bottom = True
							break

					if self.has_hit_bottom:
						pyg.event.post(pyg.event.Event(g_const.PIECE_HIT_BOTTOM_ID))
					else:
						self.move_down_one_block()

				elif event.type == g_const.PIECE_MANIP_LEFT_ID:
					self.move_left_one_block()

				elif event.type == g_const.PIECE_MANIP_RIGHT_ID:
					self.move_right_one_block()

				elif event.type == g_const.PIECE_MANIP_CLOCK_ID:
					# print(event)
					self.rotate_clock()

	def rotate_clock(self):
		self.orient_state = (self.orient_state + 1 if self.orient_state != g_const.SHAPE_ORIENT_4 else g_const.SHAPE_ORIENT_1)

		origin_x, origin_y = self.squares[1].get_block_pos()

		if self.orient_state == g_const.SHAPE_ORIENT_1 or self.orient_state == g_const.SHAPE_ORIENT_3:
			self.squares[0].move_to_block(origin_x - 1, origin_y)
			self.squares[2].move_to_block(origin_x, origin_y + 1)
			self.squares[3].move_to_block(origin_x + 1, origin_y + 1)
		else:
			self.squares[0].move_to_block(origin_x, origin_y - 1)
			self.squares[2].move_to_block(origin_x - 1, origin_y)
			self.squares[3].move_to_block(origin_x - 1, origin_y + 1)

	def move_down_one_block(self):
		self.move_blocks(0, 1)

	def move_left_one_block(self):
		self.move_blocks(-1, 0)

	def move_right_one_block(self):
		self.move_blocks(1, 0)

	def move_blocks(self, dx, dy):
		for square in self.squares:
			square.move_blocks(dx, dy)

	# def move_to_block(self, x, y):
	# 	self.squares[0].move_to_block(x, y)
	# 	self.squares[1].move_to_block(x + 1, y)
	# 	self.squares[2].move_to_block(x + 1, y + 1)
	# 	self.squares[3].move_to_block(x + 1, y + 2)

	def draw(self):
		for square in self.squares:
			self.screen.blit(square.s_surface, square.get_pixel_pos())
