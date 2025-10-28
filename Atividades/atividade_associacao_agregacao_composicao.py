print('1) Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.\n')

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome


class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
    


pessoa_01 = Pessoa("Maria")
livro_01 = Livro("Dom Quixote")

print(f"{pessoa_01.nome} está lendo o livro {livro_01.titulo}")


print('\n2) Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.\n')

class Onibus:
    def __init__(self, linha: str):
        self.linha = linha


class Aluno:
    def __init__(self, nome: str):
        self.nome = nome


    def pegar_onibus(self, onibus: Onibus):
        print(f"{self.nome} está esperando a linha '{onibus.linha}'")


onibus = Onibus("Conde da Boa Vista - TI CDU")
aluno = Aluno("Ana")

aluno.pegar_onibus(onibus)


print('\n3) Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.\n')

class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

class Departamento:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionarios(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Funcionário: {funcionario.nome}")

funcionario_01 = Funcionario("Marcos")
funcionario_02 = Funcionario("Débora")
departamento = Departamento()
departamento.adicionar_funcionarios(funcionario_01)
departamento.adicionar_funcionarios(funcionario_02)

departamento.listar_funcionarios()