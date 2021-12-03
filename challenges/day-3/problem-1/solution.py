data = [line.strip('\n') for line in open("solution-data.txt").readlines()]


def get_codes(data):
    gamma_code = []
    epsilon_code = []
    for i in range(len(data[1])):
        ones, zeros = 0, 0
        for code in data:
            if int(code[i]) == 1:
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma_code.append("1")
            epsilon_code.append("0")
        else:
            gamma_code.append("0")
            epsilon_code.append("1")

    gamma = int(''.join(gamma_code), 2)
    epsilon = int(''.join(epsilon_code), 2)

    return gamma * epsilon


print(get_codes(data))
