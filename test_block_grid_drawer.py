import unittest, pygame
from unittest import mock
import block, block_grid, block_grid_space_manager, block_grid_drawer

class TestBlockGridDrawer(unittest.TestCase):
	def setUp(self):
		self.block_grid = block_grid.BlockGrid(blocks={(0, 0): block.Block()})

		self.base_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
		self.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.points = block_grid_space_manager.BlockSpaceInstance(self.base_points, self.top_points)

		self.block_grid_drawer = block_grid_drawer.BlockGridDrawer('BGSS')
	
	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('pygame.draw.line')
	@mock.patch('pygame.draw.lines')
	def testDrawMesh(self, mock_draw_lines, mock_draw_line, mock_calculate_points):
		d_surf = 'D_SURF'
		mock_calculate_points.return_value = self.points
		
		self.block_grid_drawer.draw_mesh(self.block_grid, d_surf)

		expected_lines_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, True, self.top_points),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, True, self.base_points)
		]

		expected_line_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[0], self.base_points[0]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[1], self.base_points[1]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[2], self.base_points[2]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[3], self.base_points[3])
		]

		self.assertEqual(expected_lines_calls, mock_draw_lines.call_args_list)
		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)

	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('pygame.draw.polygon')
	def testDrawFill(self, mock_draw_polygon, mock_calculate_points):
		d_surf = 'D_SURF'
		mock_calculate_points.return_value = self.points
		
		self.block_grid_drawer.draw_fill(self.block_grid, d_surf)

		expected_polygon_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_TOP_COLOUR, self.top_points),
		mock.call(d_surf, block_grid_drawer.DEFAULT_SIDE_COLOUR, 
			[self.top_points[0], self.top_points[3], self.top_points[2], self.base_points[2], self.base_points[3], self.base_points[0]])
		]

		self.assertEqual(expected_polygon_calls, mock_draw_polygon.call_args_list)

if __name__ == '__main__':
	unittest.main()

