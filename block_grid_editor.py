import pygame
import collision_utils
import block_grid_space_manager

DEFAULT_RAISE_INC = 10

class BlockGridEditor:
	def __init__(self, bgss, block_selector):
		self.block_selector = block_selector
		self.bgss = bgss
		self.selected_blocks = []
		self.selected_points = []

	def handle_mouse_button_up(self, grid, e):
		for k in self.selected_blocks:
			points = block_grid_space_manager.calculate_points(k, grid.blocks[k], self.bgss)
			for i, top_point in enumerate(points.top_points):
				if collision_utils.is_circle_point_collision(top_point, 5, e.pos):
					self.selected_points = [i]
					return
		self.selected_points = []

		k = self.block_selector.select(grid, e.pos)
		self.selected_blocks = [k] if k else []

	def handle_key_down(self, grid, e):
		if self.selected_points:
			if e.key == pygame.K_UP:
				return grid.raise_point(self.selected_blocks[0], self.selected_points[0], DEFAULT_RAISE_INC)
			elif e.key == pygame.K_DOWN:
				return grid.lower_point(self.selected_blocks[0], self.selected_points[0], DEFAULT_RAISE_INC)

		if e.key == pygame.K_UP:
			for k in self.selected_blocks:
				grid = grid.raise_(k, DEFAULT_RAISE_INC)
		elif e.key == pygame.K_DOWN:
			for k in self.selected_blocks:
				grid = grid.lower(k, DEFAULT_RAISE_INC)
		elif e.key == pygame.K_d:
			for k in self.selected_blocks:
				grid = grid.remove(k)
				self.selected_blocks.remove(k)

		return grid