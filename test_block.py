import unittest
from block import Block


class TestBlock(unittest.TestCase):
	def setUp(self):
		self.start_height = 20
		self.block = Block(self.start_height)

	def testBlock(self):
		for i in range(4):
			self.assertEqual(self.start_height, self.block.vertex_heights[i])

	def testBlockRaise(self):
		block = self.block.raise_(10)
		for i in range(4):
			self.assertEqual(self.start_height + 10, block.vertex_heights[i])

	def testBlockLower(self):
		block = self.block.lower(10)
		for i in range(4):
			self.assertEqual(self.start_height - 10, block.vertex_heights[i])

	def testBlockPointRaise(self):
		block = self.block.raise_point(0, 10)
		self.assertEqual(self.start_height + 10, block.vertex_heights[0])
		self.assertEqual(self.start_height, block.vertex_heights[1])
		self.assertEqual(self.start_height, block.vertex_heights[2])
		self.assertEqual(self.start_height, block.vertex_heights[3])

	def testBlockPointLower(self):
		block = self.block.lower_point(0, 10)
		self.assertEqual(self.start_height - 10, block.vertex_heights[0])
		self.assertEqual(self.start_height, block.vertex_heights[1])
		self.assertEqual(self.start_height, block.vertex_heights[2])
		self.assertEqual(self.start_height, block.vertex_heights[3])


if __name__ == '__main__':
	unittest.main()