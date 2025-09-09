class Cliente:
    pass

class Item:
    pass

class Filme(Item):
    pass

class Jogos(Item):
    pass

class Locadora:
    def __init__ (self):
        self.__clientes = []
        self.__itens =[]

    def cadastrarCliente (self, cliente:Cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado!")

    def cadastrarItem (self, item:Item):
        self.item.append(item)
        print(f"Item {item.nome} cadastrado!")

    def listarClientes(self):
        print("•═❀═• CLIENTES CADASTRADOS •═❀═•")
        if len(self.clientes) > 0:
            for cliente in self.clientes:
                print(f"- {cliente.nome} (CPF: {cliente.cpf})")
        else:
            print("Nenhum cliente cadastrado.")
            
    def listarItens(self):
        print("\n •═❀═• ITENS NA LOCADORA •═❀═•")
        if len(self.itens) > 0:
            for item in self.itens:
                status = "Disponível" if item.disponivel else "Alugado"
                print(f"- {item.codigo} | {item.titulo} ({status})")
        else:
            print("Nenhum item cadastrado.")
