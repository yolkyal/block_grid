import unittest
import block, block_grid, block_grid_selector, block_grid_space_manager
from unittest import mock
from unittest.mock import Mock


class TestBlockGridSelector(unittest.TestCase):
	def setUp(self):
		self.start_height = 10
		self.block_grid = block_grid.BlockGrid(blocks={(0, 0): block.Block(self.start_height)})

		self.base_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
		self.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.points = block_grid_space_manager.BlockSpaceInstance(self.base_points, self.top_points)

		self.bgss = 'BGSS'
		self.grid_block_selector = block_grid_selector.BlockGridSelector(self.bgss)

	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('collision_utils.is_diamond_point_collision')
	def testSelect(self, mock_diamond_collision, mock_calculate_points):
		mock_calculate_points.return_value = self.points
		mock_diamond_collision.return_value = True

		pos = Mock()
		k = self.grid_block_selector.select(self.block_grid, pos)

		self.assertEqual((0, 0), k)
		mock_calculate_points.assert_called_with((0, 0), self.block_grid.blocks[(0, 0)], 'BGSS')
		mock_diamond_collision.assert_called_with(self.top_points[0], self.top_points[1], self.top_points[2], self.top_points[3], pos)


	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('collision_utils.is_diamond_point_collision')
	def testOrdering(self, mock_diamond_collision, mock_calculate_points):
		mock_calculate_points.return_value = self.points
		mock_diamond_collision.return_value = False

		grid = block_grid.BlockGrid(blocks={(0, 0): block.Block(self.start_height), (0, 1): block.Block(self.start_height), (1, 0): block.Block(self.start_height), (1, 1): block.Block(self.start_height)})

		pos = Mock()
		k = self.grid_block_selector.select(grid, pos)

		self.assertEqual(None, k)

		expected_calculate_points_calls = [
		mock.call((1, 1), grid.blocks[(1, 1)], 'BGSS'),
		mock.call((1, 0), grid.blocks[(1, 0)], 'BGSS'),
		mock.call((0, 1), grid.blocks[(0, 1)], 'BGSS'),
		mock.call((0, 0), grid.blocks[(0, 0)], 'BGSS')
		]

		self.assertEqual(expected_calculate_points_calls, mock_calculate_points.call_args_list)

