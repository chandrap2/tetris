import pygame as pyg
import game_constants as g_const, util

class UIBox:
	def __init__(self, size, color, pos):
		self.box_surface = pyg.Surface(size)
		self.box_surface.fill(color)
		self.box_pos = pos

	def draw(self):
		g_const.screen.blit(self.box_surface, self.box_pos)
