import unittest
import block_grid_space_manager, block

class TestBlockGridSpaceManager(unittest.TestCase):
	def setUp(self):
		self.start_height = 10

		self.start_x = 100
		self.start_y = 10
		self.block_width = 64
		self.block_height = 32
		self.grid_space_specification = block_grid_space_manager.BlockGridSpaceSpecification(self.start_x, self.start_y, self.block_width, self.block_height)

	def testFlatBlockCalculationPoints(self):
		left_point_top = (float(self.start_x - (self.block_width / 2)), float(self.start_y - self.start_height))
		top_point_top = (float(self.start_x), float(self.start_y - (self.block_height / 2) - self.start_height))
		right_point_top = (float(self.start_x + (self.block_width / 2)), float(self.start_y - self.start_height))
		bottom_point_top = (float(self.start_x), float(self.start_y + (self.block_height / 2) - self.start_height))

		left_point_bottom = (left_point_top[0], left_point_top[1] + self.start_height) 
		top_point_bottom = (top_point_top[0], top_point_top[1] + self.start_height)
		right_point_bottom = (right_point_top[0], right_point_top[1] + self.start_height)
		bottom_point_bottom = (bottom_point_top[0], bottom_point_top[1] + self.start_height)

		result = block_grid_space_manager.calculate_points((0, 0), block.Block(self.start_height), self.grid_space_specification)

		self.assertEqual([left_point_top, top_point_top, right_point_top, bottom_point_top], result.top_points)
		self.assertEqual([left_point_bottom, top_point_bottom, right_point_bottom, bottom_point_bottom], result.base_points)


if __name__ == '__main__':
	unittest.main()