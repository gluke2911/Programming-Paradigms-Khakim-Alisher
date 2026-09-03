import tkinter as tk

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))

def calculate() -> None:
    try:
        values = [int(value) for value in entry.get().split()]
        primes = [value for value in values if is_prime(value)]
        result_label.config(text=f"Простые числа: {primes}\nКоличество: {len(primes)}")
    except ValueError:
        result_label.config(text="Ошибка: введите только целые числа через пробел.")

def clear_result() -> None:
    entry.delete(0, tk.END)
    result_label.config(text="Результат очищен.")

root = tk.Tk()
root.title("Индивидуальный вариант 20")
root.geometry("520x250")

tk.Label(root, text="Введите целые числа через пробел:").pack(pady=(15, 5))
entry = tk.Entry(root, width=55)
entry.pack()
entry.insert(0, "2 3 4 5 8 11 13 15 17 20 23 25")

tk.Button(root, text="Подсчитать простые числа", command=calculate).pack(pady=10)
tk.Button(root, text="Очистить", command=clear_result).pack()

result_label = tk.Label(root, text="Нажмите кнопку", justify="left")
result_label.pack(pady=10)

root.mainloop()
