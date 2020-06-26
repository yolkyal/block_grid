import unittest
import block_drawer
from unittest import mock


class TestBlockDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.bgss = mock.Mock()
		self.block = mock.Mock()
		self.block_drawer = block_drawer.BlockDrawer(self.bgss)

		self.k = (0, 0)
		self.base_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
		self.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.points = mock.Mock()
		self.points.top_points = self.top_points
		self.points.base_points = self.base_points

	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('pygame.draw.polygon')
	def testDrawFill(self, mock_draw_polygon, mock_calculate_points):
		mock_calculate_points.return_value = self.points
		
		self.block_drawer.draw_fill(self.k, self.block, self.d_surf)

		expected_polygon_calls = [
		mock.call(self.d_surf, block_drawer.DEFAULT_TOP_COLOUR, self.top_points),
		mock.call(self.d_surf, block_drawer.DEFAULT_SIDE_COLOUR, 
			[self.top_points[0], self.top_points[3], self.top_points[2], self.base_points[2], self.base_points[3], self.base_points[0]])
		]

		self.assertEqual(expected_polygon_calls, mock_draw_polygon.call_args_list)

	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('pygame.draw.line')
	@mock.patch('pygame.draw.lines')
	def testDrawMesh(self, mock_draw_lines, mock_draw_line, mock_calculate_points):
		mock_calculate_points.return_value = self.points
		
		self.block_drawer.draw_mesh(self.k, self.block, self.d_surf)

		expected_lines_calls = [
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, True, self.top_points),
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, True, self.base_points)
		]

		expected_line_calls = [
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, self.top_points[0], self.base_points[0]),
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, self.top_points[1], self.base_points[1]),
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, self.top_points[2], self.base_points[2]),
		mock.call(self.d_surf, block_drawer.DEFAULT_LINE_COLOUR, self.top_points[3], self.base_points[3])
		]

		self.assertEqual(expected_lines_calls, mock_draw_lines.call_args_list)
		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)


if __name__ == '__main__':
	unittest.main()