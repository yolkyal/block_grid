import unittest
from block import Block


class TestBlock(unittest.TestCase):
	def setUp(self):
		self.block = Block()

	def testBlock(self):
		for i in range(4):
			self.assertEqual(1, self.block.vertex_heights[i])

	def testBlockRaise(self):
		block = self.block.raise_(1)
		for i in range(4):
			self.assertEqual(2, block.vertex_heights[i])

	def testBlockLower(self):
		block = self.block.lower(1)
		for i in range(4):
			self.assertEqual(0, block.vertex_heights[i])

	def testBlockPointRaise(self):
		block = self.block.raise_point(0, 1)
		self.assertEqual(2, block.vertex_heights[0])
		self.assertEqual(1, block.vertex_heights[1])
		self.assertEqual(1, block.vertex_heights[2])
		self.assertEqual(1, block.vertex_heights[3])

	def testBlockPointLower(self):
		block = self.block.lower_point(0, 1)
		self.assertEqual(0, block.vertex_heights[0])
		self.assertEqual(1, block.vertex_heights[1])
		self.assertEqual(1, block.vertex_heights[2])
		self.assertEqual(1, block.vertex_heights[3])


if __name__ == '__main__':
	unittest.main()