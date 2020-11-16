package main

import (
	"fmt"
	"testing"
)

func BenchmarkUseLen(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		generateAllCombinations(10, 3)
	}
}

func BenchmarkUseLevel(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		generateAllCombinations2(10, 3)
	}
}

func TestSlice(t *testing.T) {
	v := []int{1, 2, 3}
	u := v[:]
	u[0] = 4
	fmt.Printf("v: %v\n", v)
	fmt.Printf("u: %v\n", u)
}
