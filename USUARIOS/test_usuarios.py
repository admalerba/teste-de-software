import os
import pytest
from teste import carregar_usuarios, salvar_usuarios, cadastrar_usuario, autenticar_usuario, USUARIOS_ARQUIVO

def setup_module(module):
    if os.path.exists(USUARIOS_ARQUIVO):
        os.remove(USUARIOS_ARQUIVO)

def teardown_module(module):
    if os.path.exists(USUARIOS_ARQUIVO):
        os.remove(USUARIOS_ARQUIVO)

def test_carregar_usuarios():
    usuarios = carregar_usuarios()
    assert usuarios == {}

def test_salvar_e_carregar_usuarios():
    usuarios = {"usuario1": "senha1"}
    salvar_usuarios(usuarios)
    carregados = carregar_usuarios()
    assert carregados == usuarios

def test_cadastrar_usuario():
    assert cadastrar_usuario("usuario2", "senha2") == True
    assert cadastrar_usuario("usuario2", "senha2") == False

def test_autenticar_usuario():
    cadastrar_usuario("usuario3", "senha3")
    assert autenticar_usuario("usuario3", "senha3") == True
    assert autenticar_usuario("usuario3", "senha_errada") == False
    assert autenticar_usuario("usuario_inexistente", "senha3") == False
