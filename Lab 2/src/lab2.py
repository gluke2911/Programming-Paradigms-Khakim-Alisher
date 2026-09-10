# Лабораторная работа № 2
# Императивная парадигма: состояние, присваивание и управление выполнением
# Студент: Хаким Алишер, группа ТИИ 25-21
# Индивидуальный вариант №11: Факториал

def task1_state():
    print("=== Задание 1. Исследование изменения состояния ===")
    x = 10
    print(f"1) x = 10      -> x = {x}")
    x = x + 5
    print(f"2) x = x + 5   -> x = {x}")
    x = x * 2
    print(f"3) x = x * 2   -> x = {x}")
    x = x - 8
    print(f"4) x = x - 8   -> x = {x}")
    x = x // 2
    print(f"5) x = x // 2  -> x = {x}")
    print(f"Результат: {x}\n")


def task2_purchase():
    print("=== Задание 2. Расчет стоимости покупки ===")
    price = float(input("Цена одного товара: "))
    quantity = int(input("Количество товаров: "))
    discount_percent = float(input("Процент скидки: "))

    total_without_discount = price * quantity
    discount = total_without_discount * discount_percent / 100
    total_to_pay = total_without_discount - discount

    print(f"Стоимость без скидки: {total_without_discount:.2f}")
    print(f"Размер скидки: {discount:.2f}")
    print(f"К оплате: {total_to_pay:.2f}\n")


def task3_grade():
    print("=== Задание 3. Управление выполнением с помощью условия ===")
    score = int(input("Введите балл от 0 до 100: "))

    if score < 0 or score > 100:
        print("Ошибка: балл должен быть от 0 до 100.")
    elif score >= 90:
        print("Оценка: A")
    elif score >= 75:
        print("Оценка: B")
    elif score >= 50:
        print("Оценка: C")
    else:
        print("Оценка: F")
    print()


def task4_accumulation():
    print("=== Задание 4. Накопление состояния в цикле ===")
    numbers = [12, -5, 8, -3, 21, 0, 14, -7]
    total = 0
    positive_sum = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    print("Итерация | число | total | positive_sum | + | - | 0")
    for index, number in enumerate(numbers, start=1):
        total = total + number
        if number > 0:
            positive_sum = positive_sum + number
            positive_count = positive_count + 1
        elif number < 0:
            negative_count = negative_count + 1
        else:
            zero_count = zero_count + 1
        print(f"{index:8} | {number:5} | {total:5} | {positive_sum:12} | "
              f"{positive_count:1} | {negative_count:1} | {zero_count:1}")

    print(f"Сумма всех чисел: {total}")
    print(f"Сумма положительных чисел: {positive_sum}")
    print(f"Количество положительных: {positive_count}")
    print(f"Количество отрицательных: {negative_count}")
    print(f"Количество нулей: {zero_count}\n")


def task5_maximum():
    print("=== Задание 5. Поиск максимального значения ===")
    scores = [67, 82, 45, 91, 76, 88, 54]
    maximum = scores[0]
    print("score | maximum до | score > maximum | maximum после")
    for score in scores:
        before = maximum
        changed = score > maximum
        if score > maximum:
            maximum = score
        print(f"{score:5} | {before:11} | {str(changed):16} | {maximum:14}")
    print(f"Максимальное значение: {maximum}\n")


def individual_variant_11():
    print("=== Индивидуальное задание. Вариант 11 — Факториал ===")
    n = int(input("Введите неотрицательное целое число n: "))

    if n < 0:
        print("Ошибка: n должно быть неотрицательным.")
        return

    factorial = 1
    counter = 1

    # Накопитель factorial изменяет состояние на каждой итерации.
    while counter <= n:
        factorial = factorial * counter
        print(f"Шаг {counter}: factorial = {factorial}")
        counter = counter + 1

    print(f"{n}! = {factorial}\n")


def comparative_task():
    print("=== Обязательное сравнительное задание ===")
    numbers = [-4, 7, -2, 10, 5, -8]

    # Императивный стиль: состояние total явно изменяется присваиванием.
    total = 0
    for number in numbers:
        if number > 0:
            total = total + number
    print(f"Императивный вариант: {total}")

    # Более декларативная запись.
    declarative_total = sum(number for number in numbers if number > 0)
    print(f"Более декларативный вариант: {declarative_total}\n")


def main():
    task1_state()
    task2_purchase()
    task3_grade()
    task4_accumulation()
    task5_maximum()
    individual_variant_11()
    comparative_task()


if __name__ == "__main__":
    main()
