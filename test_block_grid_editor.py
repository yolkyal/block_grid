import unittest
import pygame
import block, block_grid, block_grid_editor, block_grid_selector, block_grid_space_manager
from unittest import mock

class TestBlockGridEditor(unittest.TestCase):
	def setUp(self):
		self.bgss = mock.Mock()
		self.block_grid = block_grid.BlockGrid(blocks={(0, 0): block.Block()})
		self.block_grid_selector = block_grid_selector.BlockGridSelector(self.bgss)
		self.block_grid_editor = block_grid_editor.BlockGridEditor(self.bgss, self.block_grid_selector)

	def testSelect(self):
		self.block_grid_selector.select = mock.Mock()
		self.block_grid_selector.select.return_value = (0, 0)

		mouse_pos = mock.Mock()

		e = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=mouse_pos)
		self.block_grid_editor.handle_mouse_button_up(self.block_grid, e)

		self.block_grid_selector.select.assert_called_with(self.block_grid, mouse_pos)
		self.assertEqual([(0, 0)], self.block_grid_editor.selected_blocks)

	def testRaise(self):
		self.block_grid_editor.selected_blocks = [(0, 0)]
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)

		self.block_grid.raise_ = mock.Mock()
		self.block_grid_editor.handle_key_down(self.block_grid, e)

		self.block_grid.raise_.assert_called_with((0, 0), block_grid_editor.DEFAULT_RAISE_INC)

	def testLower(self):
		self.block_grid_editor.selected_blocks = [(0, 0)]
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

		self.block_grid.lower = mock.Mock()
		self.block_grid_editor.handle_key_down(self.block_grid, e)

		self.block_grid.lower.assert_called_with((0, 0), block_grid_editor.DEFAULT_RAISE_INC)

	def testRemove(self):
		grid = block_grid.BlockGrid()
		self.block_grid_editor.selected_blocks = [(0, 0)]
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)

		grid.remove = mock.Mock()
		self.block_grid_editor.handle_key_down(grid, e)

		grid.remove.assert_called_with((0, 0))

	@mock.patch('collision_utils.is_circle_point_collision', return_value = True)
	@mock.patch('block_grid_space_manager.calculate_points')
	def testSelectPoint(self, mock_calculate_points, mock_circle_point_collision):
		mouse_pos = mock.Mock()

		top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		mock_calculate_points.return_value = block_grid_space_manager.BlockSpaceInstance(None, top_points)

		self.block_grid_editor.selected_blocks = [(0, 0)]

		e = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=mouse_pos)
		self.block_grid_editor.handle_mouse_button_up(self.block_grid, e)

		self.assertEqual([0], self.block_grid_editor.selected_points)
		mock_calculate_points.assert_called_once_with((0, 0), self.block_grid.blocks[(0, 0)], self.bgss)
		mock_circle_point_collision.assert_called_once_with(top_points[0], 5, mouse_pos)

	def testRaisePoint(self):
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = [0]

		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
		self.block_grid.raise_point = mock.Mock()
		self.block_grid_editor.handle_key_down(self.block_grid, e)

		self.block_grid.raise_point.assert_called_once_with((0, 0), 0, block_grid_editor.DEFAULT_RAISE_INC)

	def testLowerPoint(self):
		self.block_grid_editor.selected_blocks = [(0, 0)]
		self.block_grid_editor.selected_points = [0]

		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
		self.block_grid.lower_point = mock.Mock()
		self.block_grid_editor.handle_key_down(self.block_grid, e)

		self.block_grid.lower_point.assert_called_once_with((0, 0), 0, block_grid_editor.DEFAULT_RAISE_INC)
		

if __name__ == '__main__':
	unittest.main()
