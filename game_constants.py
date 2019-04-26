import pygame as pyg
import util

pyg.init()

""" square constants """
square_size = 40

""" UI constants """
UI_LEFT_MARGIN = 10
UI_TOP_MARGIN = 10
UI_RIGHT_MARGIN = square_size * 4 + 50 * 2
UI_BOTTOM_MARGIN = 10

""" general game constants """
fps = 120 # desired framerate
frame_length = 1.0 / fps # in seconds

screen_w_blocks, screen_h_blocks = 10, 20
arena_size = (screen_w_blocks * square_size, screen_h_blocks * square_size)
screen_size = (UI_LEFT_MARGIN + screen_w_blocks * square_size + UI_RIGHT_MARGIN, \
UI_TOP_MARGIN + screen_h_blocks * square_size + UI_BOTTOM_MARGIN)

screen = pyg.display.set_mode(screen_size)

face_surface = pyg.image.load("face.png").convert()

dt_world_update = 750 # in ms
dt_manip_update = 62 # in ms

""" shape constants """
SHAPE_ORIENT_1 = 0
SHAPE_ORIENT_2 = 1
SHAPE_ORIENT_3 = 2
SHAPE_ORIENT_4 = 3

""" key bindings """
KEY_STRAFE_L = pyg.K_LEFT
KEY_STRAFE_R = pyg.K_RIGHT
KEY_ROT_CLOCK = pyg.K_UP
KEY_DOWN = pyg.K_DOWN
KEY_FALL = pyg.K_SPACE

""" events """
WORLD_UPDATE_ID = pyg.USEREVENT
WORLD_UPDATE_EV = pyg.event.Event(WORLD_UPDATE_ID)

PIECE_MANIP_LEFT_ID = pyg.USEREVENT + 1
PIECE_MANIP_RIGHT_ID = pyg.USEREVENT + 2
continue_strafe_while_key_held = False # whether shape can be strafed continuously as long as keys are help down

PIECE_MANIP_CLOCK_ID = pyg.USEREVENT + 3
continue_rot_while_key_held = False # whether shape can be rotated continuously as long as keys are help down

PIECE_MANIP_DOWN_ID = pyg.USEREVENT + 4
continue_down_while_key_held = True  # whether shape can be strafed continuously as long as keys are help down

PIECE_MANIP_FALL_DOWN_ID = pyg.USEREVENT + 5

PIECE_HIT_BOTTOM_ID = pyg.USEREVENT + 6

SQUARE_COOR_ID = pyg.USEREVENT + 7 # event to store square coords when it's corresponding shape falls
