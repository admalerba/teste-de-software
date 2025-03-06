from calculadora import Calculadora
from pytest import mark

@mark.somar
def test_somar():
    calc = Calculadora() 
    assert calc.somar(1, 2) == 3

@mark.subtrair
def test_subtrair():    
    calc = Calculadora()    
    assert calc.subtrair(1, 2) == -1
    
def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(1, 2) == 2
    
def test_dividir():
    calc = Calculadora()
    assert calc.dividir(1, 2) == 0.5

def test_potencia():    
    calc = Calculadora()
    assert calc.potencia(2, 2) == 4    
    assert calc.potencia(2, 3) == 8
    
def test_raiz():    
    calc = Calculadora()
    assert calc.raiz(4) == 2        
    assert calc.raiz(9) == 3
    
def test_porcentagem():    
    calc = Calculadora()
    assert calc.porcentagem(10, 20) == 2        
    assert calc.porcentagem(10, 30) == 3                        
    assert calc.porcentagem(10, 40) == 4