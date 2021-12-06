import unittest
from solution import solve_bingo, parse_data, get_winnable_rows, check_solutions


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.rstrip() for line in open("test-data.txt").readlines() if line != '\n']

    def test_bingo_result(self):
        self.assertEqual(solve_bingo(self.data), 1924)

    def test_parse_data(self):
        numbers, bingo_boards = parse_data(self.data)
        self.assertEqual(len(numbers), 27)
        self.assertEqual(len(bingo_boards.boards), 3)

    def test_winnable_rows(self):
        numbers, bingo_boards = parse_data(self.data)
        winnable_rows = get_winnable_rows(bingo_boards.boards[0])
        self.assertEqual(len(winnable_rows), 10)

    def test_check_fail_solutions(self):
        numbers, bingo_boards = parse_data(self.data)
        bingo_boards.final_boards = bingo_boards.boards.copy()
        called_numbers = ["7", "4", "9", "5", "11", "17", "23", "2", "0", "14", "21", "24"]
        found, num_sum = check_solutions(bingo_boards, called_numbers)
        self.assertFalse(found)
        self.assertEqual(num_sum, [])

    def test_pass_solution(self):
        numbers, bingo_boards = parse_data(self.data)
        del bingo_boards.boards[0]
        del bingo_boards.boards[2]
        bingo_boards.final_boards = bingo_boards.boards.copy()
        called_numbers = ["7", "4", "9", "5", "11", "17", "23", "2", "0", "14", "21", "24", "10", "16", "13"]
        found, num_sum = check_solutions(bingo_boards, called_numbers)
        self.assertTrue(found)
        self.assertEqual(num_sum, 148)
