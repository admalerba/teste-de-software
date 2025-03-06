import pytest
from calculadora import Calculadora

def test_somar_aceitacao():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5  # Validado pelo usuário final
