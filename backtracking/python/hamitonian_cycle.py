"""
给一个图和起始节点，判断是否存在哈密顿环，即从该节点出发不重复地经历图中的所有节点并回到起点
"""


def hamitonian_cycle(graph: list[list[int]], start: int) -> list[list[int]]:
    """
    判断方法是， 从初始节点搜索所有相邻节点，并标记为已经过，用回溯递归法遍历整个路径树。
    """
    path = [-1] * (len(graph)+1)
    path[0] = path[-1] = start
    return path if until_hamitonian_cycle(graph, path, 1) else []


def until_hamitonian_cycle(graph: list[list[int]], path: list[int], path_index: int) -> bool:
    if path_index == len(graph):
        return graph[path[path_index-1]][path[-1]] == 1

    for next in range(len(graph)):
        if is_valid(graph, path[path_index-1], next, path):
            path[path_index] = next
            if until_hamitonian_cycle(graph, path, path_index+1):
                return True
            path[path_index] = -1
    return False


def is_valid(graph: list[list[int]], current: int, next: int, path: list[int]) -> bool:
    if graph[current][next] == 0:
        return False
    return not any([x == next for x in path])


if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]]
    for i in range(len(graph)):
        v = hamitonian_cycle(graph, i)
        print("start vertex: {}, cycle {}".format(i, v))
