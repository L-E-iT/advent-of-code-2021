import unittest
from solution import get_gas_used, solve


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [int(i) for i in open("test-data.txt").read().split(",")]

    def test_get_gas_used(self):
        gas_used2 = get_gas_used(self.data, 2)
        gas_used10 = get_gas_used(self.data, 10)
        self.assertEqual(gas_used2, 37)
        self.assertEqual(gas_used10, 71)

    def test_solve(self):
        result = solve(self.data)
        self.assertEqual(result, 37)

