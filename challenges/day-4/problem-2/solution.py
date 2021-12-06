import numpy as np

file_data = [line.rstrip() for line in open("solution-data.txt").readlines() if line != '\n']


class BingoBoards:
    boards = {}
    final_boards = {}

    def __init__(self, bingoboards):
        self.boards = {k: v for k, v in enumerate(bingoboards)}


def solve_bingo(data):
    numbers, bingo_boards = parse_data(data)
    bingo_boards.final_boards = bingo_boards.boards.copy()
    final_num_sum = 0
    last_number = 0
    for i in range(5, len(numbers)):
        found_solution, num_sum = check_solutions(bingo_boards, numbers[0:i])
        if found_solution:
            last_number = numbers[i - 1]
            final_num_sum = num_sum
            break

    return final_num_sum*int(last_number)


def parse_data(data):
    numbers = data[0].split(",")
    bingo_boards = []
    del data[0]

    while len(data) >= 5:
        array = [value for value in [value_list.split() for value_list in data[:5]]]
        bingo_boards.append(np.array(array))
        del data[:5]

    boards_object = BingoBoards(bingo_boards)

    return numbers, boards_object


def check_solutions(bingo_boards, called_numbers):
    for key, array in bingo_boards.boards.items():
        if key not in bingo_boards.final_boards.keys():
            break
        winnable_rows = get_winnable_rows(array)
        for row in winnable_rows:
            result = all(number in called_numbers for number in row)
            if result:
                unmarked_values = [int(value) for value in array.flatten() if value not in called_numbers]
                if len(bingo_boards.final_boards) > 1:
                    del bingo_boards.final_boards[key]
                    break
                elif len(bingo_boards.final_boards) == 1:
                    print("we win?")
                    return True, sum(unmarked_values)
    bingo_boards.boards = bingo_boards.final_boards.copy()
    return False, []


def get_winnable_rows(bingo_board):
    winnable_rows = []
    for i in range(0, 5):
        winnable_rows.append(bingo_board[i, :].tolist())
        winnable_rows.append(bingo_board[:, i].tolist())
    return winnable_rows


print(solve_bingo(file_data))
