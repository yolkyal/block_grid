import unittest
from unittest import mock
from block_grid.src import block_grid, block_grid_save_loader


class TestBlockGridSaveLoader(unittest.TestCase):
	def setUp(self):
		self.dest_folder = '/tmp'
		self.block_grid_name = 'block_grid'
		self.block_grid = block_grid.BlockGrid()
		self.block_grid_save_loader = block_grid_save_loader.BlockGridSaveLoader(self.dest_folder)

	@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="{\"(0, 0)\": \"[1, 1, 1, 1]\"}")
	def testLoad(self, mock_open):
		result = self.block_grid_save_loader.load(self.block_grid_name)

		mock_open.assert_called_once_with(self.dest_folder + '/' + self.block_grid_name + '.bg')
		self.assertEqual(len(result.blocks), 1)
		self.assertEqual([1, 1, 1, 1], result.blocks.get((0, 0)).vertex_heights)

	@mock.patch("builtins.open", new_callable=mock.mock_open)
	def testSave(self, mock_open):
		self.mock_file = mock_open.return_value

		self.block_grid_save_loader.save(self.block_grid, self.block_grid_name)

		mock_open.assert_called_once_with(self.dest_folder + '/' + self.block_grid_name + '.bg', 'w')
		self.mock_file.write.assert_called_once_with("{\"(0, 0)\": \"[1, 1, 1, 1]\"}")