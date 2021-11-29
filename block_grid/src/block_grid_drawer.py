import pygame
from block_grid.src.block import LEFT, TOP, RIGHT, BOTTOM
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

			front_points = [points.top_points[i] for i in [LEFT, BOTTOM, RIGHT]] + [points.base_points[i] for i in [RIGHT, BOTTOM, LEFT]]

			pygame.draw.polygon(d_surf, colour_map.get(k, DEFAULT_TOP_COLOUR), points.top_points)
			pygame.draw.polygon(d_surf, DEFAULT_SIDE_COLOUR, front_points)

	def draw_fill_mesh_front(self, grid, d_surf, colour_map={}):
		for k in grid.blocks:
			points = block_grid_space_manager.calculate_block_points(k, grid.blocks[k], self.bgss)

			front_points = [points.top_points[i] for i in [LEFT, BOTTOM, RIGHT]] + [points.base_points[i] for i in [RIGHT, BOTTOM, LEFT]]

			pygame.draw.polygon(d_surf, colour_map.get(k, DEFAULT_TOP_COLOUR), points.top_points)
			pygame.draw.lines(d_surf, DEFAULT_LINE_COLOUR, True, points.top_points)

			pygame.draw.polygon(d_surf, DEFAULT_SIDE_COLOUR, front_points)
			pygame.draw.lines(d_surf, DEFAULT_LINE_COLOUR, True, front_points)
			pygame.draw.line(d_surf, DEFAULT_LINE_COLOUR, points.top_points[BOTTOM], points.base_points[BOTTOM])