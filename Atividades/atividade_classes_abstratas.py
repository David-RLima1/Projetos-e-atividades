from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def falar(self):
       return "Falando"

    @abstractmethod
    def comer(self):
        return "Comendo"

    @abstractmethod
    def andar(self):
        return "Andando"

class Funcionario(Pessoa):
    
    def falar(self):
        print(f"Funcionário {super().falar()}")
        
    def comer(self):
        print(f"Funcionário {super().comer()}")
    
    def andar(self):
        print(f"Funcionário {super().andar()}")

class Aluno(Pessoa):
    
    def falar(self):
        print(f"Aluno {super().falar()}")
       
    def comer(self):
        print(f"Aluno {super().comer()}")

    def andar(self):
        print(f"Aluno {super().andar()}")


aluno = Aluno()
funcionario = Funcionario()

aluno.falar()
aluno.comer()
aluno.andar()

funcionario.falar()
funcionario.comer()
funcionario.andar()


class Pessoa(ABC):

    @abstractmethod
    def falar(self):
        ...
    
    @abstractmethod
    def comer(self):
        ...
    
    @abstractmethod
    def andar(self):
        ...