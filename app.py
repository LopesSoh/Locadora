from funcs import *

while True:
    menu_principal()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        LP()
        print("Entrada inválida, digite um número!")
        LP()
        continue
        

    match opcao:
        case 1: 
            pass
        case 2: 
            pass
        case 3: 
            pass
        case 0:
            LP()
            print("Saindo... ")
            break
        case _:
            print("Opção inválida! Tente novamente.")
            LP()