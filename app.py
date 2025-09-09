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
        

    match opcao:
        case 1: 
            while True:
                menu_cadastro()
                try:
                    opcao2 = int(input("Escolha uma opção: "))
                except ValueError:
                    LP()
                    print("Entrada inválida, digite um número!")
                    LP()
                    continue
                
                match opcao2:
                    case 1:
                        LP()
                        print("CADASTRAR CLIENTE")
                        cadastrar_cliente(locadora)
                        LP()
                    
                    case 2:
                        LP()
                        print("CADASTRAR FILME")
                        cadastrar_filme(locadora)
                        LP()
            
                    case 3:
                        LP()
                        pass
                    case 0:
                        LP()
                        break

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