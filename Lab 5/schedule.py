"""Модель занятий и расписания аудиторий."""

from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class Lesson:
    """Неизменяемое занятие с аудиторией и временным интервалом."""

    title: str
    classroom: str
    start: time
    end: time

    def __post_init__(self) -> None:
        """Проверить инварианты занятия после создания объекта."""
        if not self.title.strip():
            raise ValueError("Название занятия не может быть пустым.")
        if not self.classroom.strip():
            raise ValueError("Аудитория не может быть пустой.")
        if not isinstance(self.start, time) or not isinstance(self.end, time):
            raise TypeError("Время начала и окончания должно иметь тип datetime.time.")
        if self.start >= self.end:
            raise ValueError("Время начала должно быть раньше времени окончания.")


class ClassroomSchedule:
    """Управляет занятиями и предотвращает пересечения в одной аудитории."""

    def __init__(self) -> None:
        """Создать пустое расписание."""
        self._lessons: list[Lesson] = []

    @property
    def lessons(self) -> tuple[Lesson, ...]:
        """Вернуть неизменяемое представление списка занятий."""
        return tuple(self._lessons)

    @staticmethod
    def _overlaps(first: Lesson, second: Lesson) -> bool:
        """Определить, пересекаются ли два временных интервала."""
        return first.start < second.end and second.start < first.end

    def add_lesson(self, lesson: Lesson) -> None:
        """Добавить занятие, если аудитория свободна в указанный интервал."""
        if not isinstance(lesson, Lesson):
            raise TypeError("Можно добавлять только объекты Lesson.")

        for existing in self._lessons:
            same_classroom = existing.classroom.casefold() == lesson.classroom.casefold()
            if same_classroom and self._overlaps(existing, lesson):
                raise ValueError(
                    f"Аудитория {lesson.classroom} уже занята в это время."
                )

        # Состояние меняется только после прохождения всех проверок.
        self._lessons.append(lesson)

    def find_by_classroom(self, classroom: str) -> tuple[Lesson, ...]:
        """Найти занятия в указанной аудитории без учёта регистра."""
        if not classroom.strip():
            raise ValueError("Название аудитории не может быть пустым.")
        return tuple(
            lesson
            for lesson in self._lessons
            if lesson.classroom.casefold() == classroom.casefold()
        )
