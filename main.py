"""Простой калькулятор: сложение, вычитание, умножение.

Файл создан в рамках задания 1553 по работе с Git и PEP 8.
"""

APP_NAME = "MyCalculator"
VERSION = "1.1"


def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b


def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def main():
    """Демонстрирует работу функций калькулятора."""
    print(APP_NAME + " v" + VERSION)
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))


if __name__ == "__main__":
    main()
