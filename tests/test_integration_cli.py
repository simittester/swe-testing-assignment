from quick_calc.core import Calculator
from quick_calc.cli import QuickCalcCLI


def test_full_user_flow_addition():
    app = QuickCalcCLI(Calculator())
    app.press("5")
    app.press("+")
    app.press("3")
    assert app.press("=") == "8"


def test_clear_after_calculation_resets_to_zero():
    app = QuickCalcCLI(Calculator())
    app.press("9")
    app.press("*")
    app.press("2")
    assert app.press("=") == "18"
    assert app.press("C") == "0"


def test_division_by_zero_shows_error():
    app = QuickCalcCLI(Calculator())
    app.press("7")
    app.press("/")
    app.press("0")
    assert app.press("=") == "Error"