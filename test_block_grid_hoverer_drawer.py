import pygame, unittest
import block_grid_hoverer_drawer, block_grid_space_manager
from unittest import mock


class TestBlockGridHovererDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.bgss = mock.Mock()
		self.grid = mock.Mock()
		self.hoverer = mock.Mock()
		self.points = mock.Mock()
		self.points.top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		self.hoverer_drawer = block_grid_hoverer_drawer.BlockGridHovererDrawer(self.bgss)

	@mock.patch('block_grid_space_manager.calculate_points')
	@mock.patch('pygame.draw.polygon')
	def testDraw(self, mock_draw_polygon, mock_calculate_points):
		mock_calculate_points.return_value = self.points

		self.grid.blocks = {(0, 0): mock.Mock()}
		
		self.hoverer.hovered=(0, 0)
		self.hoverer_drawer.draw(self.grid, self.hoverer, self.d_surf)

		mock_draw_polygon.assert_called_with(self.d_surf, block_grid_hoverer_drawer.DEFAULT_HOVER_COL, self.points.top_points)


if __name__ == '__main__':
	unittest.main()