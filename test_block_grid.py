import unittest
from block_grid import BlockGrid
from block import Block


class TestBlockGrid(unittest.TestCase):
	def setUp(self):
		self.size=3
		self.grid = BlockGrid(self.size)

	def testGridKeys(self):
		expected = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (1, 2), (2, 1), (2, 2)]
		self.assertEqual(expected, list(self.grid.blocks.keys()))

	def testBlocksSetup(self):
		block = self.grid.blocks[(0, 0)]
		self.assertIsInstance(block, Block)
		for i in range(4):
			self.assertEqual(1, block.vertex_heights[i])

	def testRaise(self):
		grid = self.grid.raise_((0, 0), 1)
		block = grid.blocks[(0, 0)]
		for i in range(4):
			self.assertEqual(2, block.vertex_heights[i])

	def testLower(self):
		grid = self.grid.lower((0, 0), 1)
		block = grid.blocks[(0, 0)]
		for i in range(4):
			self.assertEqual(0, block.vertex_heights[i])

	def testRaisePoint(self):
		grid = self.grid.raise_point((0, 0), 0, 1)
		block = grid.blocks[(0, 0)]
		self.assertEqual(2, block.vertex_heights[0])
		self.assertEqual(1, block.vertex_heights[1])
		self.assertEqual(1, block.vertex_heights[2])
		self.assertEqual(1, block.vertex_heights[3])

	def testLowerPoint(self):
		grid = self.grid.lower_point((0, 0), 0, 1)
		block = grid.blocks[(0, 0)]
		self.assertEqual(0, block.vertex_heights[0])
		self.assertEqual(1, block.vertex_heights[1])
		self.assertEqual(1, block.vertex_heights[2])
		self.assertEqual(1, block.vertex_heights[3])

	def testRemove(self):
		grid = self.grid.remove((0, 0))
		self.assertEqual([(0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (1, 2), (2, 1), (2, 2)], list(grid.blocks.keys()))


if __name__ == '__main__':
	unittest.main()