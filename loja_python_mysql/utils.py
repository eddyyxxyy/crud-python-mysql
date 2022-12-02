def menu() -> None:
    """
    Função que gera o menu no terminal.

    :return: None
    """
    print(
        'Gerenciamento de Produtos'
        + '\n\n'
        + 'Selecione uma opção:\n'
        + '1 - Listar produtos;\n'
        + '2 - Inserir produtos;\n'
        + '3 - Atualizar produtos;\n'
        + '4 - Deletar produtos.',
        flush=True,
    )
    opcao = int(input('->'))
    match opcao:
        case 1:
            listar()
        case 2:
            inserir()
        case 3:
            atualizar()
        case 4:
            deletar()
        case _:
            print(f'Opção {opcao} é inválida')


def conectar() -> None:
    """
    Função para se conectar ao servidor.

    :return: None
    """
    print('\nConectando-se ao servidor...')


def desconectar() -> None:
    """
    Função para desconectar do servidor.

    :return: None
    """
    print('\nDesconectando do servidor...')


def listar() -> None:
    """
    Função para listar os produtos.

    :return: None
    """
    print('\nListando produtos...')


def inserir() -> None:
    """
    Função para inserir produtos no db.

    :return: None
    """
    print('\nInserindo produto...')


def atualizar() -> None:
    """
    Função para atualizar as informações de um produto.

    :return: None
    """
    print('\nAtualizando produto...')


def deletar() -> None:
    """
    Função para deletar um produto do db.

    :return: None
    """
    print('\nDeletando produto...')
