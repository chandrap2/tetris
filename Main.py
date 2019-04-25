import pygame as pyg, time
from random import randint

import game_constants as g_const
import EventManager as evtMan

from Shapes import *
from Terrain import Terrain

pyg.init() # initialize modules
pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN]) # blocking unwanted events

frame_length = g_const.frame_length # in seconds
screen = g_const.screen
screen_dim = g_const.screen_dim

def main():
	terrain = Terrain()
	shapes = [gen_shape(terrain)]

	start = time.time()
	evtMan.start_world_update()

	while True:
		dt = time.time() - start

		if dt >= frame_length:
			start = time.time() # reset start tick

			events = evtMan.processEvents() # handle events

			for event in events:
				if event.type == g_const.PIECE_HIT_BOTTOM_ID: shapes.append(gen_shape(terrain)) # spawn new shape if a shape has fallen

			terrain.update(events)

			# draw background and objects
			screen.fill((0, 0, 0))
			for shape in shapes:
				shape.update(events)
				shape.draw()

			# update display
			pyg.display.update()

def gen_shape(terrain):
	rand = randint(1, 7)

	if rand == 1: return Shape1(terrain)
	if rand == 2: return Shape2(terrain)
	if rand == 3: return Shape3(terrain)
	if rand == 4: return Shape4(terrain)
	if rand == 5: return Shape5(terrain)
	if rand == 6: return Shape6(terrain)
	if rand == 7: return Shape7(terrain)

main()
