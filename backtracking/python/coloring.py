def coloring(graph: list[list[int]], max_color: int) -> list[int]:
    color_map = [-1] * len(graph)
    return color_map if coloring_help(graph, color_map, 0, max_color) else []


def coloring_help(graph: list[list[int]], color_map: list[int], index: int, max_color: int) -> bool:
    if index == len(graph):
        return True
    for color in range(max_color):
        if is_valid_color(graph, color_map, index, color):
            color_map[index] = color
            if coloring_help(graph, color_map, index+1, max_color):
                return True
            color_map[index] = -1

    return False


def is_valid_color(graph: list[list[int]], color_map: list[int], index: int, color: int):
    return not any(
        neighbour == 1 and color_map[i] == color
        for i, neighbour in enumerate(graph[index])
    )


if __name__ == "__main__":
    graph = [[0, 1, 0, 0, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 1, 0],
             [0, 1, 1, 0, 0],
             [0, 1, 0, 0, 0]]
    print(coloring(graph, 3))
