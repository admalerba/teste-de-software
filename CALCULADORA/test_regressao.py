import pytest
from calculadora import Calculadora

def test_somar_regressao():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5
    assert calc.somar(-1, -1) == -2  # Testando caso especial
