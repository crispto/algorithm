package main

import (
	"fmt"
	"log"
)

// 哈密顿环问题

var (
	graph = [][]int{
		{0, 1, 0, 1, 0},
		{1, 0, 1, 1, 1},
		{0, 1, 0, 0, 1},
		{1, 1, 0, 0, 1},
		{0, 1, 1, 1, 0}}
)

// IsHamitonianCycle 某一个图从某节点开始是否存在哈密顿环
func IsHamitonianCycle(graph [][]int, currentVertex int) {
	path := make([]int, len(graph)+1)
	for i := 0; i < len(path); i++ {
		path[i] = -1
	}

	path[0] = currentVertex
	path[len(path)-1] = currentVertex
	log.Println(path)
	var result = make([][]int, 0)
	isHamitonianCycleHelp(graph, currentVertex, 0, path, &result)
	if len(result) == 0 {
		fmt.Println("no cycle")
	} else {
		fmt.Printf("path ok")
		for _, v := range result {
			fmt.Printf("%+v\n", v)
		}
	}
}

func isHamitonianCycleHelp(graph [][]int, currentVertex int, pathIndex int, path []int, result *[][]int) {
	if pathIndex == len(graph)-1 {
		if graph[currentVertex][path[len(path)-1]] == 1 {
			var tmp = make([]int, len(path))
			copy(tmp, path)
			*result = append(*result, tmp)
		}
		return
	}
	for i := 0; i < len(graph); i++ {
		if graph[currentVertex][i] == 1 && notIn(path, i) {
			path[pathIndex+1] = i
			log.Printf("path tree is %v\n", path)
			isHamitonianCycleHelp(graph, i, pathIndex+1, path, result)
			path[pathIndex+1] = -1
		}
	}
}

func notIn(path []int, next int) bool {
	for i := 0; i < len(path); i++ {
		if path[i] == next {
			return false
		}
	}
	return true
}
