import pygame as pyg, time
from random import randint

import game_constants as g_const
import EventManager as evtMan

from Shapes import *
from Terrain import Terrain
from EventManager import EventManager
from GameState import GameState

from UIBox import UIBox

pyg.init() # initialize modules
pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN]) # blocking unwanted events

frame_length = g_const.frame_length # in seconds
screen = g_const.screen

def main():
	background = UIBox(g_const.screen_size, (0, 0, 0), (0, 0))
	arena = UIBox(g_const.arena_size, (50, 50, 50), g_const.arena_pos)
	sidebar = UIBox(g_const.sidebar_size, (50, 50, 50), g_const.sidebar_pos)
	background.draw()
	sidebar.draw()

	evt_man = EventManager()
	terrain = Terrain()
	game_state = GameState(terrain)

	start = time.time()
	evt_man.start_world_update()

	while True:
		dt = time.time() - start

		if dt >= frame_length:
			start = time.time() # reset start tick

			events = evt_man.processEvents() # handle events

			game_state.update(events)

			# draw background and objects
			arena.draw()
			game_state.curr_shape.draw()

			for col in terrain.game_map:
				for square in col:
					if square != None: square.draw()

			# update display
			pyg.display.update()

main()
