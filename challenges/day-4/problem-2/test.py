import unittest
from solution import get_codes, get_max_binary, sort_codes


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.strip('\n') for line in open("test-data.txt").readlines()]
