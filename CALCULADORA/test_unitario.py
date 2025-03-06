import pytest
from calculadora import Calculadora

def test_somar():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5

def test_subtrair():
    calc = Calculadora()
    assert calc.subtrair(5, 3) == 2

def test_multiplicar():     
    calc = Calculadora()
    assert calc.multiplicar(2, 3) == 6    
    assert calc.multiplicar(2, 4) == 8        
    assert calc.multiplicar(2, 5) == 10 
    
def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5    
    assert calc.dividir(10, 5) == 2 

def test_raiz():
    calc = Calculadora()
    assert calc.raiz(4) == 2        
    assert calc.raiz(9) == 3