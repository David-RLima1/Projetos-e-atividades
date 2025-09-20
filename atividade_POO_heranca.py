
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
    
    def saucadao(self) -> str:
        return f"Olá, usuário"

class Cliente(Usuario):
    def __init__(self,nome: str, email: str, saldo: float)-> None:
        super().__init__(nome, email)
        self.saldo = saldo
    
    
    def saucadao(self):
        return f"Olá, cliente."


pessoa_01 = Cliente('Maria', 'maria@email.com')
print(pessoa_01)


print("""\n2) Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. 
Mostre como chamar o método herdado a partir de um objeto Cliente.\n""")

pessoa_01.exibir_informacoes()

print("""\n3) Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, 
sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.\n""")

print(pessoa_01.saucadao())

print("""\nNa classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que 
inicialize também os atributos de Usuario usando super().\n""")

