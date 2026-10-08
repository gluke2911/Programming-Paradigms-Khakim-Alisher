"""Лабораторная работа №3. Вариант 1 — посещаемость."""


def validate_mark(mark):
    """Проверяет отметку посещаемости: 0 или 1."""
    if isinstance(mark, bool) or not isinstance(mark, int):
        raise TypeError("Отметка должна быть целым числом")
    if mark not in (0, 1):
        raise ValueError("Отметка должна быть 0 или 1")
    return mark


def attendance_rate(marks):
    """Возвращает процент посещаемости или None для пустого списка."""
    checked = [validate_mark(mark) for mark in marks]
    if not checked:
        return None
    return sum(checked) / len(checked) * 100


def determine_access(rate, threshold=75):
    """Определяет допуск по проценту посещаемости."""
    if not 0 <= threshold <= 100:
        raise ValueError("Порог должен быть от 0 до 100")
    if rate is None:
        return "нет данных"
    return "допущен" if rate >= threshold else "не допущен"


def summarize_student(student, threshold=75):
    """Формирует новую сводную запись студента."""
    student_id = student.get("id")
    name = student.get("name")
    marks = student.get("marks", [])

    if isinstance(student_id, bool) or not isinstance(student_id, int):
        raise TypeError("ID должен быть целым числом")
    if student_id <= 0 or not isinstance(name, str) or not name.strip():
        raise ValueError("Некорректные данные студента")

    rate = attendance_rate(marks)
    return {
        "id": student_id,
        "name": name.strip(),
        "rate": rate,
        "status": determine_access(rate, threshold),
    }


def filter_by_threshold(rows, threshold=75):
    """Возвращает студентов, достигших порога посещаемости."""
    if not 0 <= threshold <= 100:
        raise ValueError("Порог должен быть от 0 до 100")
    return [row for row in rows if row["rate"] is not None and row["rate"] >= threshold]


def build_rating(students, threshold=75):
    """Формирует рейтинг по посещаемости без изменения исходных данных."""
    rows = [summarize_student(student, threshold) for student in students]
    return sorted(
        rows,
        key=lambda row: (row["rate"] is not None, row["rate"] or 0),
        reverse=True,
    )


def format_report(rating):
    """Возвращает текстовый отчёт без печати."""
    lines = ["Рейтинг посещаемости"]
    for position, row in enumerate(rating, 1):
        rate = "—" if row["rate"] is None else f"{row['rate']:.2f}%"
        lines.append(f"{position}. {row['name']}: {rate}; {row['status']}")
    return "\n".join(lines)


def main():
    students = [
        {"id": 101, "name": "Amina", "marks": [1, 1, 1, 0, 1]},
        {"id": 102, "name": "Dias", "marks": [1, 0, 0, 1, 0]},
        {"id": 103, "name": "Mira", "marks": []},
        {"id": 104, "name": "Arman", "marks": [1, 1, 1, 1, 1]},
    ]

    rating = build_rating(students)
    print(format_report(rating))
    print("\nДопущены:")
    for student in filter_by_threshold(rating):
        print(f"- {student['name']}")


if __name__ == "__main__":
    main()
