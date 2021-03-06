import pygame as pyg, sys
import game_constants as g_const, util

from pygame.time import Clock as Clock

class EventManager:
	def __init__(self):
		self.current_manip = None # None for world update
		self.is_world_down = True # True if falling by gravity, False if falling due to player
		self.is_strafe_rot = False # True if rotating/strafing, False otherwise

		self.curr_world_ticks_index = 0

		self.move_down_manip_clock = Clock()
		self.strafe_rot_manip_clock = Clock()

		# for tracking time until appropriate updates
		self.move_down_secs = 0
		self.strafe_rot_secs = 0

	# updating movement clocks
	def update_clocks(self):
		self.move_down_secs += self.move_down_manip_clock.tick()
		self.strafe_rot_secs += self.strafe_rot_manip_clock.tick()

	# for starting world update ticks
	def start_world_update(self):
		self.is_world_down = True
		self.move_down_manip_clock = Clock()
		self.move_down_secs = 0 # reset timer

	# for starting manipulation update ticks
	def start_manip_update(self, manipulation):
		util.post_piece_manip_ev(manipulation)

		if manipulation == g_const.PIECE_MANIP_FALL_DOWN_ID:
			self.start_world_update()
			return # reset world_manip ticks, but don't change current_manip state

		# if manipulation is rotation or strafing
		elif manipulation >= g_const.PIECE_MANIP_LEFT_ID and manipulation <= g_const.PIECE_MANIP_CLOCKWISE_ID:
			if manipulation <= g_const.PIECE_MANIP_RIGHT_ID: # if manipulation is strafing
				if g_const.continue_strafe_while_key_held:
					self.is_strafe_rot = True

					self.strafe_rot_manip_clock = Clock()
					self.strafe_rot_secs = 0 # reset timer
				else: return # don't change current_manip state if action is not repeated

			else: # if manipulation is rotating
				if g_const.continue_rot_while_key_held:
					self.is_strafe_rot = True

					self.strafe_rot_manip_clock = Clock()
					self.strafe_rot_secs = 0
				else: return

		else: # down
			if g_const.continue_down_while_key_held:
				self.is_world_down = False # not falling to world ticks

				self.move_down_manip_clock = Clock()
				self.move_down_secs = 0
			else: return

		self.current_manip = manipulation

	# for stopping manip ticks
	def stop_manip_update(self):
		self.is_world_down = True
		self.is_strafe_rot = False

		self.current_manip = None

	def processEvents(self):
		self.update_clocks()
		self.post_movement_event(self.current_manip)

		events = pyg.event.get() # store, then clear event queue

		for event in events:

			if event.type == pyg.QUIT:
				sys.exit()

			if event.type == pyg.USEREVENT: # repost only custom events to event queue
				if event.cus_event == g_const.LEVEL_UP_ID:
					self.curr_world_ticks_index += 1

				pyg.event.post(event)
				continue

			# if a key is down and piece is not being manipulated at the moment
			if event.type == pyg.KEYDOWN and self.current_manip == None:
				if event.key == g_const.KEY_STRAFE_L:
					self.start_manip_update(g_const.PIECE_MANIP_LEFT_ID)
				elif event.key == g_const.KEY_STRAFE_R:
					self.start_manip_update(g_const.PIECE_MANIP_RIGHT_ID)
				elif event.key == g_const.KEY_ROT_CLOCK:
					self.start_manip_update(g_const.PIECE_MANIP_CLOCKWISE_ID)
				elif event.key == g_const.KEY_FALL:
					self.start_manip_update(g_const.PIECE_MANIP_FALL_DOWN_ID)
				elif event.key == g_const.KEY_DOWN:
					self.start_manip_update(g_const.PIECE_MANIP_DOWN_ID) # shape will fall down faster, world ticks will be stopped momentarily

			# if a key is released and piece is being manipulated at the moment
			if event.type == pyg.KEYUP and self.current_manip != None:
				if event.key == g_const.KEY_STRAFE_L and self.current_manip == g_const.PIECE_MANIP_LEFT_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_STRAFE_R and self.current_manip == g_const.PIECE_MANIP_RIGHT_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_ROT_CLOCK and self.current_manip == g_const.PIECE_MANIP_CLOCKWISE_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_FALL and self.current_manip == g_const.PIECE_MANIP_FALL_DOWN_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_DOWN and self.current_manip == g_const.PIECE_MANIP_DOWN_ID: # world ticks will resume
					self.stop_manip_update()
					self.start_world_update()

		events = pyg.event.get()
		return events

	def post_movement_event(self, current_manip):
		if self.is_world_down:
			# if self.move_down_secs >= g_const.dt_world_update:
			if self.move_down_secs >= 1000 * (g_const.dt_world_update_lookup[self.curr_world_ticks_index] / 60):
				self.move_down_secs = 0 # reset ticks
				util.post_custom_event(g_const.WORLD_UPDATE_ID)

		else: # down manip
			if self.move_down_secs >= g_const.dt_manip_update:
				self.move_down_secs = 0
				util.post_custom_event(g_const.PIECE_MANIP_DOWN_ID)

		if self.is_strafe_rot and self.strafe_rot_secs >= g_const.dt_manip_update:
			self.strafe_rot_secs = 0 # reset timer
			util.post_piece_manip_ev(current_manip)
