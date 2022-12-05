import utils

if __name__ == '__main__':
    with utils.cons.status(
        '[b]Conectando[/b] ao banco de dados...', spinner='noise'
    ):
        utils.sleep(2)
    while True:
        utils.menu()
