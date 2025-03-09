package functions

func Compute(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

func Multiply(numbers []int) int {
	result := 1
	for _, num := range numbers {
		result *= num
	}
	return result
}

func Average(numbers []int) float64 {
	if len(numbers) == 0 {
		return 0
	}
	sum := Compute(numbers)
	return float64(sum) / float64(len(numbers))
}
