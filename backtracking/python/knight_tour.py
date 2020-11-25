import sys
# n 为棋盘宽度，国际象棋中的骑士（也就是马） 满足一下两个条件为一个解
# 1 能遍历整个棋盘
# 2 最后能回到起点


def knight_tour(n: int) -> list[list[int]]:
    chess = [[0 for x in range(n)] for y in range(n)]
    for i in range((n+1)//2):
        for j in range((n+1)//2):
            chess[i][j] = 1
            if kinght_tour_help(chess, [i, j], 1,  (i, j)):
                return chess
            chess[i][j] = 0
    return []


def kinght_tour_help(chess: list[list[int]], current_pos: list[int], current_level: int, origin_pos: tuple[int]) -> bool:
    # print("{}".format(chess))
    if current_level == len(chess) * len(chess):
        if current_pos == list(origin_pos):
            return True
        return can_access(current_pos, origin_pos)

    for next in valid_pos(chess, current_pos):
        chess[next[0]][next[1]] = current_level+1
        if kinght_tour_help(chess, next, current_level+1, origin_pos):
            return True
        chess[next[0]][next[1]] = 0
    return False


def can_access(current_pos: list[int], target_pos: list[int]) -> bool:
    """
    骑士是否能到达该点
    """
    ver = [x-y for (x, y) in zip(target_pos, current_pos)]
    return ver in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


def valid_pos(chess: list[list[int]], current_pos: list[int]) -> list[list[int]]:
    """
    返回棋盘上所有能走的点，1.尚未走过， 2.可以达到
    """
    vers = [[1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1]]
    ret = []
    for ver in vers:
        next = [x + y for (x, y) in zip(ver, current_pos)]
        if 0 <= next[0] < len(chess) and 0 <= next[1] < len(chess) and chess[next[0]][next[1]] == 0:
            ret.append(next)
    return ret


if __name__ == "__main__":
    # graph = [[0 for i in range(8)] for j in range(8)]
    # current_pos = [4, 4]
    # print(valid_pos(graph, current_pos))
    s = sys.argv[1]
    w = int(s)
    print(knight_tour(w))
