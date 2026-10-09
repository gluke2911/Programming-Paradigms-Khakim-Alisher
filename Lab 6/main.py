"""Демонстрация взаимозаменяемых способов формирования отчёта."""

from reporting import HtmlRenderer, MemoryRenderer, ReportService, TextRenderer


def main() -> None:
    """Создать отчёты с двумя форматами и тестовым хранилищем."""
    records = [
        "Студент: Алишер Хаким",
        "Группа: ТИИ 25-21",
        "Результат: лабораторная работа выполнена",
    ]

    text_service = ReportService(TextRenderer())
    print("Текстовый отчёт:")
    print(text_service.create_report("Отчёт по лабораторной работе", records))

    html_service = ReportService(HtmlRenderer())
    html_result = html_service.create_report("Отчёт по лабораторной работе", records)
    print("\nHTML-отчёт сформирован.")
    print(html_result[:100] + "...")

    memory_renderer = MemoryRenderer()
    memory_service = ReportService(memory_renderer)
    memory_service.create_report("Проверка памяти", ["Тестовая запись"])
    print(f"\nMemoryRenderer сохранил результат: {memory_renderer.last_result!r}")


if __name__ == "__main__":
    main()
