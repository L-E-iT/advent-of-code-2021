import numpy as np

file_data = [line.rstrip() for line in open("solution-data.txt").readlines() if line != '\n']

# Construct 2d array
# modify array values depending on segments of array impacted by heat vents


def generate_graph(coordinate_list, graph):
    for coordinates in coordinate_list:
        if coordinates["x1"] == coordinates["x2"]:
            y_coords = [coordinates["y1"], coordinates["y2"]]
            graph[min(y_coords):max(y_coords)+1, coordinates["x1"]] += 1

        elif coordinates["y1"] == coordinates["y2"]:
            x_coords = [coordinates["x1"], coordinates["x2"]]
            graph[coordinates["y1"], min(x_coords):max(x_coords)+1] += 1
        else:
            if abs(coordinates["y1"] - coordinates["y2"]) == abs(coordinates["x1"] - coordinates["x2"]):
                for i in range(abs(coordinates["y1"] - coordinates["y2"])+1):
                    if coordinates["x1"] > coordinates["x2"] and coordinates["y1"] > coordinates["y2"]:
                        graph[coordinates["y1"]-i, coordinates["x1"]-i] += 1
                    elif coordinates["x1"] < coordinates["x2"] and coordinates["y1"] > coordinates["y2"]:
                        graph[coordinates["y1"]-i, coordinates["x1"]+i] += 1
                    elif coordinates["x1"] > coordinates["x2"] and coordinates["y1"] < coordinates["y2"]:
                        graph[coordinates["y1"]+i, coordinates["x1"]-i] += 1
                    else:
                        graph[coordinates["y1"]+i, coordinates["x1"]+i] += 1

    return graph


def generate_coordinate_list(data_list):
    coordinate_list = []
    for data in data_list:
        data = data.split(" -> ")
        coordinates = {"x1": int(data[0].split(",")[0]), "y1": int(data[0].split(",")[1]),
                       "x2": int(data[1].split(",")[0]), "y2": int(data[1].split(",")[1])}
        coordinate_list.append(coordinates)
    return coordinate_list


def generate_empty_square_array(value):
    return np.zeros(shape=(value, value), dtype=np.uint8)


solution_graph = generate_graph(generate_coordinate_list(file_data), generate_empty_square_array(1000))
print((solution_graph > 1).sum())
