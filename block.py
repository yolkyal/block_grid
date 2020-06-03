class Block:
	LEFT = 0
	TOP = 1
	RIGHT = 2
	BOTTOM = 3

	def __init__(self, height=0, vertex_heights=None):
		if vertex_heights:
			self.vertex_heights = vertex_heights
		else:
			self.vertex_heights=[height, height, height, height]

	def raise_(self, x):
		return Block(vertex_heights=[(height + x) for height in self.vertex_heights])

	def lower(self, x):
		return Block(vertex_heights=[(height - x) for height in self.vertex_heights])

	def raise_point(self, i, x):
		vertex_heights = list.copy(self.vertex_heights)
		vertex_heights[i] += x
		return Block(vertex_heights=vertex_heights)

	def lower_point(self, i, x):
		vertex_heights = list.copy(self.vertex_heights)
		vertex_heights[i] -= x
		return Block(vertex_heights=vertex_heights)

	def copy(self):
		return Block(vertex_heights=list.copy(self.vertex_heights))