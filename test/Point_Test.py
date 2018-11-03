from context import rng
from rng.Point import Point
import unittest

class TestCore(unittest.TestCase):

    def test_points(self):
        p1 = Point(20.0,30.0)
        p2 = Point(20.0,30.0)
        self.assertEqual(p1,p2)

        p3 = Point(30.0,20.0)
        self.assertNotEqual(p1, p3)

        self.assertEqual(round(p1.distTo(p3),5), 14.14214)

        self.assertEqual(p1.distTo(p2), 0.0)

if __name__ == '__main__':
    unittest.main()