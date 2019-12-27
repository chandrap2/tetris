import game_constants as g_const
from Square import Square

class Terrain:
	def __init__(self):
		self.game_map = [] # each element is a row

		for y in range(g_const.arena_h_blocks):
			self.game_map.append([None for x in range(g_const.arena_w_blocks)]) # None if space is unoccupied

	def update(self, events):
		# has_landed = False

		for event in events:
			if event.cus_event == g_const.PIECE_HIT_BOTTOM_ID:
				for square in event.params:
					# has_landed = True
					self.game_map[square.y_block][square.x_block] = square  # mark square in map
			elif event.cus_event == g_const.ROW_FULL_ID:
				self.collapse_rows(event.params)
				# self.print_map()
				# print("..............")

	def collapse_rows(self, rows_to_collapse):
		dummy_row = [None for x in range(g_const.arena_w_blocks)]
		for row in rows_to_collapse:
			self.game_map[row] = list(dummy_row)
			self.game_map[row][0] = Square((0, row), is_full_row_indicator = True) # indicating a cleared row

		temp = [list(dummy_row) for y in range(g_const.arena_h_blocks)] # new blank terrain map
		real_i = temp_i = g_const.arena_h_blocks - 1 # indices for scanning for cleared rows/populating new map

		while real_i >= 0: # only add row to temp if it's empty, starting at bottom, else check the row above, repeat
			if self.game_map[real_i][0] != None and self.game_map[real_i][0].is_full_row_indicator:
				real_i -= 1
				continue
			temp[temp_i] = self.game_map[real_i] # add uncleared row to new map
			for square in temp[temp_i]: # move all added squares to appropriate row
				if square != None: square.move_to_block(square.x_block, temp_i)
			temp_i -= 1
			real_i -= 1

		self.game_map = temp

	def check_for_collision_to_left(self, square):
		return (square.x_block == 0 or self.game_map[square.y_block][square.x_block - 1] != None)

	def check_for_collision_below(self, square):
		return (square.y_block == g_const.arena_h_blocks - 1 or self.game_map[square.y_block + 1][square.x_block] != None)

	def check_for_collision_to_right(self, square):
		return (square.x_block == g_const.arena_w_blocks - 1 or self.game_map[square.y_block][square.x_block + 1] != None)

	# return index of highest FREE block below a given row in any given column
	def highestBelow(self, square):
		for row in range(square.y_block + 1, g_const.arena_h_blocks):
			if self.game_map[row][square.x_block] != None: return row - 1
		return g_const.arena_h_blocks - 1

	def print_map(self):
		for row in range(g_const.arena_h_blocks):
			for col in range(g_const.arena_w_blocks):
				print("#" if self.game_map[row][col] != None else "*", end = "")
			print()
		print()

	def draw(self):
		for row in self.game_map:
			for square in row:
				if square != None: square.draw()
