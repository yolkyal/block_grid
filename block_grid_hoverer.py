class BlockGridHoverer:
	def __init__(self, block_grid_selector):
		self.block_grid_selector = block_grid_selector
		self.hovered = None

	def update(self, grid, pos):
		self.hovered = self.block_grid_selector.select(grid, pos)
