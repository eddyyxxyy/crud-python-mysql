from locale import LC_ALL, currency, setlocale
from time import sleep

import MySQLdb
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

setlocale(LC_ALL, 'pt_BR.UTF-8')

cons = Console()
promp = Prompt()
conf = Confirm()


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

        [grey]Pressione [b]enter[/b] para listar produtos[/]
        """,
        title='[b]Gerenciamento de Produtos[/b]',
        subtitle=':snake:',
    )
    cons.rule(title, align='center')
    get_option(options, '\n-> ')


def conectar() -> MySQLdb.connect:
    """
    Função para se conectar ao servidor.

    :return: None
    """
    sleep(2)
    try:
        connection = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='eddyxide',
            passwd='leandoer',
        )
        return connection
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')


def desconectar(conexao: MySQLdb.connect) -> None:
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
    cons.print('\n[cyan b]Listando[/] produtos...')
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
                produto[0],
                produto[1],
                currency(produto[2], grouping=True),
                produto[3],
            )
        cons.print(table)
    else:
        cons.print('[b][red]Não[/] há produtos cadastrados...[/b]')
    desconectar(conexao)


def inserir() -> None:
    """
    Função para inserir produtos no db.

    :return: None
    """
    cons.print('\n[green b]Inserindo[/] produto...')


def atualizar() -> None:
    """
    Função para atualizar as informações de um produto.

    :return: None
    """
    cons.print('\n[yellow b]Atualizando[/] produto...')


def deletar() -> None:
    """
    Função para deletar um produto do db.

    :return: None
    """
    cons.print('\n[red b]Deletando[/] produto...')


def get_option(options: Panel, imput_prompt: str) -> None:
    cons.print(options)
    while True:
        try:
            opcao = promp.ask(imput_prompt, default='1').lower()
            match opcao:
                case '1' | 'listar' | 'list' | 'query':
                    with cons.status('[cyan b]Listando[/] produtos...'):
                        sleep(2)
                    listar()
                case '2' | 'inserir' | 'insert' | 'add':
                    with cons.status('[green b]Inserindo[/] produto(s)...'):
                        sleep(2)
                    inserir()
                case '3' | 'atualizar' | 'update' | 'mod':
                    if conf.ask(
                        'Tem certeza que deseja atualizar o item?',
                        choices=['s', 'n'],
                    ):
                        with cons.status(
                            '[yellow b]Atualizando[/] produto(s)...'
                        ):
                            sleep(2)
                        atualizar()
                case '4' | 'deletar' | 'delete' | 'remove':
                    if conf.ask(
                        'Tem certeza que deseja deletar o item?',
                        choices=['s', 'n'],
                    ):
                        with cons.status('[red b]Deletando[/] produto(s)...'):
                            sleep(2)
                        deletar()
                case '5' | 'sair' | 'q' | 'quit' | 'exit':
                    if conf.ask(
                        'Tem certeza que deseja sair da aplicação?',
                        choices=['y', 'n'],
                    ):
                        with cons.status(
                            '[deep_pink4]Finalizando[/] seção...'
                        ):
                            sleep(2)
                            cons.print('[deep_pink4]Seção finalizada...[/]')
                            exit()
                case _:
                    raise ValueError
            break
        except ValueError:
            cons.print('[red i]Opção inválida, teste novamente...')
