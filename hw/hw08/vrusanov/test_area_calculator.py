import unittest
from math import pi

from area_calculator import rectangle_area, triangle_area, circle_area


class TestAreaCalculator(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 5), 10)
        self.assertEqual(triangle_area(0, 5), 0)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2), pi * 4)


if __name__ == "__main__":
    unittest.main()
