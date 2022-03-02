from libpythonpro.spam.modelos import Usuario


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Eriko')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Eriko'), Usuario(nome='Nayara')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
