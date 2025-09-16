from classes import *
import os

def menu_principal():
    print("︿︿︿︿︿ 〔MENU LOCADORA〕 ︿︿︿︿︿")
    print(" 1- Cadastrar \n 2- Listar Clientes \n 3- Alugar/Devolver \n 4- Listar Itens \n 5- Listar intens locados \n 0- Sair ")

def LP():
    os.system('pause')
    os.system('cls')

def menu_cadastro():
    print("︿︿︿︿︿ 〔MENU CADASTRO〕 ︿︿︿︿︿")
    print(" 1- Cliente \n 2- Filme \n 3- Jogo \n 0- Sair ")

def cadastrar_cliente(locadora):
    try:
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        cliente = Cliente(nome, cpf)
        locadora.cadastrarCliente(cliente)
    except ValueError:
            print(" Entrada inválida!")

    

def cadastrar_filme(locadora):
        try:
            titulo = input("Título: ")
            genero = input("Gênero: ")
            duracao = int(input("Duração (minutos): "))
            filme = Filme(titulo, genero, duracao)
            locadora.cadastrarItem(filme)
            print(f"Filme '{filme.getTitulo()}' cadastrado com código {filme.getCodigo()}!")
            
        except ValueError:
            print(" Entrada inválida!")  

def cadastrar_jogo(locadora):
    try:
        titulo = input("Título: ")
        plataforma = input("Plataforma: ")
        faixa = int(input("Faixa Etária: "))
        jogo = Jogo(titulo, plataforma, faixa)
        locadora.cadastrarItem(jogo)
        print(f"Jogo '{titulo}' cadastrado com código {jogo.getCodigo()}!")
    except ValueError:
        print("Entrada inválida!")

def menu_alugardevolver():
    print("︿︿︿︿︿ 〔MENU ALUGAR/DEVOLVER〕 ︿︿︿︿︿")
    print(" 1- Alugar \n 2- Devolver \n 0- Sair ")

def alugar_item(locadora):
    cpf = input("Digite o CPF do cliente: ")
    try:
        locadora.listarItens()
        codigo_item = int(input("\n \n Digite o código do item a ser alugado: "))
    except ValueError:
        print("Código inválido!")
        LP()
        return
    
    
    cliente = None
    for c in locadora.getClientes():
        if c.getCpf() == cpf:
            cliente = c
            break

    if cliente is None:
        print("Cliente não encontrado!")
        LP()
        return

    item = None
    for i in locadora.getItens():
        if i.getCodigo() == codigo_item:
            item = i
            break

    if item is None:
        print("Item não encontrado!")
        LP()
        return

    if cliente.locar(item):
        print(f"Item '{item.getTitulo()}' alugado com sucesso para {cliente.getNome()}!")
    else:
        print("Esse item já está alugado.")
        LP()

def devolver_item(locadora):
    cpf = input("Digite o CPF do cliente: ")
    try:
        codigo_item = int(input("Digite o código do item a ser devolvido: "))
    except ValueError:
        print("Código inválido!")
        return

    cliente = None
    for c in locadora.getClientes():
        if c.getCpf() == cpf:
            cliente = c
            break

    if cliente is None:
        print("Cliente não encontrado!")
        return

    item = None
    for i in cliente.getItensLocados():
        if i.getCodigo() == codigo_item:
            item = i
            break

    if item is None:
        print("Esse item não está alugado por este cliente.")
        return

    if cliente.devolver(item):
        print(f"Item '{item.getTitulo()}' devolvido com sucesso!")
    else:
        print("Erro ao devolver item.")

def listar_itens_locados(locadora):
    cpf = input("Digite o CPF do cliente: ")
    cliente = None
    for c in locadora.getClientes():
        if c.getCpf() == cpf:
            cliente = c
            break

    if cliente is None:
        print("Cliente não encontrado!")
        return

    cliente.listarItensLocados()