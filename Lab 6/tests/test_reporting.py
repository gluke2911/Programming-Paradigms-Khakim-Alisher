"""Автоматические тесты генераторов отчёта."""

import unittest

from reporting import HtmlRenderer, MemoryRenderer, ReportService, TextRenderer


class ReportServiceTests(unittest.TestCase):
    """Проверки сервиса и взаимозаменяемости компонентов."""

    def test_text_renderer_formats_report(self) -> None:
        result = ReportService(TextRenderer()).create_report(
            "Итоги", ["Первая запись", "Вторая запись"]
        )
        self.assertIn("Итоги", result)
        self.assertIn("Первая запись", result)

    def test_html_renderer_formats_report(self) -> None:
        result = ReportService(HtmlRenderer()).create_report(
            "Итоги", ["Успешно"]
        )
        self.assertIn("<h1>Итоги</h1>", result)
        self.assertIn("<li>Успешно</li>", result)

    def test_html_renderer_escapes_markup(self) -> None:
        result = ReportService(HtmlRenderer()).create_report(
            "Итоги", ["<script>alert(1)</script>"]
        )
        self.assertNotIn("<script>", result)
        self.assertIn("&lt;script&gt;", result)

    def test_memory_renderer_stores_result(self) -> None:
        renderer = MemoryRenderer()
        service = ReportService(renderer)
        service.create_report("Память", ["Запись"])
        self.assertEqual(renderer.render_count, 1)
        self.assertIn("Запись", renderer.last_result or "")

    def test_renderer_can_be_replaced_without_changing_service(self) -> None:
        records = ["Одна запись"]
        text_result = ReportService(TextRenderer()).create_report("Тест", records)
        html_result = ReportService(HtmlRenderer()).create_report("Тест", records)
        self.assertIn("Тест", text_result)
        self.assertIn("<h1>Тест</h1>", html_result)
        self.assertNotEqual(text_result, html_result)

    def test_empty_title_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ReportService(TextRenderer()).create_report(" ", ["Запись"])

    def test_empty_records_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ReportService(TextRenderer()).create_report("Заголовок", [])

    def test_invalid_renderer_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            ReportService(object())  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
