import pygame
from block_grid.src.block_grid_drawer import DEFAULT_LINE_COLOUR
from block_grid.src import block_grid_space_manager

DEFAULT_HOVER_COL = (180, 180, 180)

class BlockGridHovererDrawer:
	def __init__(self, bgss):
		self.bgss = bgss

	def draw(self, grid, hoverer, d_surf):
		k = hoverer.hovered
		if k:
			points = block_grid_space_manager.calculate_block_points(k, grid.blocks[k], self.bgss)
			pygame.draw.polygon(d_surf, DEFAULT_HOVER_COL, points.top_points)
			pygame.draw.lines(d_surf, DEFAULT_LINE_COLOUR, True, points.top_points)
