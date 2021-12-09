import unittest
from solution import generate_encoded_number_list, check_occurances, solve


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [i.rstrip().split(" | ") for i in open("test-data.txt").readlines()]

    def test_generate_encoded_number_list(self):
        number_list = generate_encoded_number_list(self.data)
        self.assertEqual(len(number_list[0].keys), 10)
        self.assertEqual(len(number_list[0].encoded_values), 4)

    def test_check_occurance(self):
        result_true = check_occurances("ab", "ba")
        result_false = check_occurances("ab", "cd")
        result_true2 = check_occurances("abc", "ba")
        result_false2 = check_occurances("ab", "abc")
        result_5 = check_occurances("cefabd", "cdfbe")
        result_2 = check_occurances("cefabd", "gcdfa")
        self.assertTrue(result_true)
        self.assertFalse(result_false)
        self.assertTrue(result_true2)
        self.assertFalse(result_false2)
        self.assertTrue(result_5)
        self.assertFalse(result_2)

    def test_decode_numbers(self):
        weird_data = generate_encoded_number_list(self.data)
        result = solve(self.data)
        self.assertEqual(result, 61229)

