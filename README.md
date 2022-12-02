# CRUD com Python e MySQL

![Python Badge](https://img.shields.io/badge/Python-1076AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL Badge](https://img.shields.io/badge/mysql-3776AB.svg?style=for-the-badge&logo=mysql&logoColor=white)

Aplicação CRUD simples e direto ao ponto com Python e MySQL.

Este repositório tem como intuíto a prática e estudo das tecnologias utilizadas.

Este projeto faz parte da criação de 6 CRUDS diferentes (ou não tão diferentes assim);
três deles utilizão bancos relacionais e os outros não relacionais.

Neste projeto em específico, como o nome do repositório sugere, é um CRUD para terminal
com Python e MySQL.


## Ambiente de Desenvolvimento

Para a criação deste CRUD estou utilizando as seguintes tecnologias:

- Python 3.11;
- MySQL 8.0.31;
- Poetry 1.22.0;
- pre-commit 2.20.0;
- blue 0.9.1;
- isort 5.10.1;
- mypy 0.991;


## Utilização da base de projeto ([v.0.1.0](https://github.com/eddyyxxyy/loja-python-mysql/tree/5a7b20b1f2636168028f058d8447d13dce5f2228))

Clonar o repositório na versão 0.1.0 te permite já visualizar a estrutura básica de
um CRUD desenvolvido em Python, para poder implementar em praticamente qualquer outro
banco de dados.

> Lembre-se de estar com o terminal na pasta raiz do projeto, onde se encontra o arquivo pyproject.toml

Para utilizar as ferramentas de CI (para controle de qualidade de código e outras coisas
mais) é necessário, após inicializar seu ambiente virtual poetry com:

```shell
poetry shell

poetry install
```

É só dar o comando:

```shell
pre-commit install
```

Assim, a cada commit da sua aplicação, você terá uma verificação e correção automática na estrutura do seu código,
de suas type-hints, da ordenação de seus imports e mais alguns detalhes que julgo importante nos arquivos adjacentes de
seu projeto.

E lembrando que, essa estrutura é super básica, é somente para dar um "norte" para mim ou para alguém que está
implementando seu primeiro (ou um de seus primeiros) CRUDs. O que fazer com essa base, depende única e exclusivamente
de você.

À partir do commit que se encontra a tag da versão v0.1.0, a implementação será criada conforme eu imaginar que deva ser.

## ATENÇÃO

Se você utiliza algum outro editor de código ou IDE que não seja da Jetbrains, sugiro fortemente que coloque as pastas
de configuração criadas pelos editores de código/IDEs no arquivo ".gitignore".

## Motivação

Deixo aqui a frase que me move, que me define os esforços em cada objetivo que traço:

> "Tudo o que temos a decidir é o que fazer com o tempo que nos é concedido."
> (Tolkien, John Ronald Reuel. O Senhor dos Anéis: A Sociedade do Anel, 1954, P. 104)

### Contato:

[LinkedIn](https://www.linkedin.com/in/eeddyyxxyy/ "Para contato profissional")

---

![Eddy](logo.png)
