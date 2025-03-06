import pytest
from calculadora import Calculadora

@pytest.mark.integracao
def test_operacoes_basicas():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5
    assert calc.subtrair(5, 3) == 2
    assert calc.multiplicar(3, 4) == 12
    assert calc.dividir(8, 2) == 4
