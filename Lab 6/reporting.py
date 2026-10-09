"""Компоненты для формирования и отображения отчётов."""

from abc import ABC, abstractmethod
from html import escape


class Renderer(ABC):
    """Общий интерфейс компонента, который отображает строки отчёта."""

    @abstractmethod
    def render(self, title: str, lines: list[str]) -> str:
        """Преобразовать заголовок и строки отчёта в результат."""


class TextRenderer(Renderer):
    """Формирует обычный текстовый отчёт."""

    def render(self, title: str, lines: list[str]) -> str:
        """Вернуть отчёт в текстовом формате."""
        if not title.strip():
            raise ValueError("Заголовок отчёта не может быть пустым.")
        return "\n".join([title, "=" * len(title), *lines])


class HtmlRenderer(Renderer):
    """Формирует простой HTML-документ."""

    def render(self, title: str, lines: list[str]) -> str:
        """Вернуть отчёт в HTML-формате с экранированием текста."""
        if not title.strip():
            raise ValueError("Заголовок отчёта не может быть пустым.")
        escaped_title = escape(title)
        rendered_lines = "\n".join(f"<li>{escape(line)}</li>" for line in lines)
        return (
            "<!doctype html>\n<html lang=\"ru\">\n<head>\n"
            '<meta charset="utf-8">\n'
            f"<title>{escaped_title}</title>\n"
            "</head>\n<body>\n"
            f"<h1>{escaped_title}</h1>\n<ul>\n{rendered_lines}\n</ul>\n"
            "</body>\n</html>"
        )


class MemoryRenderer(Renderer):
    """Сохраняет последний отчёт в памяти; удобно для тестирования."""

    def __init__(self) -> None:
        """Подготовить пустое хранилище результата."""
        self.last_result: str | None = None
        self.render_count = 0

    def render(self, title: str, lines: list[str]) -> str:
        """Сохранить отчёт в памяти и вернуть его."""
        if not title.strip():
            raise ValueError("Заголовок отчёта не может быть пустым.")
        result = "\n".join([title, *lines])
        self.last_result = result
        self.render_count += 1
        return result


class ReportService:
    """Создаёт данные отчёта и делегирует форматирование Renderer."""

    def __init__(self, renderer: Renderer) -> None:
        """Получить реализацию Renderer через внедрение зависимости."""
        if not isinstance(renderer, Renderer):
            raise TypeError("renderer должен реализовывать интерфейс Renderer.")
        self._renderer = renderer

    def create_report(self, title: str, records: list[str]) -> str:
        """Проверить данные и передать их выбранному компоненту."""
        if not title.strip():
            raise ValueError("Заголовок отчёта не может быть пустым.")
        if not records:
            raise ValueError("Отчёт должен содержать хотя бы одну запись.")
        if any(not isinstance(record, str) or not record.strip() for record in records):
            raise ValueError("Записи отчёта должны быть непустыми строками.")

        # Сервис не выбирает формат самостоятельно — он вызывает общий контракт.
        return self._renderer.render(title, records)
