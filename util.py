import math, pygame as pyg
from random import randint

import game_constants as g_const
from Shapes import *

def post_piece_manip_ev(manipulation):
	post_custom_event(manipulation)

def post_custom_event(cus_event, params = []):
	pyg.event.post(pyg.event.Event(pyg.USEREVENT, cus_event = cus_event, params = params))

def gen_shape(terrain):
	rand = randint(1, 7)

	if rand == 1: return Shape1(terrain)
	if rand == 2: return Shape2(terrain)
	if rand == 3: return Shape3(terrain)
	if rand == 4: return Shape4(terrain)
	if rand == 5: return Shape5(terrain)
	if rand == 6: return Shape6(terrain)
	if rand == 7: return Shape7(terrain)
