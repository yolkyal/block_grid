import unittest
import block_grid_drawer
from unittest import mock


class TestBlockGridDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.block_grid = mock.Mock()
		self.block_drawer = mock.Mock()
		self.block_grid_drawer = block_grid_drawer.BlockGridDrawer(self.block_drawer)

		self.block_k1 = (0, 0)
		self.block_k2 = (1, 1)
		self.block_1 = mock.Mock()
		self.block_2 = mock.Mock()
		self.block_grid.blocks = {self.block_k1 : self.block_1, self.block_k2 : self.block_2}

	
	def testDrawMesh(self):	
		self.block_grid_drawer.draw_mesh(self.block_grid, self.d_surf)

		expected_block_drawer_draw_mesh_calls = [
		mock.call(self.block_k1, self.block_1, self.d_surf),
		mock.call(self.block_k2, self.block_2, self.d_surf)
		]

		self.assertEqual(expected_block_drawer_draw_mesh_calls, self.block_drawer.draw_mesh.call_args_list)

	def testDrawFill(self):
		self.block_grid_drawer.draw_fill(self.block_grid, self.d_surf)

		expected_block_drawer_draw_fill_calls = [
		mock.call(self.block_k1, self.block_1, self.d_surf),
		mock.call(self.block_k2, self.block_2, self.d_surf)
		]

		self.assertEqual(expected_block_drawer_draw_fill_calls, self.block_drawer.draw_fill.call_args_list)


if __name__ == '__main__':
	unittest.main()