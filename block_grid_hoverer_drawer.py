import pygame
import block_grid_space_manager

DEFAULT_HOVER_COL = (160, 160, 160)

class BlockGridHovererDrawer:
	def __init__(self, bgss):
		self.bgss = bgss

	def draw(self, grid, hoverer, d_surf):
		k = hoverer.hovered
		if k:
			points = block_grid_space_manager.calculate_points(k, grid.blocks[k], self.bgss)
			pygame.draw.polygon(d_surf, DEFAULT_HOVER_COL, points.top_points)
