file_data = [i.rstrip().split(" | ") for i in open("solution-data.txt").readlines()]

# 0 = 6 - 6 but all values from 4 not in number, all values from 1 in number
# 1 = 2* - unqiue
# 2 = 5 - not all 5 characters are in 9
# 3 = 5 - 5 all in 1
# 4 = 4* - unique
# 5 = 5 - all 5 characters in 9
# 6 = 6 - 6 but not all in 1
# 7 = 3* - unique
# 8 = 7* - unique
# 9 = 6 - 6 but all values from 4 in number, all values from 1 in number

# 1, 4, 7, 8, 6, 9, 0, 2, 3, 5


class EncodedNumbers:
    keys = []
    encoded_values = []
    decoded_numbers = {}
    decoded_values = ""

    def __init__(self, keys, encoded_values):
        self.keys = keys
        self.encoded_values = encoded_values
        self.decoded_numbers = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: ""
        }
        self.decoded_values = ""


def generate_encoded_number_list(data):
    return [EncodedNumbers(keys=entry[0].split(" "), encoded_values=entry[1].split(" ")) for entry in data]


# check if string1 contains all elements of string2
def check_occurances(string1, string2):
    list_string1 = list(string1)
    list_string2 = list(string2)
    return all(elem in list_string1 for elem in list_string2)


def decode_numbers(encoded_numbers):
    # find Uniques
    for encoded_number in encoded_numbers:
        # find uniques
        for key in encoded_number.keys:
            if len(key) == 2:
                encoded_number.decoded_numbers[1] = key
            elif len(key) == 4:
                encoded_number.decoded_numbers[4] = key
            elif len(key) == 3:
                encoded_number.decoded_numbers[7] = key
            elif len(key) == 7:
                encoded_number.decoded_numbers[8] = key
        # find others
        for key in encoded_number.keys:
            if len(key) == 6:
                if not check_occurances(key, encoded_number.decoded_numbers[1]):
                    encoded_number.decoded_numbers[6] = key
                elif check_occurances(key, encoded_number.decoded_numbers[1]) \
                        and check_occurances(key, encoded_number.decoded_numbers[4]):
                    encoded_number.decoded_numbers[9] = key
                elif check_occurances(key, encoded_number.decoded_numbers[1]) \
                        and not check_occurances(key, encoded_number.decoded_numbers[4]):
                    encoded_number.decoded_numbers[0] = key
        for key in encoded_number.keys:
            if len(key) == 5:
                if check_occurances(key, encoded_number.decoded_numbers[1]):
                    encoded_number.decoded_numbers[3] = key
                elif check_occurances(encoded_number.decoded_numbers[9], key):
                    encoded_number.decoded_numbers[5] = key
                elif not check_occurances(encoded_number.decoded_numbers[9], key):
                    encoded_number.decoded_numbers[2] = key

        decoded_values = ""
        flipped_decoded_keys = {"".join(sorted(v)): k for k, v in encoded_number.decoded_numbers.items()}
        for value in encoded_number.encoded_values:
            decoded_values += str(flipped_decoded_keys["".join(sorted(value))])
        encoded_number.decoded_values = decoded_values

    return encoded_numbers


def solve(data):
    number_list = generate_encoded_number_list(data)
    decoded_numbers = decode_numbers(number_list)
    total_number = 0
    for decoded_number in decoded_numbers:
        total_number += int(decoded_number.decoded_values)
    return total_number


print(solve(file_data))





