import utils

if __name__ == '__main__':
    with utils.CONS.status(
        '[b]Conectando[/b] ao banco de dados...', spinner='noise'
    ):
        utils.sleep(2)
    utils.menu()
    while True:
        utils.get_option(imput_prompt='\n-> ')
