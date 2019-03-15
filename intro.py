import pygame as pyg, time, sys
import game_constants as g_const

from random import randint
from Square import Square
from Shape import Shape
import EventManager as evtMan

pyg.init() # initialize modules
# pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN, pyg.KEYUP, pyg.KEYDOWN]) # blocking unwanted events
# pyg.event.set_allowed([pyg.KEYUP, pyg.KEYDOWN, .GAMEREADY_ID]) # blocking unwanted events

fps = g_const.fps # desired framerate
frame_length = g_const.frame_length # in seconds

screen = g_const.screen
screen_dim = g_const.screen_dim

# squares = [Square()]
shapes = [Shape()]

def main():
	start = time.time()
	evtMan.start_world_update()

	while 1:
		dt = time.time() - start

		if dt >= frame_length:
			# if 1 / dt < 58: print(1 / dt)
			# print(1 / dt)
			start = time.time() # reset start tick

			# handle events
			evtMan.processEvents()
			events = pyg.event.get()

			for event in events:
				# if event.type == g_const.PIECE_HIT_BOTTOM: squares.append(Square())
				if event.type == g_const.PIECE_HIT_BOTTOM_ID: shapes.append(Shape())

			# draw background and objects
			screen.fill((0, 0, 0))
			for shape in shapes:
				if not shape.has_hit_bottom: shape.update(events)
				shape.draw()

			# update display
			pyg.display.update()

main()
