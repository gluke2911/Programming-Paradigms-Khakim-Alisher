"""Демонстрация расписания занятий в аудиториях."""

from datetime import time

from schedule import ClassroomSchedule, Lesson


def main() -> None:
    """Создать расписание, добавить занятия и вывести результат."""
    schedule = ClassroomSchedule()
    schedule.add_lesson(
        Lesson("Программирование", "А-101", time(9, 0), time(10, 30))
    )
    schedule.add_lesson(
        Lesson("Математика", "А-101", time(10, 30), time(12, 0))
    )
    schedule.add_lesson(
        Lesson("Физика", "Б-204", time(9, 0), time(10, 0))
    )

    print("Расписание занятий:")
    for lesson in schedule.lessons:
        print(
            f"{lesson.start.strftime('%H:%M')}–"
            f"{lesson.end.strftime('%H:%M')} | "
            f"{lesson.classroom} | {lesson.title}"
        )


if __name__ == "__main__":
    main()
