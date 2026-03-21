import os.path


def check_bounds(row, col):
    return 0 <= row < 19 and 0 <= col < 19


def solve_game(file):
    board = []
    for _ in range(19):
        line = list(map(int, file.readline().split()))
        board.append(line)

    # Вправо, Вниз, Вниз-Вправо, Вгору-Вправо
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for row in range(19):
        for column in range(19):
            if board[row][column] == 0:
                continue

            color = board[row][column]

            for dx, dy in directions:
                count = 1
                next_row = row + dx
                next_col = column + dy

                while check_bounds(next_row, next_col) and board[next_row][next_col] == color:
                    count += 1
                    next_row += dx
                    next_col += dy

                if count == 5:
                    prev_row = row - dx
                    prev_col = column - dy

                    if not check_bounds(prev_row, prev_col) or board[prev_row][prev_col] != color:
                        print(color)
                        print(f"{row + 1} {column + 1}")
                        return

    print(0)


def main():

    filename = "input.txt"

    if not os.path.exists(filename):
        print(f"File {filename} doesn't exist")
        print("Please make sure the file is created in the same folder as the script")
        return

    with open(filename, "r") as file:
        cases = int(file.readline().strip())
        for _ in range(cases):
            solve_game(file)


if __name__ == "__main__":
    main()
