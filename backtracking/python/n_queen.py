print("{}, {}, {}".format(__name__, __file__, __package__))


def n_queen(n: int) -> list[list[int]]:
    """
    给出在宽度为n的棋盘上放置n皇后问题的解
    """
    board = [[0 for i in range(n)] for j in range(n)]
    if n_queen_help(board, 0):
        return board


def n_queen_help(board: list[list[int]], row) -> bool:
    if row == len(board):
        return True
    for column in range(len(board)):
        if is_safe(board, [row, column]):
            board[row][column] = 1
            if n_queen_help(board, row+1):
                return True
            board[row][column] = 0
    return False


def is_safe(board: list[list[int]], pos: tuple[int]):
    return not any(board[x][y] == 1 and can_attack((x, y), pos) for x in range(pos[0]) for y in range(len(board)))


def can_attack(v1: tuple[int], v2: tuple[int]):
    if v1[0] == v2[0] or v1[1] == v2[1]:
        return True
    return abs(v1[0] - v2[0]) == abs(v1[1] - v2[1])


if __name__ == "__main__":
    v = n_queen(8)
    for row in v:
        for elem in row:
            print(elem, end=' ')
        print()
