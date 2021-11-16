import unittest, pygame
from block_grid.src import block, block_grid, block_grid_drawer
from unittest import mock

class TestBlockGridDrawer(unittest.TestCase):
	def setUp(self):
		self.block_grid = block_grid.BlockGrid(blocks={(0, 0): block.Block()})

		self.base_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
		self.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.points = mock.Mock(base_points=self.base_points, top_points=self.top_points)

		self.block_grid_drawer = block_grid_drawer.BlockGridDrawer('BGSS')
	
	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
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
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[block.LEFT], self.base_points[block.LEFT]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[block.TOP], self.base_points[block.TOP]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[block.RIGHT], self.base_points[block.RIGHT]),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[block.BOTTOM], self.base_points[block.BOTTOM])
		]

		self.assertEqual(expected_lines_calls, mock_draw_lines.call_args_list)
		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)

	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
	@mock.patch('pygame.draw.polygon')
	def testDrawFill(self, mock_draw_polygon, mock_calculate_points):
		d_surf = 'D_SURF'
		mock_calculate_points.return_value = self.points
		
		self.block_grid_drawer.draw_fill(self.block_grid, d_surf)

		expected_polygon_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_TOP_COLOUR, self.top_points),
		mock.call(d_surf, block_grid_drawer.DEFAULT_SIDE_COLOUR, 
			[self.top_points[block.LEFT], self.top_points[block.BOTTOM], self.top_points[block.RIGHT], self.base_points[block.RIGHT], self.base_points[block.BOTTOM], self.base_points[block.LEFT]])
		]

		self.assertEqual(expected_polygon_calls, mock_draw_polygon.call_args_list)

	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
	@mock.patch('pygame.draw.line')
	@mock.patch('pygame.draw.lines')
	@mock.patch('pygame.draw.polygon')
	def testDrawFillMeshFront(self, mock_draw_polygon, mock_draw_lines, mock_draw_line, mock_calculate_points):
		d_surf = 'D_SURF'
		mock_calculate_points.return_value = self.points
		
		self.block_grid_drawer.draw_fill_mesh_front(self.block_grid, d_surf)

		expected_polygon_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_TOP_COLOUR, self.top_points),
		mock.call(d_surf, block_grid_drawer.DEFAULT_SIDE_COLOUR, 
			[self.top_points[block.LEFT], self.top_points[block.BOTTOM], self.top_points[block.RIGHT], self.base_points[block.RIGHT], self.base_points[block.BOTTOM], self.base_points[block.LEFT]])
		]

		expected_lines_calls = [
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, True, self.top_points),
		mock.call(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, True, 
			[self.top_points[block.LEFT], self.top_points[block.BOTTOM], self.top_points[block.RIGHT], self.base_points[block.RIGHT], self.base_points[block.BOTTOM], self.base_points[block.LEFT]])
		]

		self.assertEqual(expected_lines_calls, mock_draw_lines.call_args_list)
		self.assertEqual(expected_polygon_calls, mock_draw_polygon.call_args_list)
		mock_draw_line.assert_called_once_with(d_surf, block_grid_drawer.DEFAULT_LINE_COLOUR, self.top_points[block.BOTTOM], self.base_points[block.BOTTOM])
