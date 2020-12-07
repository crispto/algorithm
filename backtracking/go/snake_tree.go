package main

import "fmt"

type Node struct {
	Value int
	Left  *Node
	Right *Node
}

func SnakeTree(root *Node) {
	if root == nil {
		return
	}
	ret := make([][]int, 0)
	dq := make([]*Node, 0)
	dq = append(dq, root)
	end := root
	dqEnd := root
	line := make([]int, 0)
	for {
		if len(dq) == 0 {
			break
		}
		cur := dq[0]
		line = append(line, cur.Value)
		dq = dq[1:]
		if cur.Left != nil {
			dq = append(dq, cur.Left)
			dqEnd = cur.Left
		}
		if cur.Right != nil {
			dq = append(dq, cur.Right)
			dqEnd = cur.Right
		}
		if cur == end {
			end = dqEnd
			c := make([]int, len(line))
			copy(c, line)
			ret = append(ret, c)
			line = line[:0]
		}
	}
	for i, v := range ret {
		if i%2 == 1 {
			for j := len(v) - 1; j >= 0; j-- {
				fmt.Printf("%d\t", v[j])
			}
		} else {
			for j := 0; j < len(v); j++ {
				fmt.Printf("%d\t", v[j])
			}
		}
		print("\n")

	}

}
