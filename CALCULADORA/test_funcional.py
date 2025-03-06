import pytest
from calculadora import Calculadora

def test_calculadora():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5
    assert calc.subtrair(5, 3) == 2
    assert calc.multiplicar(3, 4) == 12
    assert calc.dividir(8, 2) == 4
    assert calc.potencia(2, 3) == 8
    assert calc.raiz(16) == 4
    assert calc.porcentagem(50, 20) == 10
