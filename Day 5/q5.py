

def print_map(bomb_map):
    for x in range(len(bomb_map)):
        for y in range(len(bomb_map)):
            print(bomb_map[y][x], end=" ")
        print("\n")


def part_one():
    file = open("input", "r")
    biggest_val = 0
    coordinate_list = []
    for line in file:
        coordinates = line.split("->")

        x_val = int(coordinates[0].split(',')[0])
        y_val = int(coordinates[0].split(',')[1])

        if x_val > biggest_val:
            biggest_val = x_val

        if y_val > biggest_val:
            biggest_val = y_val

        point1 = (x_val, y_val)

        x_val = int(coordinates[1].split(',')[0])
        y_val = int(coordinates[1].split(',')[1])

        point2 = (x_val, y_val)

        if x_val > biggest_val:
            biggest_val = x_val

        if y_val > biggest_val:
            biggest_val = y_val

        coordinate_list.append(point1)
        coordinate_list.append(point2)

    bomb_map = [[0 for c in range(biggest_val + 1)] for r in range(biggest_val + 1)]

    while len(coordinate_list) > 0:
        point1 = coordinate_list.pop(0)
        point2 = coordinate_list.pop(0)

        # Vertical line
        if point1[0] - point2[0] == 0:
            diff = point1[1] - point2[1]
            diff_len = abs(diff) + 1

            i = 0
            while i in range(diff_len):
                bomb_map[point1[0]][(point2[1] if diff > 0 else point1[1]) + i] += 1
                i += 1

        # Horizontal line
        elif point1[1] - point2[1] == 0:
            diff = point1[0] - point2[0]
            diff_len = abs(diff) + 1

            i = 0
            while i in range(diff_len):
                bomb_map[(point2[0] if diff > 0 else point1[0]) + i][point1[1]] += 1
                i += 1

    biggest_counter = 0

    for x in range(len(bomb_map)):
        for y in range(len(bomb_map)):
            if bomb_map[x][y] >= 2:
                biggest_counter += 1

    print(biggest_counter)
    print_map(bomb_map)

    file.close()


def part_two():
    file = open("input", "r")
    biggest_val = 0
    coordinate_list = []
    for line in file:
        coordinates = line.split("->")

        x_val = int(coordinates[0].split(',')[0])
        y_val = int(coordinates[0].split(',')[1])

        if x_val > biggest_val:
            biggest_val = x_val

        if y_val > biggest_val:
            biggest_val = y_val

        point1 = (x_val, y_val)

        x_val = int(coordinates[1].split(',')[0])
        y_val = int(coordinates[1].split(',')[1])

        point2 = (x_val, y_val)

        if x_val > biggest_val:
            biggest_val = x_val

        if y_val > biggest_val:
            biggest_val = y_val

        coordinate_list.append(point1)
        coordinate_list.append(point2)

    bomb_map = [[0 for c in range(biggest_val + 1)] for r in range(biggest_val + 1)]

    while len(coordinate_list) > 0:
        point1 = coordinate_list.pop(0)
        point2 = coordinate_list.pop(0)

        # Vertical line
        if point1[0] - point2[0] == 0:
            diff = point1[1] - point2[1]
            diff_len = abs(diff) + 1

            i = 0
            while i in range(diff_len):
                bomb_map[point1[0]][(point2[1] if diff > 0 else point1[1]) + i] += 1
                i += 1

        # Horizontal line
        elif point1[1] - point2[1] == 0:
            diff = point1[0] - point2[0]
            diff_len = abs(diff) + 1

            i = 0
            while i in range(diff_len):
                bomb_map[(point2[0] if diff > 0 else point1[0]) + i][point1[1]] += 1
                i += 1

        # 45 degree lines
        elif abs((point2[1] - point1[1]) / (point2[0] - point1[0])) == 1:
            print(point1)
            print(point2)
            diffx = point1[0] - point2[0] #  8
            diffy = point1[1] - point2[1] # -8

            diff_len = abs(diffx) + 1

            i = 0
            while i in range(diff_len):
                bomb_map[point2[0] + (i if diffx > 0 else -i)][point2[1] + (i if diffy > 0 else -i)] += 1
                i += 1

    biggest_counter = 0

    for x in range(len(bomb_map)):
        for y in range(len(bomb_map)):
            if bomb_map[x][y] >= 2:
                biggest_counter += 1

    print(biggest_counter)
    # print_map(bomb_map)

    file.close()


if __name__ == '__main__':
    part_two()
