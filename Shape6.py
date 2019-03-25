import pygame as pyg
import game_constants as g_const, util

from Shape1 import Shape1
from Terrain import Terrain

class Shape6(Shape1):
	"""
	01.
	23.
	...
	"""
	def __init__(self, terrain):
		Shape1.__init__(self, terrain)

		self.squares[2].move_to_block(0, 1)
		self.squares[3].move_to_block(1, 1)

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
