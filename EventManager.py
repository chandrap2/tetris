import pygame as pyg, sys
import game_constants as g_const, util

class EventManager:
	def __init__(self):
		self.current_manip = None

	# for starting world update ticks
	def start_world_update(self):
		pyg.time.set_timer(g_const.WORLD_UPDATE_ID, g_const.dt_world_update)

	# for stopping world update ticks
	def stop_world_update(self):
		pyg.time.set_timer(g_const.WORLD_UPDATE_ID, 0)

	# for starting manipulation update ticks
	def start_manip_update(self, manipulation):
		pyg.event.post(util.create_piece_manip_ev(manipulation))

		if manipulation == g_const.PIECE_MANIP_FALL_DOWN_ID:
			self.stop_world_update()
			self.start_world_update()
			return # if manipulation is not repeated with button hold, don't change current_manip state

		elif manipulation == g_const.PIECE_MANIP_LEFT_ID or manipulation == g_const.PIECE_MANIP_RIGHT_ID:
			if g_const.continue_strafe_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)
			else: return

		elif manipulation == g_const.PIECE_MANIP_CLOCK_ID:
			if g_const.continue_rot_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)
			else: return

		else: # down
			if g_const.continue_down_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)
			else: return

		# ev_con_one.manipulating_piece = True # whether a piece is being manipulated
		self.current_manip = manipulation

	# for stopping manip ticks
	def stop_manip_update(self):
		pyg.time.set_timer(g_const.PIECE_MANIP_LEFT_ID, 0)
		pyg.time.set_timer(g_const.PIECE_MANIP_RIGHT_ID, 0)
		pyg.time.set_timer(g_const.PIECE_MANIP_CLOCK_ID, 0)
		pyg.time.set_timer(g_const.PIECE_MANIP_DOWN_ID, 0)

		# ev_con_one.manipulating_piece = False
		self.current_manip = None

	def processEvents(self):
		events = pyg.event.get() # store, then clear event queue

		for event in events:

			if event.type == pyg.QUIT:
				sys.exit()

			if event.type >= pyg.USEREVENT: # repost only custom events to event queue
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
					self.stop_world_update() # shape will fall down faster, world ticks will be stopped momentarily
					self.start_manip_update(g_const.PIECE_MANIP_DOWN_ID)

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
					self.start_world_update()
					self.stop_manip_update()

		events = pyg.event.get()
		return events
