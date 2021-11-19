import pygame
import unittest
from block_grid.src import block_grid_editor_drawer
from unittest import mock

class TestBlockGridEditorDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.bgss = mock.Mock()
		self.block_grid = mock.Mock()
		self.block_grid_editor = mock.Mock()
		self.block_grid_editor_drawer = block_grid_editor_drawer.BlockGridEditorDrawer(self.bgss)

		self.base_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
		self.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.points = mock.Mock()
		self.points.top_points = self.top_points
		self.points.base_points = self.base_points

	@mock.patch('pygame.draw.circle')
	@mock.patch('pygame.draw.lines')
	@mock.patch('pygame.draw.polygon')
	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
	def testDrawMultipleBlocks(self, mock_calculate_points, mock_draw_polygon, mock_draw_lines, mock_draw_circle):
		# GIVEN
		self.block_grid_editor.selected_blocks = [(0, 0), (0, 1)]
		self.block_grid_editor.selected_points = []
		mock_calculate_points.return_value = self.points

		# WHEN
		self.block_grid_editor_drawer.draw(self.block_grid, self.block_grid_editor, self.d_surf)

		# THEN
		expected_calculate_points_calls = [
		mock.call((0, 0), self.block_grid.blocks.get((0, 0)), self.bgss),
		mock.call((0, 1), self.block_grid.blocks.get((0, 1)), self.bgss)
		]

		expected_polygon_calls = [
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_COLOUR, self.top_points),
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_COLOUR, self.top_points)
		]

		expected_lines_calls = [
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_LINE_COLOUR, True, self.top_points),
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_LINE_COLOUR, True, self.top_points)
		]

		self.assertEqual(expected_calculate_points_calls, mock_calculate_points.call_args_list)
		self.assertEqual(expected_polygon_calls, mock_draw_polygon.call_args_list)
		self.assertEqual(expected_lines_calls, mock_draw_lines.call_args_list)

		mock_draw_circle.assert_not_called()

	@mock.patch('pygame.draw.circle')
	@mock.patch('pygame.draw.lines')
	@mock.patch('pygame.draw.polygon')
	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
	def testDrawSingleBlock(self, mock_calculate_points, mock_draw_polygon, mock_draw_lines, mock_draw_circle):
		# GIVEN
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = []
		mock_calculate_points.return_value = self.points

		# WHEN
		self.block_grid_editor_drawer.draw(self.block_grid, self.block_grid_editor, self.d_surf)

		# THEN
		mock_calculate_points.assert_called_with((0, 0), self.block_grid.blocks.get((0, 0)), self.bgss)
		mock_draw_polygon.assert_called_with(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_COLOUR, self.top_points)

		fill_col = block_grid_editor_drawer.DEFAULT_POINT_COLOUR
		line_col = block_grid_editor_drawer.DEFAULT_POINT_LINE_COLOUR
		rad = block_grid_editor_drawer.DEFAULT_POINT_RADIUS

		expected_draw_circle_calls = [
		mock.call(self.d_surf, fill_col, (int(self.top_points[0][0]), int(self.top_points[0][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[0][0]), int(self.top_points[0][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[1][0]), int(self.top_points[1][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[1][0]), int(self.top_points[1][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[2][0]), int(self.top_points[2][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[2][0]), int(self.top_points[2][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[3][0]), int(self.top_points[3][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[3][0]), int(self.top_points[3][1])), rad, width=1)
		]

		self.assertEqual(expected_draw_circle_calls, mock_draw_circle.call_args_list)

	@mock.patch('pygame.draw.circle')
	@mock.patch('pygame.draw.lines')
	@mock.patch('pygame.draw.polygon')
	@mock.patch('block_grid.src.block_grid_space_manager.calculate_block_points')
	def testDrawSingleBlockWithSelectedPoint(self, mock_calculate_points, mock_draw_polygon, mock_draw_lines, mock_draw_circle):
		# GIVEN
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = [0]
		mock_calculate_points.return_value = self.points

		# WHEN
		self.block_grid_editor_drawer.draw(self.block_grid, self.block_grid_editor, self.d_surf)

		# THEN
		fill_col = block_grid_editor_drawer.DEFAULT_POINT_COLOUR
		line_col = block_grid_editor_drawer.DEFAULT_POINT_LINE_COLOUR
		rad = block_grid_editor_drawer.DEFAULT_POINT_RADIUS

		expected_draw_circle_calls = [
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_POINT_COLOUR, (int(self.top_points[0][0]), int(self.top_points[0][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[0][0]), int(self.top_points[0][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[1][0]), int(self.top_points[1][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[1][0]), int(self.top_points[1][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[2][0]), int(self.top_points[2][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[2][0]), int(self.top_points[2][1])), rad, width=1),
		mock.call(self.d_surf, fill_col, (int(self.top_points[3][0]), int(self.top_points[3][1])), rad),
		mock.call(self.d_surf, line_col, (int(self.top_points[3][0]), int(self.top_points[3][1])), rad, width=1)
		]

		self.assertEqual(expected_draw_circle_calls, mock_draw_circle.call_args_list)

