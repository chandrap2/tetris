import pygame as pyg
import game_constants as g_const, util

class Square():
	def __init__(self, init_x_block = 0, init_y_block = 0):
		# surface to be displayed, rect to be transformed
		self.s_surface = pyg.transform.scale(g_const.face_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect() # pos is (0, 0)

		self.x_block, self.y_block = init_x_block, init_y_block
		self.update_pixel_pos()

	def move_to_left(self, dx):
		self.x_block -= abs(dx)
		self.update_pixel_pos()

	def move_down(self, dy):
		self.y_block += abs(dy)
		self.update_pixel_pos()

	def move_to_right(self, dx):
		self.x_block += abs(dx)
		self.update_pixel_pos()

	def move_to_block(self, x, y):
		self.x_block = x
		self.y_block = y
		self.update_pixel_pos()

	# update pixel position of Rect instance
	def update_pixel_pos(self):
		self.s_rect.x = self.x_block * g_const.square_size + g_const.UI_BOX_MARGIN # offset by arena margins
		self.s_rect.y = self.y_block * g_const.square_size + g_const.UI_BOX_MARGIN

	def get_block_pos(self):
		return (self.x_block, self.y_block)

	def get_pixel_pos(self):
		return (self.s_rect.x, self.s_rect.y)

	def draw(self):
		g_const.screen.blit(self.s_surface, self.get_pixel_pos())
