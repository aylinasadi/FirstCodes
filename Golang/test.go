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

	if y < 3 {
		fmt.Println("y is less than 3")
	} else if y > 3 && y < 10 {
		fmt.Println("y is between 3 and 10")
	} else {
		fmt.Println("y is greater than 10")
	}

	switch a {
	case 53:
		fmt.Println("a is 53")
	case 54:
		fmt.Println("a is 54")
	default:
		fmt.Println("a is not 53 or 54")
	}

	switch {
	case y >= 25:
		fmt.Println("y is greater than or equal to 25")
	case y > 15:
		fmt.Println("y is greater than 15")
	default:
		fmt.Println("y is less than or equal to 15")
	}

	switch {
	case y > 10:
		fmt.Println("y is greater than 10")
		fallthrough
	case y > 18:
		fmt.Println("y is greater than 18")
		fallthrough
	case y > 19:
		fmt.Println("y is greater than 19")
	default:
		fmt.Println("y is less than or equal to 10")
	}

	switch x {
	case "hello", "hi", "hey":
		fmt.Println("x is a greeting")
	default:
		fmt.Println("x is not a greeting")
	}

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	for y > 15 {
		fmt.Print("ha")
		y--
	}
	fmt.Println()

	fmt.Println(string(x[0]))
}
