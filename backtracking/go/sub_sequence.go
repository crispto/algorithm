package main

import (
	"fmt"
)

// 获取lists的所有子集
func AllSubSequence(lists []interface{}) {
	tmp := make([]interface{}, 0, len(lists))
	allSubSequenceHelp(0, &tmp, lists)

}

// 这就是一个遍历二叉树的过程
func allSubSequenceHelp(i int, tmp *[]interface{}, lists []interface{}) {
	if i == len(lists) {
		fmt.Printf("%v\n", *tmp)
		return
	}

	allSubSequenceHelp(i+1, tmp, lists)
	*tmp = append(*tmp, lists[i])
	allSubSequenceHelp(i+1, tmp, lists)
	*tmp = (*tmp)[:len(*tmp)-1]
}
