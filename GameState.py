import pygame as pyg, time

import game_constants as g_const
import util

from Square import Square
from Shapes import *
from Terrain import Terrain
from EventManager import EventManager

from UIBox import UIBox

class GameState:
	def __init__(self, terrain):
		self.terrain = terrain

		self.curr_shape = util.gen_shape(terrain)
		self.next_shape = util.gen_shape(terrain)

		self.row_sizes = [0 for y in range(g_const.arena_h_blocks)]

		self.curr_state = g_const.PLAY_STATE
		self.score = 0

	def update(self, events):
		self.terrain.update(events)
		self.process_events(events)

		if self.curr_state == g_const.PLAY_STATE:
			self.curr_shape.update(events)

	def process_events(self, events):
		for event in events:
			if event.type == g_const.PIECE_HIT_BOTTOM_ID:
				self.curr_shape = self.next_shape
				self.next_shape = util.gen_shape(self.terrain)
			if event.type == g_const.SQUARE_COOR_ID:
				self.row_sizes[event.y] += 1

				if self.row_sizes[event.y] == g_const.arena_w_blocks:
					pyg.event.post(pyg.event.Event(g_const.ROW_FULL_ID, y = event.y))
