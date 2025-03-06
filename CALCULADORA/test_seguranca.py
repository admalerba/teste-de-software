import pytest
from calculadora import Calculadora
from pytest import mark

@mark.seguranca
def test_dividir_seguranca():
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.dividir(1, 0)  # Testando divisão por zero
