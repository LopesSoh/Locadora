from classes import *
import os

def menu_principal():
    print("︿︿︿︿︿ 〔MENU LOCADORA〕 ︿︿︿︿︿")
    print(" 1- Cadastrar \n 2- Listar Clientes \n 3- Alugar/Devolver \n 4- Listar Itens \n 0- Sair ")

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