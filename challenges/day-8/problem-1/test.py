import unittest
from solution import generate_encoded_number_list, find_uniques


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [i.rstrip().split(" | ") for i in open("test-data.txt").readlines()]

    def test_generate_encoded_number_list(self):
        number_list = generate_encoded_number_list(self.data)
        self.assertEqual(len(number_list[0].key), 10)
        self.assertEqual(len(number_list[0].encoded_values), 4)

    def test_find_uniques(self):
        number_list = generate_encoded_number_list(self.data)
        uniques = find_uniques(number_list)
        self.assertEqual(uniques, 26)


