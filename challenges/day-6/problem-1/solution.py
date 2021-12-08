from collections import Counter

file_data = map(int, open("solution-data.txt").read().split(","))


def solve(fish_data, days):
    new_fish_data = fish_data.copy()
    for i in range(days):
        new_fish_data = simulate_day_growth(new_fish_data)
    return new_fish_data


def simulate_day_growth(lantern_fish):
    new_fish_list = {i: 0 for i in range(0, 9)}
    for id, lantern_fish in lantern_fish.items():
        if id == 0:
            new_fish_list[6] += lantern_fish
            new_fish_list[8] += lantern_fish
        else:
            new_fish_list[id-1] += lantern_fish
    return new_fish_list


def generate_lanternfish(data):
    initial_lantern_fish_list = {i: 0 for i in range(0, 8)}
    fish_data = Counter(data)
    for uid, lantern_fish in initial_lantern_fish_list.items():
        initial_lantern_fish_list[uid] += fish_data[uid] or 0
    return initial_lantern_fish_list


print(sum(solve(generate_lanternfish(file_data), 80).values()))
