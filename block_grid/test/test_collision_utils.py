import unittest
from block_grid.src import collision_utils

class TestCollisionUtils(unittest.TestCase):

	def testTriangleCollision(self):
		pt0 = (0, 0)
		pt1 = (10, 0)
		pt2 = (10, 10)

		for i in range(11):
			self.assertTrue(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (i, i)))

		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (-1, 0)))
		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (0, -1)))

		self.assertTrue(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (10, 0)))
		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (10, -1)))
		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (11, 0)))

		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (10, 11)))
		self.assertFalse(collision_utils.is_triangle_point_collision(pt0, pt1, pt2, (11, 10)))

	def testDiamondCollision(self):
		pt0 = (0, 10)
		pt1 = (10, 0)
		pt2 = (20, 10)
		pt3 = (10, 20)

		# CENTRE
		self.assertTrue(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (10, 10)))

		# LEFT CORNER
		self.assertTrue(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 9)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (-1, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 11)))

		# TOP CORNER
		self.assertTrue(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (10, 0)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (9, 0)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (10, -1)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (11, 0)))

		# RIGHT CORNER
		self.assertTrue(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 9)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (-1, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 11)))

		# BOTTOM CORNER
		self.assertTrue(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 9)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (-1, 10)))
		self.assertFalse(collision_utils.is_diamond_point_collision(pt0, pt1, pt2, pt3, (0, 11)))

	def testCircleCollision(self):
		centre = (100, 100)
		radius = 5

		self.assertTrue(collision_utils.is_circle_point_collision(centre, radius, (100, 100)))
		self.assertTrue(collision_utils.is_circle_point_collision(centre, radius, (100 - radius, 100)))
		self.assertTrue(collision_utils.is_circle_point_collision(centre, radius, (100 + radius, 100)))
		self.assertTrue(collision_utils.is_circle_point_collision(centre, radius, (100, 100 - radius)))
		self.assertTrue(collision_utils.is_circle_point_collision(centre, radius, (100, 100 + radius)))

		self.assertFalse(collision_utils.is_circle_point_collision(centre, radius, (100 - radius - 1, 100)))
		self.assertFalse(collision_utils.is_circle_point_collision(centre, radius, (100 + radius + 1, 100)))
		self.assertFalse(collision_utils.is_circle_point_collision(centre, radius, (100, 100 - radius - 1)))
		self.assertFalse(collision_utils.is_circle_point_collision(centre, radius, (100, 100 + radius + 1)))

