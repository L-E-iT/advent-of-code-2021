data = [int(line.strip('\n')) for line in open("solution-data.txt").readlines()]


def check_increase(data):
    increase_count = 0

    for i in range(len(data)):
        if i+1 >= len(data):
            break
        if data[i] < data[i+1]:
            increase_count += 1
    return increase_count


print(check_increase(data))
