data = [int(line.strip('\n')) for line in open("solution-data.txt").readlines()]


def check_increase(data):
    increase_count = 0

    for i in range(len(data)):
        if i+3 >= len(data):
            break
        first_set = data[i] + data[i + 1] + data[i + 2]
        second_set = data[i + 1] + data[i + 2] + data[i + 3]

        if first_set < second_set:
            increase_count += 1
    return increase_count


print(check_increase(data))
