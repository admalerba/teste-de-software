import pytest
import time
from calculadora import Calculadora
from pytest import mark

@mark.desempenho
def test_somar_desempenho():
    calc = Calculadora()
    inicio = time.time()
    for _ in range(1000000):
        calc.somar(2, 3)
    fim = time.time()
    assert (fim - inicio) < 1  # O teste deve executar em menos de 1 segundo
