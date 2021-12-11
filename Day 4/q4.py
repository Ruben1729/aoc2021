class Board:
    def __init__(self):
        self.ghost_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.actual_board = []

    def update_board(self, num):
        for i in range(5):
            for j in range(5):
                if self.actual_board[i][j] == num:
                    self.ghost_board[i][j] = 1
                    return

    def add_unused_nums(self):
        num_sum = 0
        for i in range(5):
            for j in range(5):
                if self.ghost_board[i][j] == 0:
                    num_sum += self.actual_board[i][j]

        return num_sum

    def append_line(self, new_line):
        while "" in new_line:
            new_line.remove("")

        for i in range(5):
            new_line[i] = int(new_line[i])

        self.actual_board.append(new_line)

    def check_win(self):
        win = True
        # Horizontal
        for row in self.ghost_board:
            win = True
            for num in row:
                if num == 0:
                    win = False

            if win:
                return True

        # Vertical
        for i in range(5):
            win = True
            for j in range(5):
                if self.ghost_board[j][i] == 0:
                    win = False

            if win:
                return True

        return win


def part_one():
    file = open("input", "r")

    numbers_to_draw = file.readline()
    numbers_to_draw = numbers_to_draw.split(',')

    for i in range(len(numbers_to_draw)):
        numbers_to_draw[i] = int(numbers_to_draw[i])

    boards = []

    for line in file:
        if line == "\n":
            boards.append(Board())
            continue

        boards[len(boards) - 1].append_line(line.split(" "))

    for num_draw in numbers_to_draw:
        for board in boards:
            board.update_board(num_draw)
            if board.check_win():
                print(board.add_unused_nums() * num_draw)
                return


def part_two():
    file = open("input", "r")

    numbers_to_draw = file.readline()
    numbers_to_draw = numbers_to_draw.split(',')

    for i in range(len(numbers_to_draw)):
        numbers_to_draw[i] = int(numbers_to_draw[i])

    boards = []

    for line in file:
        if line == "\n":
            boards.append(Board())
            continue

        boards[len(boards) - 1].append_line(line.split(" "))

    win_counter = 0
    checked_boards = []

    for num_draw in numbers_to_draw:
        for board in boards:
            if board in checked_boards:
                continue

            board.update_board(num_draw)
            if board.check_win():
                if win_counter == len(boards) - 1:
                    print(board.actual_board)
                    print(board.ghost_board)
                    print(board.add_unused_nums() * num_draw)
                    return
                else:
                    win_counter += 1
                    checked_boards.append(board)


if __name__ == '__main__':
    part_two()
