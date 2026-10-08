import unittest

from university_rating.calculations import calculate_average, determine_status, letter_grade
from university_rating.rating import build_rating
from university_rating.validation import validate_scores


class RatingTests(unittest.TestCase):
    def test_empty_average(self):
        self.assertIsNone(calculate_average([]))

    def test_status_boundary(self):
        self.assertEqual(determine_status(49.99), "не допущен")
        self.assertEqual(determine_status(50), "допущен")

    def test_letter_grade(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(40), "F")

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_scores([80, 101])

    def test_source_is_not_changed(self):
        students = [{"id": 1, "name": "Test", "scores": [70, 80]}]
        before = [{"id": 1, "name": "Test", "scores": [70, 80]}]
        build_rating(students)
        self.assertEqual(students, before)

    def test_empty_scores(self):
        result = build_rating([{"id": 1, "name": "Mira", "scores": []}])
        self.assertEqual(result[0]["grade"], "—")


if __name__ == "__main__":
    unittest.main()
