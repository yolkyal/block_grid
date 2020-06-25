import pygame
import unittest
import block_grid_editor_drawer
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
	@mock.patch('pygame.draw.polygon')
	@mock.patch('block_grid_space_manager.calculate_points')
	def testDraw(self, mock_calculate_points, mock_draw_polygon, mock_draw_circle):
		# GIVEN
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = []
		mock_calculate_points.return_value = self.points

		# WHEN
		self.block_grid_editor_drawer.draw(self.block_grid, self.block_grid_editor, self.d_surf)

		# THEN
		mock_calculate_points.assert_called_with((0, 0), self.block_grid.blocks.get((0, 0)), self.bgss)
		mock_draw_polygon.assert_called_with(self.d_surf, block_grid_editor_drawer.DEFAULT_SELECTED_COLOUR, self.top_points)

		col = block_grid_editor_drawer.DEFAULT_POINT_COLOUR
		rad = block_grid_editor_drawer.DEFAULT_POINT_RADIUS

		expected_draw_circle_calls = [
		mock.call(self.d_surf, col, (int(self.top_points[0][0]), int(self.top_points[0][1])), rad),
		mock.call(self.d_surf, col, (int(self.top_points[1][0]), int(self.top_points[1][1])), rad),
		mock.call(self.d_surf, col, (int(self.top_points[2][0]), int(self.top_points[2][1])), rad),
		mock.call(self.d_surf, col, (int(self.top_points[3][0]), int(self.top_points[3][1])), rad)
		]

		self.assertEqual(expected_draw_circle_calls, mock_draw_circle.call_args_list)

	@mock.patch('pygame.draw.circle')
	@mock.patch('pygame.draw.polygon')
	@mock.patch('block_grid_space_manager.calculate_points')
	def testDrawSelectedPoint(self, mock_calculate_points, mock_draw_polygon, mock_draw_circle):
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = [0]
		mock_calculate_points.return_value = self.points

		self.block_grid_editor_drawer.draw(self.block_grid, self.block_grid_editor, self.d_surf)

		expected_draw_circle_calls = [
		mock.call(self.d_surf, block_grid_editor_drawer.SELECTED_POINT_COLOUR, self.top_points[0], block_grid_editor_drawer.DEFAULT_POINT_RADIUS),
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_POINT_COLOUR, self.top_points[1], block_grid_editor_drawer.DEFAULT_POINT_RADIUS),
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_POINT_COLOUR, self.top_points[2], block_grid_editor_drawer.DEFAULT_POINT_RADIUS),
		mock.call(self.d_surf, block_grid_editor_drawer.DEFAULT_POINT_COLOUR, self.top_points[3], block_grid_editor_drawer.DEFAULT_POINT_RADIUS)
		]

		self.assertEqual(expected_draw_circle_calls, mock_draw_circle.call_args_list)


if __name__ == '__main__':
	unittest.main()