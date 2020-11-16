package main

import (
	"fmt"
)

func generateAllCombinations(n, k int) [][]int {
	if n < k {
		panic("非法参数")
	}
	result := make([][]int, 0)
	tmp := make([]int, 0, k)
	generateAllCombinationsDFS(1, n, k, tmp, &result)
	return result
}

func generateAllCombinations2(n, k int) [][]int {
	if n < k {
		panic("非法参数")
	}
	result := make([][]int, 0)
	tmp := make([]int, 0, k)
	generateAllCombinationsDFS2(1, n, k, tmp, &result)
	return result
}

func generateAllCombinationsDFS(start, n, k int, tmp []int, result *[][]int) {
	if len(tmp) == k {
		v := make([]int, k)
		copy(v, tmp)
		*result = append(*result, v)
		return
	}
	for i := start; i <= n-(k-len(tmp))+1; i++ {
		tmp = append(tmp, i)
		generateAllCombinationsDFS(i+1, n, k, tmp, result)
		tmp = tmp[:len(tmp)-1]
	}

}

func generateAllCombinationsDFS2(start, n, k int, tmp []int, result *[][]int) {
	if k == 0 {
		v := make([]int, len(tmp))
		copy(v, tmp)
		*result = append(*result, v)
		return
	}
	for i := start; i <= n-k+1; i++ {
		tmp = append(tmp, i)
		generateAllCombinationsDFS2(i+1, n, k-1, tmp, result)
		tmp = tmp[:len(tmp)-1]
	}

}
func main() {
	q := generateAllCombinations2(5, 3)
	for i := range q {
		fmt.Println(q[i])
	}
}
