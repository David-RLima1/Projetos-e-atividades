class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_lendo = None 

    def definir_leitura(self, livro: Livro):
        self.livro_lendo = livro

print("--- 1. Associação (Pessoa e Livro) ---")
livro_python = Livro("Python para Devs")
pessoa_joao = Pessoa("João")
pessoa_joao.definir_leitura(livro_python)
print(f"{pessoa_joao.nome} está lendo {pessoa_joao.livro_lendo.titulo}")


class Onibus:
    def __init__(self, linha):
        self.linha = linha
        
    def embarcar(self):
        print(f"Embarcando no ônibus {self.linha}.")

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def ir_para_escola(self, onibus: Onibus):
        print(f"{self.nome} indo para a escola.")
        onibus.embarcar() 

print("\n--- 2. Dependência (Aluno e Onibus) ---")
onibus_escolar = Onibus("501")
aluno_pedro = Aluno("Pedro")
aluno_pedro.ir_para_escola(onibus_escolar)


class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = [] 
        
    def add_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        
    def listar_funcionarios(self):
        print(f"Depto. {self.nome}:")
        for f in self.funcionarios:
            print(f" - {f.nome} ({f.cargo})")

print("\n--- 3. Agregação (Departamento e Funcionarios) ---")
f1 = Funcionario("Ana", "Engenheira")
f2 = Funcionario("Bruno", "Analista")
depto_ti = Departamento("T.I.")
depto_ti.add_funcionario(f1)
depto_ti.add_funcionario(f2)
depto_ti.listar_funcionarios()
del depto_ti
print(f"Funcionario f1 ({f1.nome}) ainda existe.")


class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []
        
    def contratar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def mostrar_elenco(self):
        print(f"Elenco do {self.nome_time}:")
        for j in self.jogadores:
            print(f" - {j.nome} ({j.posicao})")

print("\n--- 4. Agregação (Time e Jogador) ---")
j1 = Jogador("Ronaldo", "Atacante")
j2 = Jogador("Zidane", "Meio-campo")
time_galatico = Time("Real Madrid")
time_galatico.contratar_jogador(j1)
time_galatico.contratar_jogador(j2)
time_galatico.mostrar_elenco()


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"  -> Motor {self.potencia}cv criado.")
        
    def __del__(self):
        print(f"  -> Motor {self.potencia}cv destruído.")

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
        print(f"Carro '{self.modelo}' fabricado.")
        
    def __del__(self):
        print(f"Carro '{self.modelo}' destruído.")

print("\n--- 5. Composição (Carro e Motor) ---")
meu_carro = Carro("Fusca", 1.6)
print(f"Motor do {meu_carro.modelo}: {meu_carro.motor.potencia}cv.")
print("Apagando a referência ao carro...")
del meu_carro 


class Comodo:
    def __init__(self, nome_comodo, area_m2):
        self.nome_comodo = nome_comodo
        self.area_m2 = area_m2
        print(f"  -> Cômodo '{self.nome_comodo}' ({area_m2}m²) criado.")

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []
        print(f"Casa em '{self.endereco}' sendo construída.")
        
    def add_comodo(self, nome_comodo, area_m2):
        novo_comodo = Comodo(nome_comodo, area_m2)
        self.comodos.append(novo_comodo)
        
    def listar_comodos(self):
        print(f"Planta da casa em {self.endereco}:")
        for c in self.comodos:
            print(f"- {c.nome_comodo} ({c.area_m2}m²)")

print("\n--- 6. Composição (Casa e Comodos) ---")
minha_casa = Casa("Rua das Flores, 123")
minha_casa.add_comodo("Sala", 20)
minha_casa.add_comodo("Cozinha", 15)
minha_casa.add_comodo("Quarto", 12)
minha_casa.listar_comodos()