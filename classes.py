class Item:
    _contador = 1

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
    
    # GETS e SETS
    def getCodigo(self):
        return self.__codigo   # não terá set, código é fixo

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    def getDisponivel(self):
        return self.__disponivel

    def setDisponivel(self, status: bool):
        self.__disponivel = status

class Filme(Item):
    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        Item.__init__(self, titulo)
        self.__genero = genero
        self.__duracao = duracao

    def getGenero(self):
        return self.__genero

    def setGenero(self, novo_genero: str):
        self.__genero = novo_genero

    def getDuracao(self):
        return self.__duracao

    def setDuracao(self, nova_duracao: int):
        self.__duracao = nova_duracao

class Jogo(Item):
    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        Item.__init__(self, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    def getPlataforma(self):
        return self.__plataforma

    def setPlataforma(self, nova_plataforma: str):
        self.__plataforma = nova_plataforma

    def getFaixaEtaria(self):
        return self.__faixaEtaria

    def setFaixaEtaria(self, nova_faixa: int):
        self.__faixaEtaria = nova_faixa


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
    
    def getNome(self):
        return self.__nome

    def setNome(self, novo_nome: str):
        self.__nome = novo_nome

    def getCpf(self):
        return self.__cpf

    def setCpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    def getItensLocados(self):
        return self.__itensLocados


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
