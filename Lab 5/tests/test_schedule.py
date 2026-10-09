"""Автоматические тесты для расписания аудиторий."""

import unittest
from datetime import time

from schedule import ClassroomSchedule, Lesson


class LessonTests(unittest.TestCase):
    """Проверки инвариантов класса Lesson."""

    def test_lesson_can_be_created(self) -> None:
        lesson = Lesson("Математика", "А-101", time(9), time(10))
        self.assertEqual(lesson.title, "Математика")

    def test_empty_title_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Lesson(" ", "А-101", time(9), time(10))

    def test_end_must_be_after_start(self) -> None:
        with self.assertRaises(ValueError):
            Lesson("Математика", "А-101", time(10), time(10))


class ClassroomScheduleTests(unittest.TestCase):
    """Проверки добавления занятий и защиты от конфликтов."""

    def setUp(self) -> None:
        self.schedule = ClassroomSchedule()
        self.schedule.add_lesson(
            Lesson("Математика", "А-101", time(9), time(10))
        )

    def test_adjacent_lessons_are_allowed(self) -> None:
        self.schedule.add_lesson(
            Lesson("Физика", "А-101", time(10), time(11))
        )
        self.assertEqual(len(self.schedule.lessons), 2)

    def test_overlapping_lessons_in_same_room_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.schedule.add_lesson(
                Lesson("Физика", "А-101", time(9, 30), time(10, 30))
            )
        self.assertEqual(len(self.schedule.lessons), 1)

    def test_overlapping_lessons_in_different_rooms_are_allowed(self) -> None:
        self.schedule.add_lesson(
            Lesson("Физика", "Б-204", time(9, 30), time(10, 30))
        )
        self.assertEqual(len(self.schedule.lessons), 2)

    def test_lessons_property_does_not_expose_mutable_list(self) -> None:
        lessons = self.schedule.lessons
        self.assertIsInstance(lessons, tuple)
        with self.assertRaises(AttributeError):
            lessons.append(Lesson("Химия", "В-3", time(11), time(12)))  # type: ignore[attr-defined]

    def test_wrong_object_type_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            self.schedule.add_lesson("не занятие")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
