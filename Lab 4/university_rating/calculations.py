PASSING_AVERAGE = 50


def calculate_average(scores):
    """Возвращает среднее или None для пустого списка."""
    return sum(scores) / len(scores) if scores else None


def determine_status(average):
    """Возвращает статус студента."""
    if average is None:
        return "нет данных"
    return "допущен" if average >= PASSING_AVERAGE else "не допущен"


def letter_grade(average):
    """Возвращает буквенную оценку A, B, C, D или F."""
    if average is None:
        return "—"
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"
