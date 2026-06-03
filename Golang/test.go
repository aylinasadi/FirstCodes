package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	var x string = "hello"
	var y uint = 20
	var z int = -2000
	a := 54.3567
	b := int(a)
	fmt.Println(x, y, z, a, b)
	fmt.Printf("%T %T", a, b)
	fmt.Println()
	fmt.Printf("the value of a is: %v\n", a)
	fmt.Printf("%b\n", y)
	c := fmt.Sprintf("%.2f", a)
	fmt.Println(c)
	d := x + fmt.Sprint(y)
	fmt.Println(d)
	fmt.Println(math.Min(1, -9))
	fmt.Println(math.Pow(2, 3))
	e := "1234"
	f := "123hi"
	g, err := strconv.Atoi(e)
	h, err := strconv.Atoi(f)
	fmt.Println(g)
	fmt.Println(h, err)

}
