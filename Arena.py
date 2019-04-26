import pygame as pyg
import game_constants as g_const, util

class Arena:
	def __init__(self):
		self.arena_surface = pyg.Surface(g_const.arena_size)
		self.arena_surface.fill((50, 50, 50))

	def draw(self):
		g_const.screen.blit(self.arena_surface, (g_const.UI_LEFT_MARGIN, g_const.UI_TOP_MARGIN))
