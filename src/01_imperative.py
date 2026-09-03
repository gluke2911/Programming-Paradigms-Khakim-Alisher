numbers = [4, 7, 2, 9, 12, 5, 8, 3]

total = 0
even_numbers = []
squares = []
iterations = 0

for number in numbers:
    iterations += 1
    if number % 2 == 0:
        even_numbers.append(number)
        squares.append(number ** 2)
        total += number ** 2

print("Чётные числа:", even_numbers)
print("Квадраты выбранных чисел:", squares)
print("Сумма квадратов:", total)
print("Количество итераций:", iterations)
print("Изменяемое состояние: total, even_numbers, squares, iterations")
