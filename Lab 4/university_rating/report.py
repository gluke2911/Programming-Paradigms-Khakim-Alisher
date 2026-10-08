def format_average(value):
    """Форматирует средний балл."""
    return "—" if value is None else f"{value:.2f}"


def format_rating(rows):
    """Формирует текстовый отчёт."""
    lines = ["Рейтинг группы"]
    for position, row in enumerate(rows, 1):
        average = format_average(row["average"])
        lines.append(
            f"{position}. {row['name']}: {average} — "
            f"{row['grade']} — {row['status']}"
        )
    return "\n".join(lines)
