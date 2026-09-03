from collections.abc import Iterable

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def get_prime_numbers(values: Iterable[int]) -> list[int]:
    return [number for number in values if is_prime(number)]

def count_prime_numbers(values: Iterable[int]) -> int:
    return len(get_prime_numbers(values))

numbers = [2, 3, 4, 5, 8, 11, 13, 15, 17, 20, 23, 25]

print("is_prime(17):", is_prime(17))
print("is_prime(20):", is_prime(20))
print("Простые числа:", get_prime_numbers(numbers))
print("Количество простых чисел:", count_prime_numbers(numbers))
