import unittest
from solution import get_codes


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.strip('\n') for line in open("test-data.txt").readlines()]

    def test_solution(self):
        self.assertEqual(get_codes(self.data), 198)
