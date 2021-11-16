class BlockGridSpaceSpecification:
	def __init__(self, start_x, start_y, block_width, block_height, height_modifier):
		self.start_x = start_x
		self.start_y = start_y
		self.block_width = block_width
		self.block_height = block_height
		self.height_modifier = height_modifier


class BlockSpaceInstance:
	def __init__(self, base_points, top_points):
		self.base_points = base_points
		self.top_points = top_points


def calculate_block_points(block_pos, block, bgss):
	centre = calculate_block_centre(block_pos, bgss)
	base_points = [(centre[0] - bgss.block_width / 2, centre[1]), (centre[0], centre[1] - bgss.block_height / 2),
	(centre[0] + bgss.block_width / 2, centre[1]), (centre[0], centre[1] + bgss.block_height / 2)]

	top_points = [(base_points[i][0], base_points[i][1] - block.vertex_heights[i] * bgss.height_modifier) for i in range(4)]

	return BlockSpaceInstance(base_points, top_points)


def calculate_block_centre(block_pos, bgss):
	half_block_width = bgss.block_width / 2
	half_block_height = bgss.block_height / 2

	return (bgss.start_x + half_block_width * (block_pos[1] - block_pos[0]), bgss.start_y + half_block_height * (block_pos[0] + block_pos[1]))