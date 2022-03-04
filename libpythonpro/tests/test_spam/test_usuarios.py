from libpythonpro.spam.modelos import Usuario


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Eriko', email='erikoa.93@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Eriko', email='erikoa.93@gmail.com'),
                Usuario(nome='Nayara', email='nayara.t.95@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
