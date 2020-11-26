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
    """
    每一个将要决定的空位相当于状态树的一行，开始时位于[0,0]，到[8,9]结束，也就是说 level 从0到81结束，
    在该图的当前状态下安全的数字相当于树的一个子节点，
    """
    if level == len(matrix) * len(matrix):
        return True
    # i, j 是当前要决定的下标
    i, j = level//len(matrix), level % len(matrix)
    if matrix[i][j] == 0:
        # 为0 代表未决定的， 可能衍生出多个子节点
        # 需要用回溯递归dfs搜索
        for x in range(1, 10):
            if is_safe(matrix, i, j, x):
                matrix[i][j] = x
                if solve_tree(matrix, level+1):
                    return True
                matrix[i][j] = 0
    else:
        # 已经决定的节点，只会衍生出一个子节点
        return solve_tree(matrix, level+1)
    return False


def is_safe(matrix: list[list[int]], i: int, j: int, x: int) -> bool:
    """
    满足三个条件，每行、每列、已经子方块内没有重复
    """
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
