from collections.abc import Iterable

class NumberAnalyzer:
    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = list(numbers)

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    def get_prime_numbers(self) -> list[int]:
        return [number for number in self._numbers if self.is_prime(number)]

    def count_prime_numbers(self) -> int:
        return len(self.get_prime_numbers())

    def find_maximum(self) -> int:
        return max(self._numbers)

numbers = [2, 3, 4, 5, 8, 11, 13, 15, 17, 20, 23, 25]
analyzer = NumberAnalyzer(numbers)

print("Простые числа:", analyzer.get_prime_numbers())
print("Количество простых чисел:", analyzer.count_prime_numbers())
print("Максимум:", analyzer.find_maximum())
print("self._numbers хранит состояние объекта — набор чисел для анализа.")
