from collections.abc import Iterable

class NumberCollection:
    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = list(numbers)

    def get_even_numbers(self) -> list[int]:
        return [number for number in self._numbers if number % 2 == 0]

    def sum_even_squares(self) -> int:
        total = 0
        for number in self._numbers:
            if number % 2 == 0:
                total += number ** 2
        return total

    def count_even_numbers(self) -> int:
        return len(self.get_even_numbers())

    def find_maximum(self) -> int:
        return max(self._numbers)

    def calculate_average(self) -> float:
        return sum(self._numbers) / len(self._numbers)

numbers = [4, 7, 2, 9, 12, 5, 8, 3]
collection = NumberCollection(numbers)
second_collection = NumberCollection([10, 3, 6, 1, 14])

print("Первый объект:")
print("Чётные числа:", collection.get_even_numbers())
print("Сумма квадратов:", collection.sum_even_squares())
print("Количество чётных:", collection.count_even_numbers())
print("Максимум:", collection.find_maximum())
print("Среднее:", collection.calculate_average())

print("\nВторой объект:")
print("Чётные числа:", second_collection.get_even_numbers())
print("Сумма квадратов:", second_collection.sum_even_squares())

print("\nНазначение self._numbers: хранит состояние объекта — копию исходного набора чисел.")
