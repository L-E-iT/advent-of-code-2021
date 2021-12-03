import unittest
from solution import check_increase


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [int(line.strip('\n')) for line in open("test-data.txt").readlines()]

    def test_solution(self):
        self.assertEqual(check_increase(self.data), 7)
