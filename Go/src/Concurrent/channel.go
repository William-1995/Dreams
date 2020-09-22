package main

import "fmt"

/*
cooperate 合作
routine
co-routine
 */
func main()  {
	//done:= make(chan int,1)
	//
	//go func() {
	//	fmt.Println("Hello, world")
	//	done <- 1 // send
	//}()
	//
	//<- done // receive

	done := make(chan int , 10)
	for i:= 0; i < cap(done); i++ {
		go func(no int) {
			fmt.Println(" Hello , world")
			done <- no // send to main
		}(i)
	}

	for i := 0; i < cap(done); i++ {
		value := <- done
		fmt.Println("I amd from child go-routine", value)
	}

}
