import streamlit as st
from calculadora import Calculadora

# Instanciando a Calculadora
calc = Calculadora()

# Título da aplicação
st.title("Calculadora Web com Streamlit")

# Escolhendo a operação
operacao = st.selectbox("Escolha a operação", ["Somar", "Subtrair", "Multiplicar", "Dividir", "Potência", "Raiz", "Porcentagem"])

# Inputs para as operações
num1 = st.number_input("Digite o primeiro número", value=0.0)
if operacao != "Raiz":
    num2 = st.number_input("Digite o segundo número", value=0.0)

# Realizando a operação com base na escolha
if st.button("Calcular"):
    if operacao == "Somar":
        resultado = calc.somar(num1, num2)
    elif operacao == "Subtrair":
        resultado = calc.subtrair(num1, num2)
    elif operacao == "Multiplicar":
        resultado = calc.multiplicar(num1, num2)
    elif operacao == "Dividir":
        if num2 != 0:
            resultado = calc.dividir(num1, num2)
        else:
            resultado = "Erro: Divisão por zero"
    elif operacao == "Potência":
        resultado = calc.potencia(num1, num2)
    elif operacao == "Raiz":
        resultado = calc.raiz(num1)
    elif operacao == "Porcentagem":
        resultado = calc.porcentagem(num1, num2)
    
    # Exibindo o resultado
    st.write(f"Resultado: {resultado}")

