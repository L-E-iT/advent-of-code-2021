import unittest
from solution import get_codes, get_max_binary, sort_codes


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.strip('\n') for line in open("test-data.txt").readlines()]

    def test_solution(self):
        self.assertEqual(get_codes(self.data), 230)

    def test_max_binary(self):
        self.assertEqual(get_max_binary(12), 2048)
        self.assertEqual(get_max_binary(8), 128)

    def test_sort_c02(self):
        self.assertEqual(sort_codes(self.data, 16, 0, 0), 10)

    def test_sort_oxygen(self):
        self.assertEqual(sort_codes(self.data, 16, 1, 0), 23)
