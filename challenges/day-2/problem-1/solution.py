data = [line.strip('\n') for line in open("solution-data.txt").readlines()]


def check_depth(instructions_list):
    vertical = 0
    horizontal = 0

    for instruction in instructions_list:
        direction, distance = instruction.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        elif direction == "up":
            vertical -= distance
        elif direction == "down":
            vertical += distance

    return vertical * horizontal


print(check_depth(data))
