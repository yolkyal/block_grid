class BlockGridSpaceSpecification:
	def __init__(self, start_x, start_y, block_width, block_height):
		self.start_x = start_x
		self.start_y = start_y
		self.block_width = block_width
		self.block_height = block_height


class BlockSpaceInstance:
	def __init__(self, base_points, top_points):
		self.base_points = base_points
		self.top_points = top_points


def calculate_points(pos, block, bgss):
	centre = calculate_centre(pos, bgss)
	base_points = [(centre[0] - bgss.block_width / 2, centre[1]), (centre[0], centre[1] - bgss.block_height / 2),
	(centre[0] + bgss.block_width / 2, centre[1]), (centre[0], centre[1] + bgss.block_height / 2)]

	top_points = [(base_points[i][0], base_points[i][1] - block.vertex_heights[i]) for i in range(4)]

	return BlockSpaceInstance(base_points, top_points)


def calculate_centre(pos, bgss):
	half_block_width = bgss.block_width / 2
	half_block_height = bgss.block_height / 2

	return (bgss.start_x + half_block_width * (pos[1] - pos[0]), bgss.start_y + half_block_height * (pos[0] + pos[1]))