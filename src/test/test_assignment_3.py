import unittest
from main.assignment_3 import euler, rk, f

class TestAssignment3(unittest.TestCase):
    def test_euler(self):
        self.assertAlmostEqual(euler(f, 0, 1, 2, 10), 1.2446380979332121, places=6)

    def test_rk4(self):
        self.assertAlmostEqual(rk(f, 0, 1, 2, 10), 1.251316587879806, places=6)

if __name__ == '__main__':
    unittest.main()
