package main

import (
	"fmt"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"
)

const (
	Concurrent int = 100
)

func main() {
	var ch = make(chan func(), 10<<10)
	var done = make(chan os.Signal)
	signal.Notify(done, syscall.SIGKILL)
	go producer(done, ch)
	var wg sync.WaitGroup
	for i := 0; i < Concurrent; i++ {
		wg.Add(1)
		go consumer(&wg, ch)
	}
	wg.Wait()
}

func consumer(wg *sync.WaitGroup, ch chan func()) {
	defer wg.Done()
	for task := range ch {
		task()
	}
}

func producer(done chan os.Signal, ch chan func()) {
	ticker := time.NewTicker(time.Second)

	defer func() {
		ticker.Stop()
		close(ch)
	}()

	for {
		select {
		case <-done:
			return
		case <-ticker.C:
			ch <- func() {
				fmt.Printf("now: %v\n", time.Now())
			}
		}
	}

}

func printTime() func() {
	now := time.Now()
	return func() {
		fmt.Printf("now: %v\n", now)
	}
}
