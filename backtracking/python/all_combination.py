"""
    获取n个数中取k个的全部组合形式
"""


def generate_all_combinations(n: int, k: int) -> list[int]:
    """
    >>> generate_all_combinations(4, 2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    result = []
    generate_all_combinations_dfs(1, n, k, [], result)
    return result


def generate_all_combinations_dfs(start: int, total: int, k: int, tmp: list[int], result: list[int]):
    if k == 0:
        result.append(tmp[:])
        return
    for i in range(start, total - k + 2):
        tmp.append(i)
        generate_all_combinations_dfs(i+1, total, k-1, tmp, result)
        tmp.pop()


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = any(i > 5 for i in a)
    print(b)
