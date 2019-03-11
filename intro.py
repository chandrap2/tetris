import pygame as pyg, time, sys
import game_constants as g_const

from random import randint
from Square import Square
import EventManager as evtMan

pyg.init() # initialize modules
# pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN, pyg.KEYUP, pyg.KEYDOWN]) # blocking unwanted events
# pyg.event.set_allowed([pyg.KEYUP, pyg.KEYDOWN, .GAMEREADY_ID]) # blocking unwanted events

fps = g_const.fps # desired framerate
frame_length = g_const.frame_length # in seconds

screen = g_const.screen
screen_dim = g_const.screen_dim

obj = Square()

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
			evtMan.process(pyg.event.get())
			events = pyg.event.get()

			obj.update(events)

			# draw background and objects
			screen.fill((0, 0, 0))
			screen.blit(obj.s_surface, obj.get_pixel_pos())

			# update display
			pyg.display.update()

def is_button_pressed(int_id): # return whether specified key was pressed at that moment
	pressed = pyg.key.get_pressed()[int_id]
	return pressed

main()
