package main

import (
	"testing"
	"time"

	"gotest.tools/assert"
)

type work1 struct{}

func (w *work1) Process() {
	time.Sleep(6 * time.Second)
}

func (w *work2) Process() {
	time.Sleep(3 * time.Second)
}

type work2 struct{}

func TestQuestion(t *testing.T) {
	w1 := new(work1)
	err := Question1(w1)
	assert.Equal(t, err, TimeoutErr)

	w2 := new(work2)
	err = Question1(w2)
	assert.Equal(t, err, nil)

}

type producer1 struct{}

func TestQuestion2(t *testing.T) {

}
