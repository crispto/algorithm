from utils import list_print


def maze(maze: list[list[int]]) -> bool:
    route = [[0 for i in j] for j in maze]
    route[0][0] = 1
    if maze_tree(maze, route, (0, 0)):
        list_print(route)
        return True
    return False


# dfs递归树
def maze_tree(maze: list[list[int]], route: list[list[int]], pos: tuple[int]) -> bool:
    if route[-1][-1] == 1:
        return True
    for next in valid_next(maze, route, pos):
        x, y = next[0], next[1]
        route[x][y] = 1
        if maze_tree(maze, route, next):
            return True
        route[x][y] = 0
    return False


# 有效的下一位，1： 下标不超标， 2：是未经过的路线  3：不是墙
def valid_next(maze: list[list[int]], route: list[list[int]], pos: tuple[int]) -> list[tuple[int]]:
    nexts = (
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    )
    ret = []
    for n in nexts:
        x, y = pos[0] + n[0], pos[1] + n[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze) and route[x][y] == 0 and maze[x][y] == 0:
            ret.append((x, y))
    return ret


def my_max(a, b):
    return a if a > b else b


if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 1],
             [0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0],
             [1, 0, 0, 1, 0]]
    if maze(graph):
        print(True)
    else:
        print(False)
