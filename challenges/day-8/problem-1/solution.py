file_data = [i.rstrip().split(" | ") for i in open("solution-data.txt").readlines()]

# 1 = 2*
# 2 = 5
# 3 = 5
# 4 = 4*
# 5 = 5
# 6 = 6
# 7 = 3*
# 8 = 7*
# 9 = 6

class EncodedNumbers:
    key = []
    encoded_values = []

    def __init__(self, key, encoded_values):
        self.key = key
        self.encoded_values = encoded_values


def generate_encoded_number_list(data):
    return [EncodedNumbers(key=entry[0].split(" "), encoded_values=entry[1].split(" ")) for entry in data]


def find_uniques(encoded_numbers):
    count = 0
    for number in encoded_numbers:
        for encoded_number in number.encoded_values:
            if len(encoded_number) == 2 or \
                    len(encoded_number) == 4 or \
                    len(encoded_number) == 7 or \
                    len(encoded_number) == 3:
                count += 1
    return count


print(find_uniques(generate_encoded_number_list(file_data)))
