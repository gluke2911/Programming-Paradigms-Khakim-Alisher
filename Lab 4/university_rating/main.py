from .rating import build_rating
from .report import format_rating


def load_demo_data():
    """Возвращает демонстрационные данные."""
    return [
        {"id": 101, "name": "Amina", "scores": [88, 92, 79]},
        {"id": 102, "name": "Dias", "scores": [45, 52, 48]},
        {"id": 103, "name": "Mira", "scores": []},
        {"id": 104, "name": "Arman", "scores": [95, 91, 96]},
    ]


def main():
    """Запускает демонстрацию пакета."""
    rating = build_rating(load_demo_data())
    print(format_rating(rating))


if __name__ == "__main__":
    main()
