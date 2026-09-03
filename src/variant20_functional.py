from functools import reduce

numbers = [2, 3, 4, 5, 8, 11, 13, 15, 17, 20, 23, 25]

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))

prime_numbers = list(filter(is_prime, numbers))
count = reduce(lambda total, _: total + 1, prime_numbers, 0)

print("Простые числа:", prime_numbers)
print("Количество простых чисел:", count)
print("Изменяемый накопитель цикла не используется.")
