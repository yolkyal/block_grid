import pygame, unittest
from block_grid.src import block_grid, block_grid_selector, block_grid_hoverer
from unittest import mock


class TestBlockGridHoverer(unittest.TestCase):
	def setUp(self):
		self.bgss = mock.Mock()
		self.block_grid = mock.Mock()
		self.block_grid_selector = block_grid_selector.BlockGridSelector(self.bgss)
		self.block_grid_hoverer = block_grid_hoverer.BlockGridHoverer(self.block_grid_selector)

	def testUpdate(self):
		self.assertEqual(None, self.block_grid_hoverer.hovered)

		self.block_grid_selector.select = mock.MagicMock(return_value=(0, 0))
		mouse_pos = (100, 100)
		self.block_grid_hoverer.update(self.block_grid, mouse_pos)

		self.assertEqual((0, 0), self.block_grid_hoverer.hovered)
		self.block_grid_selector.select.assert_called_with(self.block_grid, mouse_pos)

