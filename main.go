package main

import "fmt"

func SearchIsland(mesh [][]int) int {
	if len(mesh) == 0 {
		return 0
	}
	var ret int
	for i := range mesh {
		for j := range mesh[i] {
			if mesh[i][j] == 1 {
				// bfs 渲染所有的相邻点
				ret++
				queue := make([][2]int, 0)
				queue = append(queue, [2]int{i, j})
				for len(queue) > 0 {
					cur := queue[0]
					queue = queue[1:]
					x, y := cur[0], cur[1]
					mesh[x][y] = -1 // 记录为已经探索过
					if x-1 >= 0 && mesh[x-1][y] == 1 {
						mesh[x][y] = -1
						queue = append(queue, [2]int{x - 1, y})
					}
					if x+1 < len(mesh) && mesh[x+1][y] == 1 {
						mesh[x][y] = -1
						queue = append(queue, [2]int{x + 1, y})
					}
					if y-1 >= 0 && mesh[x][y-1] == 1 {
						mesh[x][y] = -1
						queue = append(queue, [2]int{x, y - 1})
					}
					if y+1 < len(mesh[0]) && mesh[x][y+1] == 1 {
						mesh[x][y] = -1
						queue = append(queue, [2]int{x, y + 1})
					}
				}

			}
		}
	}
	return ret
}

func main() {
	var v = [][]int{
		{0, 0, 0, 0, 0, 0},
		{0, 0, 1, 1, 1, 0},
		{0, 0, 1, 1, 1, 0},
		{0, 0, 1, 1, 1, 0},
		{0, 0, 0, 0, 0, 0},
	}
	fmt.Printf("%d\n", SearchIsland(v))
}
