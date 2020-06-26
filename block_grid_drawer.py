class BlockGridDrawer:
	def __init__(self, block_drawer):
		self.block_drawer = block_drawer

	def draw_mesh(self, grid, d_surf):
		for item in grid.blocks.items():
			self.block_drawer.draw_mesh(item[0], item[1], d_surf)

	def draw_fill(self, grid, d_surf, colour_map={}):
		for item in grid.blocks.items():
			self.block_drawer.draw_fill(item[0], item[1], d_surf)