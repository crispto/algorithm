package main

import "fmt"

// 着色问题，使用有限个颜色对一副图进行着色，使相邻的节点不能有相同的颜色
// 策略，采用回溯递归，深度优先搜索到合适的渲染模式

//Color 图如果成功返回节点颜色，失败返回空数组
func Color(graph [][]int, maxColor int) []int {
	currentColor := make([]int, len(graph))
	// 因为对称原则，人工赋值，减少一层树，其实也可以不用
	currentColor[0] = 0
	for i := 1; i < len(graph); i++ {
		currentColor[i] = -1
	}
	if ColorHelp(graph, currentColor, 1, maxColor) {
		return currentColor
	}
	return make([]int, 0)
}

/* graph 图
currentColor 节点着色状态图，比如[0 1 -1 -1 -1], 进行到了index = 2的节点，前两个已经着色
level 当前正要着色的节点，也是在 currentColor 的下标
maxColor 总的颜色数目
*/

func ColorHelp(graph [][]int, currentColor []int, level int, maxColor int) bool {
	if level == len(currentColor) {
		return true
	}
	// 对每一种可用的颜色构建结构树的下一层
	for color := 0; color < maxColor; color++ {
		if validColor(graph, currentColor, level, color) {
			currentColor[level] = color
			if ColorHelp(graph, currentColor, level+1, maxColor) {
				return true
			}
			currentColor[level] = -1

		}

	}
	return false
}

// 验证该节点是否能用 color 着色
func validColor(graph [][]int, currentColor []int, level int, color int) bool {
	for i := 0; i < len(graph); i++ {
		// 如果存在和该节点相连，而且已经使用当前颜色
		if graph[i][level] == 1 && currentColor[i] == color {
			return false
		}
	}
	return true

}

func coloring_test() {
	var graph = [][]int{
		{0, 1, 0, 0, 0},
		{1, 0, 1, 1, 1},
		{0, 1, 0, 1, 0},
		{0, 1, 1, 0, 0},
		{0, 1, 0, 0, 0}}
	v := Color(graph, 4)

	fmt.Println(v)

}
