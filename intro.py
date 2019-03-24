import pygame as pyg, time
from random import randint

import game_constants as g_const
import EventManager as evtMan

from Shape4 import Shape4
from Terrain import Terrain

pyg.init() # initialize modules
pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN]) # blocking unwanted events

frame_length = g_const.frame_length # in seconds
screen = g_const.screen
screen_dim = g_const.screen_dim

def main():
	terrain = Terrain()
	shapes = [Shape4(terrain)]

	start = time.time()
	evtMan.start_world_update()

	while True:
		dt = time.time() - start

		if dt >= frame_length:
			start = time.time() # reset start tick

			# handle events
			events = evtMan.processEvents()

			for event in events:
				if event.type == g_const.PIECE_HIT_BOTTOM_ID: shapes.append(Shape4(terrain))

			terrain.update(events)

			# draw background and objects
			screen.fill((0, 0, 0))
			for shape in shapes:
				shape.update(events)
				shape.draw()

			# update display
			pyg.display.update()

main()
