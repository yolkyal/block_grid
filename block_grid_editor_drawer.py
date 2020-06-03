import pygame
import block_grid_space_manager
DEFAULT_SELECTED_COLOUR = (200, 200, 200)
DEFAULT_POINT_COLOUR = (70, 70, 70)
SELECTED_POINT_COLOUR = (150, 255, 150)
DEFAULT_POINT_RADIUS = 5

class BlockGridEditorDrawer:
	def __init__(self, bgss):
		self.bgss = bgss

	def draw(self, grid, grid_editor, d_surf):
		for k in grid_editor.selected_blocks:
			points = block_grid_space_manager.calculate_points(k, grid.blocks[k], self.bgss)
			pygame.draw.polygon(d_surf, DEFAULT_SELECTED_COLOUR, points.top_points)
			
			for i in range(4):
				pygame.draw.circle(d_surf, SELECTED_POINT_COLOUR if i in grid_editor.selected_points else DEFAULT_POINT_COLOUR, 
					int_tuple(points.top_points[i]), DEFAULT_POINT_RADIUS)

def int_tuple(tup):
	return (int(tup[0]), int(tup[1]))
