import pygame as pyg
import game_constants as g_const, util

class EvtManContainer:
	def __init__(self):
		self.maniputing_piece = False
		self.current_manip = 0

ev_con_one = EvtManContainer()

def start_world_update():
	pyg.time.set_timer(g_const.WORLD_UPDATE_ID, g_const.dt_world_update)

def start_manip_update(manipulation):
	event = util.create_piece_manip_ev(manipulation)

	pyg.event.post(event)
	pyg.time.set_timer(manipulation, g_const.dt_manip_update)

	ev_con_one.current_manip = manipulation
	ev_con_one.maniputing_piece = True

	print("starting manip, current_manip =", ev_con_one.current_manip)

def stop_manip_update():
	pyg.time.set_timer(g_const.PIECE_MANIP_LEFT_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_RIGHT_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_CLOCK_ID, 0)
	pyg.time.set_timer(g_const.PIECE_MANIP_COUNTERCLOCK_ID, 0)

	ev_con_one.maniputing_piece = False

	print("ending manip")

def process(events):
	for event in events:
		if event.type == pyg.QUIT:
			sys.exit()

		if event.type == g_const.WORLD_UPDATE_ID or (event.type >= g_const.PIECE_MANIP_LEFT_ID and event.type <= g_const.PIECE_MANIP_COUNTERCLOCK_ID):
			pyg.event.post(event)
			continue

		if not ev_con_one.maniputing_piece and event.type == pyg.KEYDOWN:
			if event.key == pyg.K_LEFT:
				start_manip_update(g_const.PIECE_MANIP_LEFT_ID)
			elif event.key == pyg.K_RIGHT:
				start_manip_update(g_const.PIECE_MANIP_RIGHT_ID)

		if event.type == pyg.KEYUP and (event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT):
			# print("key lifted, current_manip=", current_manip)
			if event.key == pyg.K_LEFT and ev_con_one.current_manip == g_const.PIECE_MANIP_LEFT_ID:
				stop_manip_update()
			elif event.key == pyg.K_RIGHT and ev_con_one.current_manip == g_const.PIECE_MANIP_RIGHT_ID:
				stop_manip_update()
