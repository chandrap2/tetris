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
			if event.cus_event == g_const.PIECE_HIT_BOTTOM_ID:
				self.curr_shape = self.next_shape
				self.next_shape = util.gen_shape(self.terrain)
				is_row_full = False

				for square_pos in event.params:
					y = square_pos[1]
					self.row_sizes[y] += 1
					if self.row_sizes[y] == g_const.arena_w_blocks:
						util.post_custom_event(g_const.ROW_FULL_ID, [y])
						print("fullaaa")
						is_row_full = True

				if is_row_full:
					print(self.row_sizes)
					print()
					self.collapse_row_sizes()

	def collapse_row_sizes(self):
		# y = g_const.arena_h_blocks - 1
		# while y >= 0:
		# 	if self.row_sizes[y] == g_const.arena_w_blocks:
		# 		for j in range(y, -1, -1):
		# 			self.row_sizes[j] = self.row_sizes[j - 1] if j > 0 else 0
		# 		continue
		# 	y -= 1
		temp = [0 for y in range(g_const.arena_h_blocks)]
		curr_y = g_const.arena_h_blocks - 1 # curr location in self.row_sizes
		temp_y = g_const.arena_h_blocks - 1 # curr location in temp list

		while curr_y >= 0:
			if self.row_sizes[curr_y] != g_const.arena_w_blocks:
				temp[temp_y] = self.row_sizes[curr_y]
				curr_y -= 1
				temp_y -= 1
				continue
			curr_y -= 1

		self.row_sizes = temp
