def search_room(v):
    """
    [[1, 2, 3], [3], [2], []],
    每个房间里通向其他房间的钥匙
    """
    if search_dfs(v, 0, 1, [0]):
        return True
    return False


def search_dfs(v, current, level, walked):
    if level == len(v):
        return True
    for i in v[current]:
        if not i in walked:
            walked.append(i)
            if search_dfs(v, i, level+1, walked):
                return True
            walked.pop()
    return False


if __name__ == "__main__":
    v = [
        [[], [], [], []],
        [[1], [3], [2], []],
        [[3], [2], [1], [2]],
        [[2], [2], [1], []]
    ]
    for i in v:
        if search_room(i):
            print("true")
        else:
            print("false")