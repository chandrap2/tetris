import pygame as pyg
import game_constants as g_const, util

class Background:
	def __init__(self):
		self.back_surface = pyg.transform.scale(g_const.face_surface, g_const.screen_size)

	def draw(self):
		# g_const.screen.blit(self.back_surface, (0, 0))
		g_const.screen.fill((0, 0, 0))
