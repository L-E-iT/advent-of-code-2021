import unittest
from solution import generate_lanternfish, simulate_day_growth, solve


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = map(int, open("test-data.txt").read().split(","))

    def test_generate_lanternfist(self):
        fish_list = generate_lanternfish(self.data)
        self.assertEqual(fish_list[3], 2)

    def test_simulate_day(self):
        fish_list = generate_lanternfish(self.data)
        one_day_fish_list = simulate_day_growth(fish_list)
        two_day_fish_list = simulate_day_growth(one_day_fish_list)
        self.assertEqual(one_day_fish_list[2], 2)
        print(one_day_fish_list)
        print(two_day_fish_list)
        self.assertEqual(two_day_fish_list[8], 1)

    def test_day_growth_count(self):
        fish_list = generate_lanternfish(self.data)
        days18 = solve(fish_list, 18)
        days80 = solve(fish_list, 80)
        self.assertEqual(sum(days18.values()), 26)
        self.assertEqual(sum(days80.values()), 5934)
