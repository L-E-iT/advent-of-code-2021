import unittest
from solution import generate_empty_square_array, generate_coordinate_list, generate_graph


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [line.rstrip() for line in open("test-data.txt").readlines() if line != '\n']

    def test_array_creation(self):
        self.array = generate_empty_square_array(10)
        self.assertEqual(self.array.size, 100)

    def test_coordinate_list_creation(self):
        self.test_data = ['0,9 -> 5,9', '8,0 -> 0,8']
        return_data = generate_coordinate_list(self.test_data)
        self.assertEqual(return_data[0]["x1"], 0)
        self.assertEqual(return_data[1]["y2"], 8)

    def test_generate_graph(self):
        graph = generate_empty_square_array(10)
        coordinate_list = generate_coordinate_list(self.data)
        solution_graph = generate_graph(coordinate_list, graph)
        print(solution_graph)
        self.assertEqual((solution_graph >= 2).sum(), 5)

    def test_coordinate_failure(self):
        self.test_data = ['0,9 -> 1,8', '2,9 -> 5,6', '9,9 -> 8,8']
        graph = generate_empty_square_array(10)
        coordinate_list = generate_coordinate_list(self.test_data)
        solution_graph = generate_graph(coordinate_list, graph)
        self.assertEqual((solution_graph >= 1).sum(), 0)
