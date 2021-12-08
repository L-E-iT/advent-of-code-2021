import unittest
from solution import get_gas_used, solve


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [int(i) for i in open("test-data.txt").read().split(",")]

    def test_get_gas_used(self):
        gas_used5 = get_gas_used(self.data, 5)
        gas_used2 = get_gas_used(self.data, 2)
        self.assertEqual(gas_used5, 168)
        self.assertEqual(gas_used2, 206)

    def test_solve(self):
        result = solve(self.data)
        self.assertEqual(result, 168)

