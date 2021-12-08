file_data = [int(i) for i in open("solution-data.txt").read().split(",")]


def solve(file_data):
    max_value = max(file_data)
    data_storage = {i: 0 for i in range(1, max_value + 1)}
    for i in range(0, max_value+1):
        data_storage[i] = get_gas_used(file_data, i)

    return min(data_storage.values())


def get_gas_used(data, position):
    diff_list = [abs(x-position) for x in data]
    gas_list = [(((x**2)+x)/2) for x in diff_list]

    return sum(gas_list)


print(solve(file_data))
