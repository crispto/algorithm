package main

import "fmt"

type ListNode struct {
	Val  int
	Prev *ListNode
	Next *ListNode
}

func (l *ListNode) Show() {
	h := l
	for h != nil {
		fmt.Printf("%d\t", h.Val)
		h = h.Next
	}
	fmt.Println()
}

func Reverse1(l *ListNode) *ListNode {
	// 直接交换值
	if l == nil || l.Next == nil {
		return l
	}
	head := l
	tail := l
	for tail.Next != nil {
		tail = tail.Next
	}
	for head != tail && head.Prev != tail {
		head.Val, tail.Val = tail.Val, head.Val
		head = head.Next
		tail = tail.Prev
	}
	return l
}

func SortList(l *ListNode) *ListNode {
	// 选择排序
	if l == nil || l.Next == nil {
		return l
	}
	tail := l
	for tail != nil {
		maxNode := tail
		cur := tail
		for cur != nil {
			if cur.Val < maxNode.Val {
				maxNode = cur
			}
			cur = cur.Next
		}
		tail.Val, maxNode.Val = maxNode.Val, tail.Val
		tail = tail.Next
	}
	return l
}
