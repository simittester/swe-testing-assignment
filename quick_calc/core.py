from __future__ import annotations

class Calculator:
    """Core calculation engine (no I/O)."""

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.current: float = 0.0

    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b