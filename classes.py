class Item:
    def __init__(self, titulo: str):
        self.__codigo = Item._contador  
        Item._contador += 1
        self.__titulo = titulo
        self.__disponivel = True


    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False

class Filme(Item):
    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        Item.__init__(self, titulo)
        self.__genero = genero
        self.__duracao = duracao

class Jogos(Item):
    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        Item.__init__(self, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

    def locar(self, item: Item):
        if item.alugar():
            self.itensLocados.append(item)
            return True
        return False

    def devolver(self, item: Item):
        if item in self.itensLocados and item.devolver():
            self.itensLocados.remove(item)
            return True
        return False

    def listarItens(self):
        return [item.titulo for item in self.itensLocados]


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
