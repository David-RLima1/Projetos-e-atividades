
print("""\n1) Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe 
Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.\n""")


class Usuario:
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email
    
    def __str__(self)-> str:
        return f"Nome: {self.nome} | Email: {self.email}"

    def exibir_informacoes(self)-> None:
        print(f"Nome: {self.nome}\nEmail: {self.email}")
    
    def saudacao(self) -> str:
        return f"Olá, usuário"

class Cliente(Usuario):
    def __init__(self,nome: str, email: str, saldo: float):
        super().__init__(nome, email)
        self.saldo = saldo
    
    
    def saudacao(self) -> str:
        return f"Olá, cliente."


pessoa_01 = Cliente('Maria', 'maria@email.com', 500)
print(pessoa_01)


print("""\n2) Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. 
Mostre como chamar o método herdado a partir de um objeto Cliente.\n""")

pessoa_01.exibir_informacoes()

print("""\n3) Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, 
sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.\n""")

print(pessoa_01.saudacao())

print("""\n4) Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que 
inicialize também os atributos de Usuario usando super().\n""")

print(f"R$ {pessoa_01.saldo:.2f}")


print("""\n5) Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que 
herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos. \n""")

class Funcionario(Usuario):
    pass

class Gerente(Funcionario):
    pass

gerente = Gerente("Marcos", "marcos@email.com")

print(gerente)

print("""\n6) Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método 
verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?\n""")

class Autenticacao:
    
    def login(self, email: str, senha: str):

        if email == "usuario" and senha == "12345":
            return True
        return False
    
    def status(self):
        print("Autenticação!")


class Permissao:

    def verificar_permissao(self, autenticacao: bool):

        if autenticacao:
            print("Bem vindo!")
            return True
        
        print("Senha ou usuário incorreto.")
        return False

    def status(self):
        print("Permissão!")
    

class Administrador(Autenticacao, Permissao):
    pass



usuario = Administrador()

checagem = usuario.login("usuario", "12345")
usuario.verificar_permissao(checagem)


    
print("""\n7) Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador 
herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.\n""")


usuario.status()