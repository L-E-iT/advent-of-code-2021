import numpy as np

file_data = [line.rstrip() for line in open("solution-data.txt").readlines() if line != '\n']


def solve_bingo(data):
    numbers, bingo_boards = parse_data(data)
    found_solution = False
    num_sum = 0
    last_number = 0
    while not found_solution:
        for i in range(5, len(numbers)):
            found_solution, num_sum = check_solutions(bingo_boards, numbers[0:i])
            last_number = numbers[i-1]
            if found_solution:
                break

    return num_sum*int(last_number)


def parse_data(data):
    numbers = data[0].split(",")
    bingo_boards = []
    del data[0]

    while len(data) >= 5:
        array = [value for value in [value_list.split() for value_list in data[:5]]]
        bingo_boards.append(np.array(array))
        del data[:5]

    return numbers, bingo_boards


def check_solutions(bingo_boards, called_numbers):
    for array in bingo_boards:
        winnable_rows = get_winnable_rows(array)
        for row in winnable_rows:
            result = all(number in called_numbers for number in row)
            if result:
                unmarked_values = [int(value) for value in array.flatten() if value not in called_numbers]
                return True, sum(unmarked_values)
    return False, []


def get_winnable_rows(bingo_board):
    winnable_rows = []
    for i in range(0, 5):
        winnable_rows.append(bingo_board[i, :].tolist())
        winnable_rows.append(bingo_board[:, i].tolist())
    return winnable_rows


print(solve_bingo(file_data))
