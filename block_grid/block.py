class Block:
	LEFT = 0
	TOP = 1
	RIGHT = 2
	BOTTOM = 3

	def __init__(self, vertex_heights=[(0, 1), (0, 1), (0, 1), (0, 1)]):
		self.vertex_heights = vertex_heights

	def raise_(self, x):
		return Block(vertex_heights=[(height[0], height[1] + x) for height in self.vertex_heights])

	def lower(self, x):
		return Block(vertex_heights=[(height[0], max(height[1] - x, height[0])) for height in self.vertex_heights])

	def raise_point(self, i, x):
		vertex_heights = list.copy(self.vertex_heights)
		vertex_heights[i] = (vertex_heights[i][0], vertex_heights[i][1] + x)
		return Block(vertex_heights=vertex_heights)

	def lower_point(self, i, x):
		vertex_heights = list.copy(self.vertex_heights)
		vertex_heights[i] = (vertex_heights[i][0], max(vertex_heights[i][1] - x, vertex_heights[i][0]))
		return Block(vertex_heights=vertex_heights)

	def copy(self):
		return Block(vertex_heights=list.copy(self.vertex_heights))