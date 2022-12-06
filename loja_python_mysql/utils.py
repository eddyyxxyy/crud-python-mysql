from locale import LC_MONETARY, currency, setlocale
from time import sleep

import MySQLdb
from MySQLdb import Connection
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, FloatPrompt, IntPrompt, Prompt
from rich.table import Table

setlocale(LC_MONETARY, 'pt_BR.UTF-8')

connection: Connection

CONS = Console()
PROMP = Prompt()
CONF = Confirm()


def menu() -> None:
    """
    Função que gera o menu no terminal.

    :return: None
    """
    title = '[b]CRUD - Python/MySQL[/b]'
    options = Panel(
        """
        Selecione uma opção:

        [b]1[/b] - [cyan b]Listar[/] produtos;
        [b]2[/b] - [green b]Inserir[/] produtos;
        [b]3[/b] - [yellow b]Atualizar[/] produtos;
        [b]4[/b] - [red b]Deletar[/] produtos;
        [b]5[/b] - [deep_pink4]Sair[/] do programa.

        [grey]Pressione [b]enter[/b] para listar produtos ou digite "m", para abrir o menu novamente[/]
        """,
        title='[b]Gerenciamento de Produtos[/b]',
        subtitle=':snake:',
    )
    CONS.rule(title, align='center')
    CONS.print(options)
    get_option('\n-> ')


def conectar() -> Connection:
    """
    Função para se conectar ao servidor.

    :return: Connection
    """
    global connection
    sleep(2)
    try:
        connection = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='eddyxide',
            passwd='leandoer',
        )
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')
        return connection
    else:
        return connection


def desconectar(conexao: Connection) -> None:
    """
    Função para desconectar do servidor.

    :return: None
    """
    if conexao:
        conexao.close()


def listar() -> None:
    """
    Função para listar os produtos.

    :return: None
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    if len(produtos) > 0:
        table = Table(title='Produtos')
        table.add_column('id', justify='right', style='cyan')
        table.add_column('Nome', style='magenta')
        table.add_column('Preço', justify='right', style='green')
        table.add_column('Estoque', justify='right')
        for produto in produtos:
            table.add_row(
                str(produto[0]),
                str(produto[1]),
                currency(produto[2], grouping=True),
                str(produto[3]),
            )
        CONS.print()
        CONS.print(table)
        CONF.ask(
            '\nPressione [b]enter[/b] para continuar',
            show_choices=False,
            show_default=False,
            default='y',
        )
    else:
        CONS.print('[b][red]Não[/] há produtos cadastrados...[/b]')
    desconectar(conexao)


def inserir() -> None:
    """
    Função para inserir produtos no db.

    :return: None
    """
    conexao: Connection = conectar()
    cursor = conexao.cursor()

    nome: str = get_name('Informe o [b]nome[/b] do produto')
    preco: float = get_price('Informe o [b]preço[/b] do produto')
    estoque: int = get_int('Informe a [b]quantidade[/b] em [b]estoque[/b]')

    cursor.execute(
        f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', '{preco}', '{estoque}')"
    )

    conexao.commit()

    if cursor.rowcount == 1:
        CONS.print(
            f'\nO produto [b]"{nome}"[/b] foi inserido com [green b]sucesso[/]!'
        )
    else:
        CONS.print(f'\n[red b]Não[/] possível inserir [b]{nome}[/b].')

    CONF.ask(
        '\nPressione [b]enter[/b] para continuar',
        show_choices=False,
        show_default=False,
        default='y',
    )
    desconectar(conexao)


def atualizar() -> None:
    """
    Função para atualizar as informações de um produto.

    :return: None
    """
    CONS.print('\n[yellow b]Atualizando[/] produto...')

    conexao: Connection = conectar()
    cursor = conexao.cursor()
    codigo = get_int('Informe o id do produto')
    nome: str = get_name('Informe o novo nome do produto')
    preco: float = get_price('Informe o novo preço do produto')
    estoque: int = get_int('Informe a nova quantidade em estoque')

    cursor.execute(
        f"UPDATE produtos SET nome='{nome}', preco='{preco}', estoque='{estoque}' WHERE id={codigo}"
    )
    conexao.commit()

    if cursor.rowcount == 1:
        CONS.print(
            f'\nO produto [b]"{nome}"[/b] foi atualizado com [green b]sucesso[/]!'
        )
    else:
        CONS.print(f'\n[red b]Não[/] possível atualizar [b]{nome}[/b].')
    CONF.ask(
        'Pressione [b]enter[/b] para continuar',
        show_choices=False,
        show_default=False,
        default='y',
    )


def deletar() -> None:
    """
    Função para deletar um produto do db.

    :return: None
    """
    CONS.print('\n[red b]Deletando[/] produto...')
    CONF.ask(
        'Tem certeza que deseja deletar o item?',
        choices=['y', 'n'],
    )
    CONF.ask(
        'Pressione [b]enter[/b] para continuar',
        show_choices=False,
        show_default=False,
        default='y',
    )


def get_option(imput_prompt: str) -> None:
    while True:
        try:
            opcao = PROMP.ask(imput_prompt, default='1').lower()
            match opcao:
                case '1' | 'listar' | 'list' | 'query':
                    with CONS.status('[cyan b]Listando[/] produtos...'):
                        sleep(0.4)
                    listar()
                case '2' | 'inserir' | 'insert' | 'add':
                    with CONS.status('[green b]Inserindo[/] produto(s)...'):
                        sleep(0.4)
                    inserir()
                case '3' | 'atualizar' | 'update' | 'mod':
                    with CONS.status('[yellow b]Atualizando[/] produto(s)...'):
                        sleep(0.4)
                    atualizar()
                case '4' | 'deletar' | 'delete' | 'remove':
                    with CONS.status('[red b]Deletando[/] produto(s)...'):
                        sleep(0.4)
                    deletar()
                case '5' | 'sair' | 'q' | 'quit' | 'exit':
                    if CONF.ask(
                        'Tem certeza que deseja sair da aplicação?',
                        choices=['y', 'n'],
                    ):
                        with CONS.status(
                            '[deep_pink4]Finalizando[/] seção...'
                        ):
                            sleep(0.4)
                            CONS.print('[deep_pink4]Seção finalizada...[/]')
                            exit()
                case 'm' | 'menu':
                    menu()
                case _:
                    raise ValueError
            break
        except ValueError:
            CONS.print('[red i]Opção inválida, teste novamente...')


def get_name(prompt: str) -> str:
    nome: str = PROMP.ask(prompt)
    return nome.strip().title()


def get_price(prompt: str) -> float:
    preco: float = 0.0
    try:
        preco = float(FloatPrompt.ask(prompt))
        if preco <= 0:
            raise ValueError
        return preco
    except ValueError:
        CONS.print('[red i]Valor inválido...[/]')
    return preco


def get_int(prompt: str) -> int:
    integer: int = 0
    try:
        integer = IntPrompt.ask(prompt)
        if integer < 0:
            raise ValueError
        return integer
    except ValueError:
        CONS.print('[red i]Valor inválido...[/]')
    return integer
