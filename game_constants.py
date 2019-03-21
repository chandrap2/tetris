import pygame as pyg
import util

pyg.init()

""" square constants """
square_size = 40

""" shape constants """
SHAPE_ORIENT_1 = 0
SHAPE_ORIENT_2 = 1
SHAPE_ORIENT_3 = 2
SHAPE_ORIENT_4 = 3

""" general game constants """
fps = 120 # desired framerate
frame_length = 1.0 / fps # in seconds

screen_w_blocks, screen_h_blocks = 10, 20
screen_size = (screen_w_blocks * square_size, screen_h_blocks * square_size)

screen = pyg.display.set_mode(screen_size)
screen_dim = screen.get_rect()

face_surface = pyg.image.load("face.png").convert()

dt_world_update = 750 # in ms
dt_manip_update = 62 # in ms

""" events """
WORLD_UPDATE_ID = pyg.USEREVENT
WORLD_UPDATE_EV = pyg.event.Event(WORLD_UPDATE_ID)

PIECE_MANIP_LEFT_ID = pyg.USEREVENT + 1
PIECE_MANIP_RIGHT_ID = pyg.USEREVENT + 2
continue_strafe_while_key_held = False

PIECE_MANIP_CLOCK_ID = pyg.USEREVENT + 3
continue_rot_while_key_held = False

PIECE_MANIP_DOWN_ID = pyg.USEREVENT + 4
continue_down_while_key_held = True

PIECE_HIT_BOTTOM_ID = pyg.USEREVENT + 5

SQUARE_COOR_ID = pyg.USEREVENT + 6
