import pygame
import collision_utils
import block_grid_space_manager

DEFAULT_RAISE_INC = 1

class BlockGridEditor:
	def __init__(self, bgss, block_selector):
		self.block_selector = block_selector
		self.bgss = bgss
		self.selected_blocks = set()
		self.selected_points = set()
		self.dragging = False

	def handle_event(self, grid, event):
		if event.type == pygame.MOUSEMOTION:
			self._handle_mouse_motion(grid, event)
		elif event.type == pygame.MOUSEBUTTONUP:
			self._handle_mouse_button_up(grid, event)
		elif event.type == pygame.KEYDOWN:
			grid = self._handle_key_down(grid, event)
		return grid

	def _handle_mouse_motion(self, grid, event):
		if 1 in event.buttons:
			self._select_block(grid, event.pos, False)
			self.dragging = True

	def _handle_mouse_button_up(self, grid, event):
		if not self.dragging:
			if len(self.selected_blocks) == 1:
				point_i = self.get_selected_point(grid, event.pos)
				if point_i is not None:
					self.selected_points = {point_i}
				else:
					self._select_block(grid, event.pos)
			else:
				self._select_block(grid, event.pos)
		self.dragging = False

	def _select_block(self, grid, pos, deselect=True):
		self.selected_points = set()
		k = self.block_selector.select(grid, pos)
		if k:
			if pygame.key.get_pressed()[pygame.K_LSHIFT] or self.dragging:
				self.selected_blocks.add(k)
			else:
				self.selected_blocks = {k}
		elif deselect:
			self.selected_blocks = set()

	def _handle_key_down(self, grid, event):
		if self.selected_points:
			if event.key == pygame.K_UP:
				return grid.raise_point(next(iter(self.selected_blocks)), next(iter(self.selected_points)), DEFAULT_RAISE_INC)
			elif event.key == pygame.K_DOWN:
				return grid.lower_point(next(iter(self.selected_blocks)), next(iter(self.selected_points)), DEFAULT_RAISE_INC)
		elif self.selected_blocks:
			if event.key == pygame.K_UP:
				for k in self.selected_blocks:
					grid = grid.raise_(k, DEFAULT_RAISE_INC)
			elif event.key == pygame.K_DOWN:
				for k in self.selected_blocks:
					grid = grid.lower(k, DEFAULT_RAISE_INC)
			elif event.key == pygame.K_d:
				for k in self.selected_blocks:
					grid = grid.remove(k)
				self.selected_blocks = []
		return grid


	def get_selected_point(self, grid, pos):
		for k in self.selected_blocks:
			points = block_grid_space_manager.calculate_points(k, grid.blocks.get(k), self.bgss)
			for i, top_point in enumerate(points.top_points):
				if collision_utils.is_circle_point_collision(top_point, 5, pos):
					return i