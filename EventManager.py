import pygame as pyg, sys
import game_constants as g_const, util

class EventManager:
	def __init__(self):
		self.current_manip = None
		self.is_world_down = True # True if falling by gravity, False if falling due to player
		self.is_strafe_rot = False

		self.move_down_manip_clock = pyg.time.Clock()
		self.strafe_rot_manip_clock = pyg.time.Clock()

	# for starting world update ticks
	def start_world_update(self):
		self.is_world_down = True
		self.move_down_manip_clock = Clock()
		self.move_down_manip_clock.tick()

	# for starting manipulation update ticks
	def start_manip_update(self, manipulation):
		util.post_piece_manip_ev(manipulation)

		if manipulation == g_const.PIECE_MANIP_FALL_DOWN_ID:
			self.start_world_update()
			return # reset world_manip ticks, but don't change current_manip state

		elif manipulation == g_const.PIECE_MANIP_LEFT_ID or manipulation == g_const.PIECE_MANIP_RIGHT_ID:
			if g_const.continue_strafe_while_key_held:
				self.is_strafe_rot = True

				self.strafe_rot_manip_clock = Clock()
				self.strafe_rot_manip_clock.tick()
			else: return # don't change current_manip state if action is not repeated

		elif manipulation == g_const.PIECE_MANIP_CLOCK_ID:
			if g_const.continue_rot_while_key_held:
				self.is_strafe_rot = True

				self.strafe_rot_manip_clock = Clock()
				self.strafe_rot_manip_clock.tick()
			else: return

		else: # down
			if g_const.continue_down_while_key_held:
				self.is_world_down = False

				self.move_down_manip_clock = Clock()
				self.move_down_manip_clock.tick()
			else: return

		self.current_manip = manipulation

	# for stopping manip ticks
	def stop_manip_update(self):
		self.is_world_down = True
		self.is_strafe_rot = False

		self.current_manip = None

	def processEvents(self):
		self.post_move_down_event()
		self.post_strafe_rot_event(self.current_manip)

		events = pyg.event.get() # store, then clear event queue

		for event in events:

			if event.type == pyg.QUIT:
				sys.exit()

			if event.type == pyg.USEREVENT: # repost only custom events to event queue
				pyg.event.post(event)
				continue

			# if not ev_con_one.manipulating_piece and event.type == pyg.KEYDOWN:
			if event.type == pyg.KEYDOWN and self.current_manip == None:
				if event.key == g_const.KEY_STRAFE_L:
					self.start_manip_update(g_const.PIECE_MANIP_LEFT_ID)
				elif event.key == g_const.KEY_STRAFE_R:
					self.start_manip_update(g_const.PIECE_MANIP_RIGHT_ID)
				elif event.key == g_const.KEY_ROT_CLOCK:
					self.start_manip_update(g_const.PIECE_MANIP_CLOCK_ID)
				elif event.key == g_const.KEY_FALL:
					self.start_manip_update(g_const.PIECE_MANIP_FALL_DOWN_ID)
				elif event.key == g_const.KEY_DOWN:
					self.start_manip_update(g_const.PIECE_MANIP_DOWN_ID) # shape will fall down faster, world ticks will be stopped momentarily

			if event.type == pyg.KEYUP and self.current_manip != None:
				if event.key == g_const.KEY_STRAFE_L and self.current_manip == g_const.PIECE_MANIP_LEFT_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_STRAFE_R and self.current_manip == g_const.PIECE_MANIP_RIGHT_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_ROT_CLOCK and self.current_manip == g_const.PIECE_MANIP_CLOCK_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_FALL and self.current_manip == g_const.PIECE_MANIP_FALL_DOWN_ID:
					self.stop_manip_update()
				elif event.key == g_const.KEY_DOWN and self.current_manip == g_const.PIECE_MANIP_DOWN_ID: # world ticks will resume
					self.stop_manip_update()
					self.start_world_update()

		events = pyg.event.get()
		return events

	def post_move_down_event(self):
		if is_world_down:
			if move_down_manip_clock.tick() >= g_const.dt_world_update:
				pyg.event.post(pyg.event.Event(pyg.USEREVENT, event = g_const.WORLD_UPDATE_ID, params = []))

		else: # down manip
			if move_down_manip_clock.tick() >= g_const.dt_manip_update:
				pyg.event.post(pyg.event.Event(pyg.USEREVENT, event = g_const.PIECE_MANIP_DOWN_ID, params = []))

	def post_strafe_rot_event(self, manipulation):
		if strafe_rot_manip_clock.tick() >= g_const.dt_manip_update:
			util.post_piece_manip_ev(manipulation)
