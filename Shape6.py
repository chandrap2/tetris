import pygame as pyg
import game_constants as g_const, util

from Shape1 import Shape1
from Terrain import Terrain

class Shape6(Shape1):
	"""
	01.
	23.
	...
	Can't rotate
	"""
	def __init__(self, terrain):
		Shape1.__init__(self, terrain)
		for square in self.squares: square.set_surface(g_const.s6_surf)

		self.squares[0].move_to_block(0, 0)
		self.squares[1].move_to_block(1, 0)
		self.squares[2].move_to_block(0, 1)
		self.squares[3].move_to_block(1, 1)
		self.origin_block = self.squares[0] # only used for moving shape to center of screen

		self.set_init_origin_x(g_const.arena_w_blocks // 2)

	def update(self, events):
		if not self.has_hit_bottom:

			for event in events:
				if event.cus_event == g_const.WORLD_UPDATE_ID or event.cus_event == g_const.PIECE_MANIP_DOWN_ID or event.cus_event == g_const.PIECE_MANIP_FALL_DOWN_ID:
					if not event.cus_event == g_const.PIECE_MANIP_FALL_DOWN_ID: self.move_down_one_block()
					else: self.fall_down()

					if self.has_hit_bottom:
						util.post_custom_event(g_const.PIECE_HIT_BOTTOM_ID, [square for square in self.squares])
						break # stop processing any other commands if fallen

				elif event.cus_event == g_const.PIECE_MANIP_LEFT_ID:
					self.move_left_one_block()

				elif event.cus_event == g_const.PIECE_MANIP_RIGHT_ID:
					self.move_right_one_block()
