import unittest
from block_grid import block_grid_space_manager
from unittest import mock

class TestBlockGridSpaceManager(unittest.TestCase):
	def setUp(self):
		self.start_height = 1

		self.start_x = 100
		self.start_y = 10
		self.block_width = 64
		self.block_height = 32
		self.height_modifier = 5
		self.grid_space_specification = block_grid_space_manager.BlockGridSpaceSpecification(self.start_x, self.start_y, self.block_width, self.block_height, self.height_modifier)

	def testCalculateBlockPoints(self):
		block = mock.Mock()
		block.vertex_heights = [(0, self.start_height), (0, self.start_height), (0, self.start_height), (0, self.start_height)]

		left_point_bottom = (float(self.start_x - (self.block_width / 2)), float(self.start_y))
		top_point_bottom = (float(self.start_x), float(self.start_y - self.block_height / 2))
		right_point_bottom = (float(self.start_x + (self.block_width / 2)), float(self.start_y))
		bottom_point_bottom = (float(self.start_x), float(self.start_y + self.block_height / 2))

		left_point_top = (left_point_bottom[0], left_point_bottom[1] - self.start_height * self.height_modifier)
		top_point_top = (top_point_bottom[0], top_point_bottom[1] - self.start_height * self.height_modifier)
		right_point_top = (right_point_bottom[0], right_point_bottom[1] - self.start_height * self.height_modifier)
		bottom_point_top = (bottom_point_bottom[0], bottom_point_bottom[1] - self.start_height * self.height_modifier)

		result = block_grid_space_manager.calculate_block_points((0, 0), block, self.grid_space_specification)

		self.assertEqual([left_point_bottom, top_point_bottom, right_point_bottom, bottom_point_bottom], result.base_points)
		self.assertEqual([left_point_top, top_point_top, right_point_top, bottom_point_top], result.top_points)

