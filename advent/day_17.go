package main

import (
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"
)

var SMALL_PRG = `Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
`

var LARGE_PRG = `Register A: 64751475
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0
`

var PART2_SMALL_PRG = `Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0`

func run(program []int, A, B, C int) []int {
	var output []int = make([]int, 0)
	ip := 0
	for ip < len(program) {
		instruction := program[ip]
		operand := program[ip+1]
		if operand == 4 {
			operand = A
		} else if operand == 5 {
			operand = B
		} else if operand == 6 {
			operand = C
		}
		ip_plus := 2
		if instruction == 0 {
			A = int(math.Floor(float64(A) / math.Pow(2, float64(operand))))
		} else if instruction == 1 {
			B ^= operand
		} else if instruction == 2 {
			B = operand % 8
		} else if instruction == 3 {
			if A != 0 {
				ip = operand
				ip_plus = 0
			}
		} else if instruction == 4 {
			B ^= C
		} else if instruction == 5 {
			output = append(output, operand%8)
		} else if instruction == 6 {
			B = int(math.Floor(float64(A) / math.Pow(2, float64(operand))))
		} else if instruction == 7 {
			C = int(math.Floor(float64(A) / math.Pow(2, float64(operand))))
		}
		ip += ip_plus
	}
	return output

}

func read_prg(source string) (int, int, int, []int) {
	A, B, C := 0, 0, 0
	prg := make([]int, 0)
	for _, line := range strings.Split(source, "\n") {
		fmt.Println(line)
		if strings.HasPrefix(line, "Register") {
			d := strings.Split(strings.Replace(line, "Register ", "", -1), ":")
			if d[0] == "A" {
				A, _ = strconv.Atoi(strings.Replace(d[1], " ", "", -1))
			} else if d[0] == "B" {
				B, _ = strconv.Atoi(strings.Replace(d[1], " ", "", -1))
			} else if d[0] == "C" {
				C, _ = strconv.Atoi(strings.Replace(d[1], " ", "", -1))
			}
		} else if strings.HasPrefix(line, "Program") {
			for _, x := range strings.Split(strings.Replace(line, "Program: ", "", -1), ",") {
				i_x, _ := strconv.Atoi(x)
				prg = append(prg, i_x)
			}
		}
	}
	return A, B, C, prg
}

func main() {
	a, b, c, prg := read_prg(LARGE_PRG)
	fmt.Println(a, b, c, prg)
	output := run(prg, a, b, c)
	fmt.Println(output)
	/* brute force
	for {
		go func(program []int, A, B, C int) {
			output := run(program, A, B, C)
			if reflect.DeepEqual(program, output) {
				fmt.Println(A)
			}
		}(prg, a, b, c)
		a += 1
		if a%1000000 == 0 {
			fmt.Println(a)
		}
	}*/
	/* https://kyle.so/writing/aoc-2024 */
	a = 0
	for pos := len(prg) - 1; pos >= 0; pos-- {
		a <<= 3
		for !slices.Equal(run(prg, a, b, c), prg[pos:]) {
			a++
		}
	}
	fmt.Println(a)
}
