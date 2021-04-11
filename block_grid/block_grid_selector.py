import block_grid_space_manager, collision_utils

class BlockGridSelector:
	def __init__(self, bgss):
		self.bgss = bgss

	def select(self, grid, pos):
		for item in reversed(list(grid.blocks.items())):
			points = block_grid_space_manager.calculate_points(item[0], item[1], self.bgss)

			if collision_utils.is_diamond_point_collision(points.top_points[0], points.top_points[1], points.top_points[2], points.top_points[3], pos):
				return item[0]