import math, pygame as pyg
import game_constants as g_const

def clamp(lower, upper, input):
	return min(upper, max(lower, input))

def create_piece_manip_ev(manipulation):
	return pyg.event.Event(manipulation)
