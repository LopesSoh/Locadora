# Sistema de Locadora

O projeto é um sistema de locadora de filmes e jogos escrito em Python. Ele foi estruturado em três arquivos principais: `classes.py`, onde estão as classes que representam os objetos do sistema; `funcs.py`, que contém as funções responsáveis pelos menus e operações; e `app.py`, que é o arquivo principal para execução do programa. A seguir, cada parte do código será mostrada com sua explicação.

---

## Arquivo classes.py

```python
class Item:
    _contador = 1

    def __init__(self, titulo: str):
        self.__codigo = Item._contador
        Item._contador += 1
        self.__titulo = titulo
        self.__disponivel = True

```

A classe `Item` é a classe base do sistema, utilizada tanto para filmes quanto para jogos. Ela possui um contador estático `_contador` para gerar códigos automáticos para cada item cadastrado. O construtor recebe apenas o título, define o código e marca o item como disponível.

```python
    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

```

Os métodos `alugar` e `devolver` controlam a disponibilidade do item. O método `alugar` só funciona se o item estiver disponível, e o método `devolver` só funciona se o item já estiver alugado.

```python
    def getCodigo(self):
        return self.__codigo   # não terá set, código é fixo

```

O código do item é imutável, por isso só existe o getter. Para os outros atributos (título e disponibilidade) há getters e setters, permitindo leitura e modificação.

---

```python
class Filme(Item):
    def __init__(self, titulo: str, genero: str, duracao: int):
        Item.__init__(self, titulo)
        self.__genero = genero
        self.__duracao = duracao

```

A classe `Filme` herda de `Item` e adiciona dois atributos: gênero e duração. Ela utiliza o construtor da classe `Item` para inicializar o título e o código. Além disso, possui métodos getters e setters específicos para gênero e duração.

---

```python
class Jogo(Item):
    def __init__(self, titulo: str, plataforma: str, faixaEtaria: int):
        Item.__init__(self, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

```

A classe `Jogo` também herda de `Item`, mas adiciona atributos diferentes: plataforma e faixa etária. Assim como em `Filme`, há métodos getters e setters para manipular esses dados.

---

```python
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

```

A classe `Cliente` representa os clientes cadastrados na locadora. Cada cliente tem nome, CPF e uma lista de itens alugados.

```python
    def locar(self, item: Item):
        if item.alugar():
            self.__itensLocados.append(item)
            return True
        return False

```

O método `locar` permite que o cliente alugue um item. Ele só funciona se o item estiver disponível. Caso dê certo, o item é adicionado à lista de itens locados do cliente.

```python
    def devolver(self, item: Item):
        if item in self.__itensLocados and item.devolver():
            self.__itensLocados.remove(item)
            return True
        return False

```

O método `devolver` realiza o processo inverso: remove o item da lista de itens alugados e marca o item como disponível novamente.

---

```python
class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []

```

A classe `Locadora` é a responsável por gerenciar os clientes e itens. Ela possui listas para armazenar ambos.

```python
    def cadastrarCliente(self, cliente: Cliente):
        self.__clientes.append(cliente)
        print(f"Cliente {cliente.getNome()} cadastrado!")

    def cadastrarItem(self, item: Item):
        self.__itens.append(item)
        print(f"Item {item.getTitulo()} cadastrado!")

```

Estes métodos permitem adicionar clientes e itens à locadora.

```python
    def listarClientes(self):
        if len(self.__clientes) > 0:
            for cliente in self.__clientes:
                print(f"- {cliente.getNome()} (CPF: {cliente.getCpf()})")
        else:
            print("Nenhum cliente cadastrado.")

```

O método `listarClientes` exibe todos os clientes cadastrados. O método `listarItens` funciona de forma similar, mas mostrando o código, título e status de cada item.

---

## Arquivo funcs.py

```python
def menu_principal():
    print("︿︿︿︿︿ 〔MENU LOCADORA〕 ︿︿︿︿︿")
    print(" 1- Cadastrar \n 2- Listar Clientes \n 3- Alugar/Devolver \n 4- Listar Itens \n 5- Listar intens locados \n 0- Sair ")

```

As funções que começam com `menu_` servem apenas para exibir opções na tela. O `menu_principal` é o primeiro a ser mostrado, com todas as opções do sistema.

```python
def cadastrar_cliente(locadora):
    try:
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        cliente = Cliente(nome, cpf)
        locadora.cadastrarCliente(cliente)
    except ValueError:
        print(" Entrada inválida!")

```

Esta função coleta os dados de um cliente, cria um objeto `Cliente` e o adiciona à locadora. O mesmo processo é usado em `cadastrar_filme` e `cadastrar_jogo`, mudando apenas os dados solicitados.

```python
def alugar_item(locadora):
    cpf = input("Digite o CPF do cliente: ")
    ...

```

A função `alugar_item` solicita o CPF do cliente, lista os itens disponíveis e pede o código do item. Se o cliente e o item forem encontrados, e se o item estiver disponível, ele é alugado pelo cliente.

```python
def devolver_item(locadora):
    cpf = input("Digite o CPF do cliente: ")
    ...

```

Já a função `devolver_item` funciona de forma inversa: pede o CPF e o código do item, verifica se o cliente realmente está com aquele item alugado e então devolve.

```python
def listar_itens_locados(locadora):
    cpf = input("Digite o CPF do cliente: ")
    ...

```

A função `listar_itens_locados` mostra todos os itens que um cliente específico alugou.

---

## Arquivo app.py

```python
from funcs import *

locadora = Locadora()
while True:
    menu_principal()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        LP()
        print("Entrada inválida, digite um número!")
        LP()
        continue

```

O arquivo `app.py` é o ponto de entrada do programa. Ele cria um objeto `Locadora` e entra em um loop infinito que exibe o menu principal. O usuário escolhe a opção digitando um número.

```python
    match opcao:
        case 1:
            while True:
                LP()
                menu_cadastro()
                ...

```

A estrutura `match case` é usada para organizar o fluxo do programa. Se o usuário escolher `1`, o sistema abre o submenu de cadastro, que permite cadastrar clientes, filmes ou jogos.

```python
        case 3:
            while True:
                LP()
                menu_alugardevolver()
                ...

```

A opção `3` abre o menu de aluguel e devolução. Dentro dele, o usuário pode alugar ou devolver um item.

```python
        case 4:
            LP()
            locadora.listarItens()
            LP()

```

A opção `4` lista todos os itens cadastrados, mostrando quais estão disponíveis e quais estão alugados.

```python
        case 5:
            LP()
            listar_itens_locados(locadora)
            LP()

```

A opção `5` mostra todos os itens alugados por um cliente específico, de acordo com o CPF digitado.

```python
        case 0:
            LP()
            print("Saindo... ")
            break

```

A opção `0` encerra o programa.
