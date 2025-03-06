import pytest
from calculadora import Calculadora

def test_calculadora_sistema():
    calc = Calculadora()
    resultado = calc.somar(calc.subtrair(10, 2), calc.multiplicar(2, 2))
    assert resultado == 12  # Testando várias operações combinadas
