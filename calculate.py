
from typing import Literal


def calculate(a: float, b: float, operation: Literal["+", "-", "*", "/"]):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "Ошибка в делении на 0"
        case _:
            return "Неизвестная операция"


print(calculate(1, 2, "+"))
print(calculate(1, 0, "/"))
print(calculate(4, 2, "/"))
