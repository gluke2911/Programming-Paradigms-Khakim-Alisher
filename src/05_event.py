import tkinter as tk

def calculate() -> None:
    try:
        values = [int(value) for value in entry.get().split()]
        even_numbers = [n for n in values if n % 2 == 0]
        squares = [n ** 2 for n in even_numbers]
        result_label.config(
            text=f"Чётные: {even_numbers}\nКвадраты: {squares}\nСумма квадратов: {sum(squares)}"
        )
    except ValueError:
        result_label.config(text="Ошибка: введите только целые числа через пробел.")

def clear_result() -> None:
    entry.delete(0, tk.END)
    result_label.config(text="Результат очищен.")

root = tk.Tk()
root.title("Парадигмы программирования — лабораторная №1")
root.geometry("520x260")

tk.Label(root, text="Введите целые числа через пробел:").pack(pady=(15, 5))
entry = tk.Entry(root, width=55)
entry.pack()
entry.insert(0, "4 7 2 9 12 5 8 3")

tk.Button(root, text="Вычислить", command=calculate).pack(pady=10)
tk.Button(root, text="Очистить", command=clear_result).pack()

result_label = tk.Label(root, text="Нажмите «Вычислить»", justify="left")
result_label.pack(pady=10)

root.mainloop()
