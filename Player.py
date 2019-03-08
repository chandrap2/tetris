import time, pygame as pyg
import game_constants as g_const

class Square():

	def __init__(self):
		# uses screen dimensions for player placement
		self.screen_dim = g_const.screen_dim

		# surface to be displayed, rect to be transformed
		self.s_surface = g_const.face_surface
		self.s_surface = pyg.transform.scale(self.s_surface, (g_const.square_size, g_const.square_size))
		self.s_rect = self.s_surface.get_rect()

		self.x_block, self.y_block = 0, 0
		self.x_pixel, self.y_pixel = 0, 0

		self.prev_key_pressed = False
		self.left_state = False
		self.right_state = False

	def update(self, events, dt):
		self.player_event_listener(events)

		if left_state and x_block != 0:
			self.move_block(-1, 0)
		elif right_state and x_block < g_const.screen_w_blocks:
			self.move_block(1, 0)

	def player_event_listener(self, events):
		for event in events:
			if event.type == pyg.KEYDOWN:
				if not self.prev_key_pressed:
					if event.key == pyg.K_a:
						self.left_state = True
					elif event.key == pyg.K_d:
						self.right_state = True
					self.prev_key_pressed = True
				else:
					self.prev_key_pressed = False

	def get_pos(self):
		pos = (self.x_pixel, self.x_pixel)
		return pos

	def move_block(self, x, y):
		self.x_block += x
		self.y_block += y

	# # center player position
	# def reset_player(self):
	# 	self.p_rect.centery = self.screen_dim.h // 2
	#
	# def reset_score(self):
	# 	self.score = 0
	#
	# def create_game_won_ev(self, player_won_id):
	# 	event = g_const.GAMEWIN_EV
	# 	event.winning_player_id = player_won_id
	# 	return event
