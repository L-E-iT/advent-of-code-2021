import unittest
from solution import check_depth


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.strip('\n') for line in open("test-data.txt").readlines()]

    def test_solution(self):
        self.assertEqual(check_depth(self.data), 150)
