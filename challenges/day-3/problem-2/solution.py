data = [line.strip('\n') for line in open("solution-data.txt").readlines()]

# Oxygen most common, take 1, filter 1
# C02 least common, take 0, filter 0


def get_codes(data):
    max_binary = get_max_binary(len(data[1]))
    c02 = sort_codes(data, max_binary, 0, 0)
    oxygen = sort_codes(data, max_binary, 1, 0)
    return c02 * oxygen


def get_max_binary(length):
    blank_binary = ['0' for i in range(length)]
    blank_binary[0] = "1"
    return int(''.join(blank_binary), 2)


def sort_codes(data, max_binary, filter_flag, index):
    if filter_flag == 1:
        greater_than = [i for i in data if int(i[index:], 2) >= max_binary]
        less_than = [i for i in data if int(i[index:], 2) < max_binary]
        if len(greater_than) >= len(less_than):
            results = greater_than
        else:
            results = less_than
    else:
        greater_than = [i for i in data if int(i[index:], 2) >= max_binary]
        less_than = [i for i in data if int(i[index:], 2) < max_binary]
        if len(greater_than) >= len(less_than):
            results = less_than
        else:
            results = greater_than

    return sort_codes(results, max_binary/2, filter_flag, index+1) if len(results) != 1 else int(results[0], 2)


print(get_codes(data))
