"""
数独问题，一个部分填充的9*9矩阵，让每行、每列、每个3*3小方块里都刚好有1-9这9个数
"""


def solve(matrix: list[list[int]]):
    if solve_tree(matrix, 0):
        print("find a solution !!!!")
        from utils import list_print
        list_print(matrix)
    else:
        print("no solutions")


def solve_tree(matrix: list[list[int]], level: int) -> bool:
    if level == len(matrix) * len(matrix):
        return True
    i, j = level//len(matrix), level % len(matrix)
    if matrix[i][j] == 0:
        for x in range(1, 10):
            if is_safe(matrix, i, j, x):
                matrix[i][j] = x
                if solve_tree(matrix, level+1):
                    return True
                matrix[i][j] = 0
    else:
        return solve_tree(matrix, level+1)
    return False


def is_safe(matrix: list[list[int]], i: int, j: int, x: int) -> bool:
    # row
    if any(matrix[i][v] == x for v in range(len(matrix))):
        return False
    # column
    if any(matrix[v][j] == x for v in range(len(matrix))):
        return False
    # submatrix
    l = 3
    i_start, j_start = (i//l)*l, (j//l)*l
    if any([matrix[i_start+i][j_start+j] == x for i in range(l) for j in range(l)]):
        return False
    return True


if __name__ == "__main__":
    initial_grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]
    solve(initial_grid)
