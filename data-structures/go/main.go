package main

import (
	"fmt"
	"sync"
	"time"
)

type IWorkload interface {
	Process()
}

type IProducer interface {
	Produce() IWorkload
}

var TimeoutErr = fmt.Errorf("timeout")

func Question1(workload IWorkload) (err error) {
	c := make(chan int)
	go func() {
		time.Sleep(5 * time.Second)
		c <- -1 // timeout
	}()

	go func() {
		workload.Process()
		c <- 1 // success
	}()
	v := <-c
	if v == -1 {
		return TimeoutErr
	}
	return nil
}

func Question2(producer IProducer) {
	var wg sync.WaitGroup
	ch := make(chan IWorkload, 1<<8)
	// 一个生产者,Produce()不一定是线程安全的
	wg.Add(1)
	go func(wg *sync.WaitGroup) {
		defer wg.Done()
		for {
			w := producer.Produce()
			if w == nil {
				close(ch)
				return
			}
			ch <- w
		}
	}(&wg)
	// 并发5个消费者
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for w := range ch {
				w.Process()
			}

		}(&wg)
	}
	wg.Wait()

}
