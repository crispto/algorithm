def min_path_sum(grid: list[list[int]]) -> int:
    """
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    dp(i,j) = min{ dp(i-1)(j), dp(i)(j-1) } + grid(i, j)
    """
    m, n = len(grid), len(grid[0])
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 and j == 0: continue
            elif i ==0: grid[i][j] += grid[i][j-1]
            elif j ==0: grid[i][j] += grid[i-1][j]
            else: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
if __name__ == "__main__":
    v= [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(min_path_sum(v))
        