import pygame as pyg, sys
import game_constants as g_const, util

class EvtManContainer:
	def __init__(self):
		self.manipulating_piece = False
		self.current_manip = None

ev_con_one = EvtManContainer()

def start_world_update():
	pyg.time.set_timer(g_const.WORLD_UPDATE_ID, g_const.dt_world_update)

def stop_world_update():
	pyg.time.set_timer(g_const.WORLD_UPDATE_ID, 0)

def start_manip_update(manipulation):
	event = util.create_piece_manip_ev(manipulation)

	pyg.event.post(event)

	if manipulation == g_const.PIECE_MANIP_LEFT_ID or manipulation == g_const.PIECE_MANIP_RIGHT_ID:
		if g_const.continue_strafe_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	elif manipulation == g_const.PIECE_MANIP_CLOCK_ID:
		if g_const.continue_rot_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	else: # down
		if g_const.continue_down_while_key_held: pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	ev_con_one.current_manip = manipulation
	ev_con_one.manipulating_piece = True

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

		if event.type >= pyg.USEREVENT:
			# print(event)

			pyg.event.post(event)
			continue

		if not ev_con_one.manipulating_piece and event.type == pyg.KEYDOWN:
			if event.key == pyg.K_LEFT:
				start_manip_update(g_const.PIECE_MANIP_LEFT_ID)
			elif event.key == pyg.K_RIGHT:
				start_manip_update(g_const.PIECE_MANIP_RIGHT_ID)
			elif event.key == pyg.K_e:
				start_manip_update(g_const.PIECE_MANIP_CLOCK_ID)
			elif event.key == pyg.K_DOWN:
				stop_world_update()
				start_manip_update(g_const.PIECE_MANIP_DOWN_ID)

		if event.type == pyg.KEYUP and ev_con_one.current_manip != None:
			if event.key == pyg.K_LEFT and ev_con_one.current_manip == g_const.PIECE_MANIP_LEFT_ID:
				stop_manip_update()
			elif event.key == pyg.K_RIGHT and ev_con_one.current_manip == g_const.PIECE_MANIP_RIGHT_ID:
				stop_manip_update()
			elif event.key == pyg.K_e and ev_con_one.current_manip == g_const.PIECE_MANIP_CLOCK_ID:
				stop_manip_update()
			elif event.key == pyg.K_DOWN and ev_con_one.current_manip == g_const.PIECE_MANIP_DOWN_ID:
				start_world_update()
				stop_manip_update()

	return pyg.event.get()
