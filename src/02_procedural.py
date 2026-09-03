from typing import Iterable

def is_even(number: int) -> bool:
    return number % 2 == 0

def square(number: int) -> int:
    return number ** 2

def get_even_numbers(values: Iterable[int]) -> list[int]:
    return [number for number in values if is_even(number)]

def sum_even_squares(values: Iterable[int]) -> int:
    total = 0
    for number in values:
        if is_even(number):
            total += square(number)
    return total

numbers = [4, 7, 2, 9, 12, 5, 8, 3]

print("is_even(4):", is_even(4))
print("square(12):", square(12))
print("Чётные числа:", get_even_numbers(numbers))
print("Сумма квадратов:", sum_even_squares(numbers))
