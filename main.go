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
	// var v = [][]int{
	// 	{0, 0, 0, 0, 0, 0},
	// 	{0, 0, 1, 1, 1, 0},
	// 	{0, 0, 1, 1, 1, 0},
	// 	{0, 0, 1, 1, 1, 0},
	// 	{0, 0, 0, 0, 0, 0},
	// }
	// fmt.Printf("%d\n", SearchIsland(v))
	a := Node{
		Value: "a",
		Children: []*Node{
			&Node{"b", nil},
			&Node{"c", nil},
			&Node{"d", []*Node{&Node{"e", nil}}},
		},
	}
	k := visit(&a, 2)
	for x := range k {
		fmt.Println(k[x].Value)
	}

}

type Node struct {
	Value    string
	Children []*Node
}

func visit(root *Node, n int) []*Node {
	if root == nil {
		return nil
	}
	if n == 0 {
		return []*Node{root}
	}
	queue := make([]*Node, 0)
	queue = append(queue, root)
	end := root
	level := 0
	for {
		if len(queue) == 0 {
			break
		}
		cur := queue[0]
		queue = queue[1:]
		queue = append(queue, cur.Children...) // 子节点入队

		if cur == end {
			end = queue[len(queue)-1]
			level++
		}
		if level == n {
			return queue
		}
	}
	return nil
}
