"""
    获取n个树中取k个的全部排列
"""


def all_permutations(n: int, k: int) -> None:
    if n < k:
        raise("无效参数")
    used = [0 for i in range(n)]
    all_permutations_help(n, k, [], used)


def all_permutations_help(n: int, k: int, tmp: list[int], used: list[int]):
    if len(tmp) == k:
        print(tmp)
        return

    for i in range(n):
        if used[i] == 0:
            tmp.append(i+1)
            used[i] = 1
            all_permutations_help(n, k, tmp, used)
            used[i] = 0
            tmp.pop()


if __name__ == "__main__":
    all_permutations(4, 2)
