from typing import Callable

numbers = [4, 7, 2, 9, 12, 5, 8, 3]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
squares = list(map(lambda number: number ** 2, even_numbers))
result = sum(squares)

print("Чётные числа:", even_numbers)
print("Квадраты чётных чисел:", squares)
print("Сумма квадратов:", result)
print("Изменяемые переменные-накопители total нет; вычисление задано цепочкой преобразований.")
