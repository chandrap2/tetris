import pygame as pyg
import util

pyg.init()

""" general game constants """
fps = 120 # desired framerate
frame_length = 1.0 / fps # in seconds

square_size = 20

screen_w_blocks, screen_h_blocks = 10, 20
screen_size = (screen_w_blocks * square_size, screen_h_blocks * square_size)

screen = pyg.display.set_mode(screen_size)
screen_dim = screen.get_rect()

face_surface = pyg.image.load("face.png").convert()

dt_world_update = 500 # in ms
dt_manip_update = 250 # in ms

# pong_noise = pyg.mixer.Sound("4388__noisecollector__pongblipe5.wav")

# events
# GAMEREADY_ID = pyg.USEREVENT
# GAMEREADY_EV = pyg.event.Event(GAMEREADY_ID, move_to_player_id = b_move_to_rand_p_id)
#
# GAMEWIN_ID = pyg.USEREVENT + 1
# GAMEWIN_EV = pyg.event.Event(GAMEWIN_ID, winning_player_id = p_p1_won_id)

WORLD_UPDATE_ID = pyg.USEREVENT
WORLD_UPDATE_EV = pyg.event.Event(WORLD_UPDATE_ID)

PIECE_MANIP_LEFT_ID = pyg.USEREVENT + 1
PIECE_MANIP_RIGHT_ID = pyg.USEREVENT + 2
continue_strafe_while_key_held = False

PIECE_MANIP_CLOCK_ID = pyg.USEREVENT + 3
continue_rot_while_key_held = False

PIECE_MANIP_DOWN_ID = pyg.USEREVENT + 4
continue_down_while_key_held = True
