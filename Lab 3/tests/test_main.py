import unittest

from main import (
    attendance_rate,
    determine_access,
    filter_by_threshold,
    build_rating,
    validate_mark,
)


class AttendanceTests(unittest.TestCase):
    def test_attendance_rate(self):
        self.assertEqual(attendance_rate([1, 1, 0, 1]), 75)

    def test_empty_marks(self):
        self.assertIsNone(attendance_rate([]))

    def test_invalid_mark_type(self):
        with self.assertRaises(TypeError):
            validate_mark("1")

    def test_invalid_mark_value(self):
        with self.assertRaises(ValueError):
            validate_mark(2)

    def test_access_boundary(self):
        self.assertEqual(determine_access(75), "допущен")
        self.assertEqual(determine_access(74.99), "не допущен")

    def test_filter(self):
        rows = [
            {"name": "A", "rate": 80},
            {"name": "B", "rate": 70},
            {"name": "C", "rate": None},
        ]
        self.assertEqual([x["name"] for x in filter_by_threshold(rows)], ["A"])


if __name__ == "__main__":
    unittest.main()
