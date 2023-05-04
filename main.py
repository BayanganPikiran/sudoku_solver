board = [
    [0, 2, 0, 8, 0, 4, 0, 9, 7],
    [3, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0, 9, 0, 2, 4],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 5, 0, 6, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 8, 3, 0, 0],
    [6, 0, 0, 0, 9, 0, 0, 7, 8]
]


def print_board(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print("---------------")
        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]), end="")


def find_unknown(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
    return None


def validate(bd, num, pos):
    # through row
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False
    # through  column
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    # through box
    box_x_pos = pos[0] // 3
    box_y_pos = pos[1] // 3

    for i in range(box_x_pos * 3, box_x_pos * 3 + 3):
        for j in range(box_y_pos * 3, box_y_pos * 3 + 3):
            if bd[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_sudoku(bd):
    solving = find_unknown(bd)
    if not solving:
        return True
    else:
        row, col = solving
    for i in range(1, 10):
        if validate(bd, i, (row, col)):
            bd[row][col] = i

            if solve_sudoku(bd):
                return True

            bd[row][col] = 0

    return False


print_board(board)
solve_sudoku(board)
print_board(board)