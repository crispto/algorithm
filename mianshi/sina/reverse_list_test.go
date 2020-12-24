package main

import "testing"

func TestSort1(t *testing.T) {
	v := []int{2, 5, 4, 7, 8}
	var vh *ListNode
	for i := 0; i < len(v); i++ {
		tmp := &ListNode{
			Val:  v[len(v)-1-i],
			Next: vh,
		}
		vh = tmp
	}
	var prev *ListNode
	cur := vh
	for cur != nil {
		cur.Prev = prev
		prev = cur
		cur = cur.Next
	}

	vh.Show()
	Reverse1(vh)
	vh.Show()
	// new_vh := SortList(vh)
	// new_vh.Show()
}
