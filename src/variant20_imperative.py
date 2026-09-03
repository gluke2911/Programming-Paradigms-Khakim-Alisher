# Индивидуальный вариант 20: подсчитать количество простых чисел.
numbers = [2, 3, 4, 5, 8, 11, 13, 15, 17, 20, 23, 25]

prime_numbers = []
count = 0
iterations = 0

for number in numbers:
    iterations += 1
    if number < 2:
        continue

    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        prime_numbers.append(number)
        count += 1

print("Исходные числа:", numbers)
print("Простые числа:", prime_numbers)
print("Количество простых чисел:", count)
print("Итераций по исходному списку:", iterations)
