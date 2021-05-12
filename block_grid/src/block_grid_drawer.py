import pygame
from block_grid.src import block_grid_space_manager
DEFAULT_TOP_COLOUR = (150, 150, 150)
DEFAULT_SIDE_COLOUR = (100, 100, 100)
DEFAULT_LINE_COLOUR = (50, 50, 50)

class BlockGridDrawer:
	def __init__(self, bgss):
		self.bgss = bgss

	def draw_mesh(self, grid, d_surf):
		for k in grid.blocks:
			points = block_grid_space_manager.calculate_block_points(k, grid.blocks[k], self.bgss)

			pygame.draw.lines(d_surf, DEFAULT_LINE_COLOUR, True, points.top_points)
			pygame.draw.lines(d_surf, DEFAULT_LINE_COLOUR, True, points.base_points)

			for i in range(4):
				pygame.draw.line(d_surf, DEFAULT_LINE_COLOUR, points.top_points[i], points.base_points[i])

	def draw_fill(self, grid, d_surf, colour_map={}):
		for k in grid.blocks:
			points = block_grid_space_manager.calculate_block_points(k, grid.blocks[k], self.bgss)

			side_points = [points.top_points[0], points.top_points[3], points.top_points[2], 
			points.base_points[2], points.base_points[3], points.base_points[0]]

			pygame.draw.polygon(d_surf, colour_map.get(k, DEFAULT_TOP_COLOUR), points.top_points)
			pygame.draw.polygon(d_surf, DEFAULT_SIDE_COLOUR, side_points)