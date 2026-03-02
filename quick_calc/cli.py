from __future__ import annotations
from dataclasses import dataclass
from quick_calc.core import Calculator


@dataclass
class QuickCalcCLI:
    """
    Minimal state machine for integration testing.
    Simulates button presses.
    """
    calc: Calculator

    def __post_init__(self) -> None:
        self.display = "0"
        self._pending_op = None
        self._lhs = None

    def press(self, token: str) -> str:
        token = token.strip()

        if token.upper() == "C":
            self.calc.clear()
            self.display = "0"
            self._pending_op = None
            self._lhs = None
            return self.display

        if token in {"+", "-", "*", "/"}:
            self._lhs = float(self.display)
            self._pending_op = token
            self.display = "0"
            return self.display

        if token == "=":
            if self._pending_op is None or self._lhs is None:
                return self.display

            rhs = float(self.display)

            try:
                if self._pending_op == "+":
                    result = self.calc.add(self._lhs, rhs)
                elif self._pending_op == "-":
                    result = self.calc.sub(self._lhs, rhs)
                elif self._pending_op == "*":
                    result = self.calc.mul(self._lhs, rhs)
                else:
                    result = self.calc.div(self._lhs, rhs)

                self.display = self._format_number(result)

            except ZeroDivisionError:
                self.display = "Error"

            self._pending_op = None
            self._lhs = None
            return self.display

        # assume number input
        float(token)  # will raise ValueError if invalid
        self.display = token
        return self.display

    @staticmethod
    def _format_number(value: float) -> str:
        if value.is_integer():
            return str(int(value))
        return str(value)