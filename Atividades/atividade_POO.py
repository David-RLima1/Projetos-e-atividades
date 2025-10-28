print('''1) Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e 
imprima os valores de seus atributos.\n''')

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    def __str__(self) -> str:
        return f'Nome: {self.__nome}\nIdade: {self.__idade} anos'

    def __repr__(self) -> str:
        return f'Pessoa(nome={self.__nome}, idade={self.__idade})'
    
    @property
    def nome(self) -> str:
        return self.__nome

    
    @property
    def idade(self) -> int:
        return self.__idade
    
    def apresentar(self) -> None:
        print(f'Olá, meu nome é {self.__nome} e tenho {self.__idade} anos.')
    
pessoa_01 = Pessoa('Ana', 22)
pessoa_02 = Pessoa('Paulo', 31)

print(pessoa_01)
print('-' * 75)
print(f'Nome: {pessoa_01.nome}\nIdade: {pessoa_01.idade} anos')
print('=' * 75)
print(pessoa_02)
print('-' * 75)
print(f'Nome: {pessoa_02.nome}\nIdade: {pessoa_02.idade} anos')
print('=' * 75)


print('''\n2) Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, 
meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.\n''')

pessoa_03 = Pessoa('João', 25)

pessoa_03.apresentar()

print('''\n3) Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para 
inicializar esses valores. Crie três objetos e mostre suas informações.\n''')

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def __str__(self) -> str:
        return f'Marca: {self.__marca}\nModelo: {self.__modelo}\nAno: {self.__ano}'
    

    def __repr__(self) -> str:
        return f'Carro(marca= {self.__marca}, modelo= {self.__modelo}, ano= {self.__ano})'
    

    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, nova_marca: str) -> None:
        if nova_marca:
            self.__marca = nova_marca

    @property
    def modelo(self) -> str:
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo: str) -> None:
        if novo_modelo:
            self.__modelo = novo_modelo

    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano: int) -> None:
        if novo_ano > 1960:
            self.__ano = novo_ano
    

carro_01 = Carro('Ford', 'Mustang', 1969)
carro_02 = Carro('Chevrolet', 'Impala', 1970)
carro_03 = Carro('Crovrolet', 'Chevett', 1974)

print(carro_01)
print('-' * 75)
print(carro_02)
print('-' * 75)
print(carro_03)

print('''\n4) Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). 
Imprima antes e depois da alteração.\n''')


print(carro_01)
carro_01.ano = 2005
print('-' * 75)
print(carro_01)

print('''\n5) Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o 
saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.\n''')

class ContaBancaria:
    def __init__(self, titular, saldo = 0) -> None:
        self.__titular = titular
        self.__saldo = saldo


    def __str__(self) -> str:
        return f'Titular: {self.__titular} | Saldo: R$ {self.__saldo:.2f}'
    

    def __repr__(self) -> str:
        return f'ContaBancaria(titular= {self.__titular}, saldo= {self.__saldo})'
    
    
    @property
    def titular(self) -> str:
        return self.__titular
    

    @titular.setter
    def titular(self, novo_titular: str) -> None:
        if novo_titular:
            self.__titular = novo_titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo

    
    def depositar(self, deposito: float) -> None:
        if not isinstance(deposito, (int, float)):
            print('Depósito inválido.')
            return False
        
        if deposito <= 0:
            print('O depósito deve ser um número positivo.')
            return False
        
        self.__saldo += deposito
        print(f'Valor depositado: R$ {deposito:.2f}')
        return True
    

    def sacar(self, saque: float) -> bool:
        if not isinstance(saque, (int, float)) or saque <= 0:
            print('Saque inválido.')
            return False
        
        if saque > self.__saldo:
            print('Saldo insuficiente.')
            return False

        self.__saldo -= saque
        print(f'Valor Sacado: R$ {saque:.2f}')
        return True

    def checar_saldo(self) -> None:
        print(f'Saldo atual: R$ {self.__saldo:.2f}')


pessoa_04 = ContaBancaria('Ana')
print(pessoa_04)
pessoa_04.depositar(1000)
pessoa_04.checar_saldo()
pessoa_04.sacar(1500)
pessoa_04.checar_saldo()

print('''\n6) Modifique a classe ContaBancaria para que o método sacar retorne True se a operação 
for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.\n''')


pessoa_05 = ContaBancaria("Juca")

pessoa_05.depositar(1000)

if pessoa_05.sacar(100):
    print("Saque realizado!")
else:
    print("Saque não realizado.")


print('''\n7) Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha 
uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.\n''')


class Aluno:

    def __init__(self, nome: str, nota: float) -> None:
        self.__nome = nome
        self.__nota = nota
    
    def __str__(self) -> str:
        return f'Aluno: {self.__nome} - Nota: {self.__nota}'
    

    def __repr__(self) -> str:
        return f'Aluno(nome= {self.__nome}, nota= {self.__nota})'

    
    @property
    def nome(self) -> str:
        return self.__nome
    

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if novo_nome:
            self.__nome = novo_nome

    @property
    def nota(self) -> float:
        return self.__nota


class Turma:

    def __init__(self) -> None:
        self.__lista_alunos = []
    

    def adicionar_aluno(self, aluno: object):
        self.__lista_alunos.append(aluno)
    
    def listar_alunos(self) -> bool:
        if not self.__lista_alunos:
            print('Lista vazia.')
            return False
        
        print('ALUNOS')
        print('-' * 75)
        for aluno in self.__lista_alunos:
            print(aluno)
       
        return True
    

aluno_01 = Aluno('Carlos', 7.5)
aluno_02 = Aluno('Mercedes', 5)

turma_01 = Turma()
turma_01.adicionar_aluno(aluno_01)
turma_01.adicionar_aluno(aluno_02)
turma_01.listar_alunos()

print('''\n8) Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe,
apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.\n''')
    
aluno_03 = Aluno('Maria', 9.5)
print(aluno_03)


print('''\n9) Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos 
de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.\n''')

class Cachorro:

    especie = "Canis familiaris"

    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade
        

    def __str__(self) -> str:
        return f'Nome: {self.__nome}\nIdade: {self.__idade}'
    

    def __repr__(self) -> None:
        return f'Cachorro(nome = {self.__nome}, idade = {self.__idade})'
    

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if novo_nome:
            self.__nome = novo_nome
    
    @property
    def idade(self) -> str:
        return self.__idade
    
    @idade.setter
    def idade(self, novo_idade: int) -> None:
        if novo_idade:
            self.__idade = novo_idade



toto = Cachorro('Totó', 7)

print(toto.especie)
print(Cachorro.especie)