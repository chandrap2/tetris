import pygame as pyg, sys
import game_constants as g_const, util

# container so variable values can persist
class EvtManContainer:
	def __init__(self):
		self.manipulating_piece = False
		self.current_manip = None #

ev_con_one = EvtManContainer()

# for starting world update ticks
def start_world_update():
	pyg.time.set_timer(g_const.WORLD_UPDATE_ID, g_const.dt_world_update)

# for stopping world update ticks
def stop_world_update():
	pyg.time.set_timer(g_const.WORLD_UPDATE_ID, 0)

# for starting manipulation update ticks
def start_manip_update(manipulation):
	event = util.create_piece_manip_ev(manipulation)

	pyg.event.post(event)

	if manipulation == g_const.PIECE_MANIP_FALL_DOWN_ID:
		stop_world_update()
		start_world_update()

	elif manipulation == g_const.PIECE_MANIP_LEFT_ID or manipulation == g_const.PIECE_MANIP_RIGHT_ID:
		if g_const.continue_strafe_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	elif manipulation == g_const.PIECE_MANIP_CLOCK_ID:
		if g_const.continue_rot_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	else: # down
		if g_const.continue_down_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	ev_con_one.manipulating_piece = True # whether a piece is being manipulated
	ev_con_one.current_manip = manipulation

# for stopping manip ticks
def stop_manip_update():
	pyg.time.set_timer(g_const.PIECE_MANIP_LEFT_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_RIGHT_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_CLOCK_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_DOWN_ID, 0)

	ev_con_one.manipulating_piece = False
	ev_con_one.current_manip = None

def processEvents():
	events = pyg.event.get() # store, then clear event queue

	for event in events:

		if event.type == pyg.QUIT:
			sys.exit()

		if event.type >= pyg.USEREVENT: # repost only custom events to event queue
			# print(event)

			pyg.event.post(event)
			continue

		if not ev_con_one.manipulating_piece and event.type == pyg.KEYDOWN:
			if event.key == g_const.KEY_STRAFE_L:
				start_manip_update(g_const.PIECE_MANIP_LEFT_ID)
			elif event.key == g_const.KEY_STRAFE_R:
				start_manip_update(g_const.PIECE_MANIP_RIGHT_ID)
			elif event.key == g_const.KEY_ROT_CLOCK:
				start_manip_update(g_const.PIECE_MANIP_CLOCK_ID)
			elif event.key == g_const.KEY_FALL:
				start_manip_update(g_const.PIECE_MANIP_FALL_DOWN_ID)
			elif event.key == g_const.KEY_DOWN: # shape will fall down faster, world ticks ill be stopped momentarily
				stop_world_update()
				start_manip_update(g_const.PIECE_MANIP_DOWN_ID)

		if event.type == pyg.KEYUP and ev_con_one.current_manip != None:
			if event.key == g_const.KEY_STRAFE_L and ev_con_one.current_manip == g_const.PIECE_MANIP_LEFT_ID:
				stop_manip_update()
			elif event.key == g_const.KEY_STRAFE_R and ev_con_one.current_manip == g_const.PIECE_MANIP_RIGHT_ID:
				stop_manip_update()
			elif event.key == g_const.KEY_ROT_CLOCK and ev_con_one.current_manip == g_const.PIECE_MANIP_CLOCK_ID:
				stop_manip_update()
			elif event.key == g_const.KEY_FALL and ev_con_one.current_manip == g_const.PIECE_MANIP_FALL_DOWN_ID:
				stop_manip_update()
			elif event.key == g_const.KEY_DOWN and ev_con_one.current_manip == g_const.PIECE_MANIP_DOWN_ID: # world ticks will resume
				start_world_update()
				stop_manip_update()

	return pyg.event.get()
