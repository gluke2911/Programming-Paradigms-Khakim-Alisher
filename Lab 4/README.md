# Лабораторная работа №4 — Структурное и модульное программирование

**Вариант 1 — Буквенная оценка A, B, C, D, F**

## Структура

```text
lab4_modular_letter_grades/
├── university_rating/
│   ├── __init__.py
│   ├── validation.py
│   ├── calculations.py
│   ├── rating.py
│   ├── report.py
│   └── main.py
└── tests/
    └── test_rating.py
```

## Запуск из корня проекта

```bash
python -m university_rating.main
```

## Тесты

```bash
python -m unittest discover -s tests -v
```
