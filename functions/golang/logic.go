package functions

func Compute(items []int) int {
	sum := 0
	for _, num := range items {
		sum += num
	}
	return sum
}

func Multiply(items []int) int {
	result := 1
	for _, num := range items {
		result *= num
	}
	return result
}

func Average(items []int) float64 {
	if len(items) == 0 {
		return 0
	}
	sum := Compute(items)
	return float64(sum) / float64(len(items))
}
