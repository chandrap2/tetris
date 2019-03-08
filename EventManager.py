import pygame as pyg
import game_constants as g_const

class EventManager:

	# static method
    def start_world_update():
        pyg.time.set_timer(g_const.WORLD_UPDATE_ID, g_const.dt_world_update)
