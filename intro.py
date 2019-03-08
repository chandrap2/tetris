import pygame as pyg, time, sys
import game_constants as g_const

from random import randint
from Player import Square
from EventManager import EventManager as evtMan
# from Ball import Ball
# from TextBox import TextBox

pyg.init() # initialize modules
# pyg.event.set_blocked([pyg.MOUSEMOTION, pyg.MOUSEBUTTONUP, pyg.MOUSEBUTTONDOWN, pyg.KEYUP, pyg.KEYDOWN]) # blocking unwanted events
# pyg.event.set_allowed([pyg.KEYUP, pyg.KEYDOWN, g_const.GAMEREADY_ID]) # blocking unwanted events

fps = g_const.fps # desired framerate
frame_length = g_const.frame_length # in seconds

screen = g_const.screen
screen_dim = g_const.screen_dim

obj = Square()

# game_text_font = g_const.game_text_font
# game_text_color = g_const.game_text_color

# p1 = Player(True)
# p2 = Player(False)
# ball = Ball()

def main():
	start = time.time()
	evtMan.start_world_update()

	while 1:
		dt = time.time() - start

		if dt >= frame_length:
			# if 1 / dt < 58: print(1 / dt)
			# print(1 / dt)
			start = time.time() # reset start tick

			world_update = False
			# handle events
			events = pyg.event.get()

			for event in events:
				if event.type == pyg.QUIT:
					sys.exit()
				if event.type == g_const.WORLD_UPDATE_ID:
					# world_update = True
					print(event)

			dt += time.time() - start
			# # draw background and objects
			screen.fill((0, 0, 0))

			# if world_update:
			# 	screen.blit(obj.s_surface, obj.get_pos())
			# update display
			pyg.display.update()

def is_button_pressed(int_id): # return whether specified key was pressed at that moment
	pressed = pyg.key.get_pressed()[int_id]
	return pressed

main()
