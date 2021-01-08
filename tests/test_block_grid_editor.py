import unittest
import pygame
import block_grid_editor
from unittest import mock

class TestBlockGridEditor(unittest.TestCase):
	def setUp(self):
		self.bgss = mock.Mock()
		self.block_grid = mock.Mock()
		self.block_grid_selector = mock.Mock()
		self.block_grid_editor = block_grid_editor.BlockGridEditor(self.bgss, self.block_grid_selector)
		self.mouse_pos = mock.Mock()
		pygame.init()

	def tearDown(self):
		pygame.quit()

	def testSelectWithNoneSelected(self):
		# GIVEN
		self.block_grid_selector.select.return_value = (0, 0)
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)

		# THEN
		self.block_grid_selector.select.assert_called_with(self.block_grid, self.mouse_pos)
		self.assertEqual({(0, 0)}, self.block_grid_editor.selected_blocks)

	def testSelectWithSelected(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0), (0, 1)}
		self.block_grid_selector.select.return_value = (1, 1)
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)

		# THEN
		self.assertEqual({(1, 1)}, self.block_grid_editor.selected_blocks)

	@mock.patch('pygame.key.get_pressed')
	def testSelectWithSelectedAndShiftPressed(self, mock_get_pressed):
		mock_get_pressed.return_value = get_keys_pressed_with_lshift()
		self.block_grid_editor.selected_blocks = {(0, 0), (0, 1)}
		self.block_grid_selector.select.return_value = (1, 1)
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)

		# THEN
		self.assertEqual({(0, 0), (0, 1), (1, 1)}, self.block_grid_editor.selected_blocks)

	def testMouseDragWithNoneSelected(self):
		# GIVEN
		self.block_grid_selector.select.side_effect = [(0, 0), (0, 1), (0, 1)]
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e3 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e4 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)
		self.block_grid_editor.handle_event(self.block_grid, e3)
		self.block_grid_editor.handle_event(self.block_grid, e4)

		# THEN
		self.assertEqual({(0, 0), (0, 1)}, self.block_grid_editor.selected_blocks)

	def testMouseDragWithSelected(self):
		self.block_grid_editor.selected_blocks = {(0, 0), (0, 1)}
		self.block_grid_selector.select.side_effect = [(1, 1), (1, 2), (1, 2)]
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e3 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e4 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)
		self.block_grid_editor.handle_event(self.block_grid, e3)
		self.block_grid_editor.handle_event(self.block_grid, e4)

		# THEN
		self.assertEqual({(1, 1), (1, 2)}, self.block_grid_editor.selected_blocks)

	@mock.patch('pygame.key.get_pressed')
	def testMouseDragWithSelectedAndShiftPressed(self, mock_get_pressed):
		mock_get_pressed.return_value = get_keys_pressed_with_lshift()
		self.block_grid_editor.selected_blocks = {(0, 0), (0, 1)}
		self.block_grid_selector.select.side_effect = [(1, 1), (1, 2), (1, 2)]
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e3 = pygame.event.Event(pygame.MOUSEMOTION, buttons=[1], pos=self.mouse_pos)
		e4 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)
		self.block_grid_editor.handle_event(self.block_grid, e3)
		self.block_grid_editor.handle_event(self.block_grid, e4)

		# THEN
		self.assertEqual({(0, 0), (0, 1), (1, 1), (1, 2)}, self.block_grid_editor.selected_blocks)

	@mock.patch('collision_utils.is_circle_point_collision', return_value = False)
	@mock.patch('block_grid_space_manager.calculate_points')
	def testDeselectAllWithOneSelected(self, mock_calculate_points, mock_circle_point_collision):
		# GIVEN

		self.block_grid_editor.selected_blocks = {(0, 0)}
		self.block_grid_selector.select.return_value = None
		e1 = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=self.mouse_pos)
		e2 = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e1)
		self.block_grid_editor.handle_event(self.block_grid, e2)

		# THEN
		self.assertEqual(set(), self.block_grid_editor.selected_blocks)

	@mock.patch('collision_utils.is_circle_point_collision', return_value = True)
	@mock.patch('block_grid_space_manager.calculate_points')
	def testSelectPoint(self, mock_calculate_points, mock_circle_point_collision):
		# GIVEN
		self.block_grid.blocks = {(0, 0): mock.Mock()}
		self.block_grid_editor.selected_blocks = {(0, 0)}

		top_points = [(9, 10), (11, 12), (13, 14), (15, 16)]
		mock_block_space_instance = mock.Mock()
		mock_block_space_instance.top_points = top_points
		mock_calculate_points.return_value = mock_block_space_instance

		mock_circle_point_collision.return_value = True

		mouse_pos = mock.Mock()
		e = pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=mouse_pos)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN 
		self.assertEqual({0}, self.block_grid_editor.selected_points)
		mock_calculate_points.assert_called_once_with((0, 0), self.block_grid.blocks[(0, 0)], self.bgss)
		mock_circle_point_collision.assert_called_once_with(top_points[0], 5, mouse_pos)

	def testRaise(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0)}
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN
		self.block_grid.raise_.assert_called_with((0, 0), block_grid_editor.DEFAULT_RAISE_INC)

	def testLower(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0)}
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN
		self.block_grid.lower.assert_called_with((0, 0), block_grid_editor.DEFAULT_RAISE_INC)

	def testRemove(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0)}
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN
		self.block_grid.remove.assert_called_with((0, 0))

	def testRaisePoint(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0)}
		self.block_grid_editor.selected_points = {0}
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN
		self.block_grid.raise_point.assert_called_once_with((0, 0), 0, block_grid_editor.DEFAULT_RAISE_INC)

	def testLowerPoint(self):
		# GIVEN
		self.block_grid_editor.selected_blocks = {(0, 0)}
		self.block_grid_editor.selected_points = {0}
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

		# WHEN
		self.block_grid_editor.handle_event(self.block_grid, e)

		# THEN
		self.block_grid.lower_point.assert_called_once_with((0, 0), 0, block_grid_editor.DEFAULT_RAISE_INC)

def get_keys_pressed_with_lshift():
	keys_pressed = [0] * 512
	keys_pressed[pygame.K_LSHIFT] = 1
	return tuple(keys_pressed)

		
