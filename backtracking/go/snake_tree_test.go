package main

import (
	"testing"
)

func TestSnakeTree(t *testing.T) {
	a := Node{Value: 1}
	b := Node{Value: 3}
	c := Node{Value: 2}
	d := Node{Value: 4}
	e := Node{Value: 5}
	a.Left = &b
	a.Right = &c
	c.Left = &d
	d.Left = &e
	SnakeTree(&a)
}
