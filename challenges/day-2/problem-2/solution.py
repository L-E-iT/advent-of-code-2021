data = [line.strip('\n') for line in open("solution-data.txt").readlines()]


def check_depth(instructions_list):
    vertical = 0
    aim = 0
    horizontal = 0

    for instruction in instructions_list:
        direction, distance = instruction.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            vertical += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

    return vertical * horizontal


print(check_depth(data))
