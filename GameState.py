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

		# self.curr_shape = Shape1(self.terrain)
		self.curr_shape = util.gen_shape(terrain) # Shape currently being played
		self.next_shape = util.gen_shape(terrain) # Shape queued for after current shape has fallen

		self.row_sizes = [0 for y in range(g_const.arena_h_blocks)] # list storing number of dropped blocks in each row

		self.curr_state = g_const.PLAY_STATE # variable storing current game state
		self.level = 0 # current level
		self.line_clears = 0 # number of line clears in current level
		self.score = 0 # game score

	def update(self, events):
		self.terrain.update(events)
		self.process_events(events)

		if self.curr_state == g_const.PLAY_STATE:
			self.curr_shape.update(events)

	# update game
	def process_events(self, events):
		for event in events:
			if event.cus_event == g_const.PIECE_HIT_BOTTOM_ID: # if a piece has fallen
				# self.curr_shape = Shape1(self.terrain)	# for testing
				self.curr_shape = self.next_shape
				self.next_shape = util.gen_shape(self.terrain)
				are_rows_full = False
				full_rows = [] # list for storing row indices of full rows

				for square in event.params:
					y = square.y_block
					self.row_sizes[y] += 1

					# if a row is full
					if self.row_sizes[y] == g_const.arena_w_blocks:
						full_rows.append(y)

						self.line_clears += 1
						if self.line_clears == 10: # leveling up
							self.line_clears = 0
							self.level += 1

						are_rows_full = True

				if are_rows_full:
					self.calculate_score(len(full_rows)) # Update score if rows filled up
					print("Score:", self.score)

					util.post_custom_event(g_const.ROW_FULL_ID, full_rows)
					self.collapse_row_sizes()

	# collapsing row_sizes at full rows
	def collapse_row_sizes(self):
		temp = [0 for y in range(g_const.arena_h_blocks)]
		curr_y = g_const.arena_h_blocks - 1 # curr location in self.row_sizes
		temp_y = g_const.arena_h_blocks - 1 # curr location in temp list

		while curr_y >= 0:
			# ignoring full rows, adding non-full rows to temp
			if self.row_sizes[curr_y] != g_const.arena_w_blocks:
				temp[temp_y] = self.row_sizes[curr_y]
				curr_y -= 1
				temp_y -= 1
				continue
			curr_y -= 1

		self.row_sizes = temp

	# Increment score according to number of full rows and current level
	def calculate_score(self, num_rows):
		if num_rows == 1:
			self.score += 40 * (self.level + 1)
		elif num_rows == 2:
			self.score += 100 * (self.level + 1)
		elif num_rows == 3:
			self.score += 300 * (self.level + 1)
		elif num_rows == 4:
			self.score += 1200 * (self.level + 1)
