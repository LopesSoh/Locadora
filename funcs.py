from classes import *
import os

def menu_principal():
    print("︿︿︿︿︿ 〔MENU LOCADORA〕 ︿︿︿︿︿")
    print(" 1- Cadastrar \n 2- Listar \n 3- Alugar/Devolver \n 0- Sair ")

def LP():
    os.system('pause')
    os.system('cls')

def menu_cadastro():
    print("︿︿︿︿︿ 〔MENU CADASTRO〕 ︿︿︿︿︿")
    print(" 1- Cliente \n 2- Filme \n 3- Jogo \n 0- Sair ")

def cadastrar_cliente(locadora, nome, cpf, cliente):
    locadora.cadastrarCliente(cliente)
    

def cadastrar_filme(locadora, titulo, genero, duracao):
        try:
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            filme = Filme(titulo, genero, duracao)
            locadora.cadastrarItem(filme)
            print(f"Cliente {nome} cadastrado!")
        except ValueError:
            print(" Entrada inválida!")
        


def cadastrar_jogo(locadora):
    try:
        titulo = input("Título: ")
        plataforma = input("Plataforma: ")
        faixa = int(input("Faixa Etária: "))
        jogo = Jogo(titulo, plataforma, faixa)
        locadora.cadastrarItem(jogo)
        print(f"Jogo '{titulo}' cadastrado com código {jogo.codigo}!")
    except ValueError:
        print("⚠️ Entrada inválida!")

