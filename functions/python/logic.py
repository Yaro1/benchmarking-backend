def compute(numbers: list[int]):
    """Computes the sum of numbers."""
    return sum(numbers)


def multiply(numbers: list[int]):
    """Multiplies all numbers together."""
    result = 1
    for num in numbers:
        result *= num
    return result


def average(numbers: list[int]):
    """Calculates the average of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0
