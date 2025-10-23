from abc import ABC, abstractmethod

# 1. Definição de classe abstrata


class Animal(ABC):
    
    @abstractmethod
    def falar(self):
        """Método abstrato que define a fala do animal."""
        pass


class Cachorro(Animal):
    def falar(self):
        print("Au au!")


class Gato(Animal):
    def falar(self):
        print("Miau!")


print("--- 1. Definição ---")
meu_cachorro = Cachorro()
meu_gato = Gato()

print("Cachorro diz:")
meu_cachorro.falar()

print("Gato diz:")
meu_gato.falar()

# -----------------------------------------------------

# 2. Proibição de instanciamento

print("\n--- 2. Proibição de Instanciamento ---")
try:
    animal_abstrato = Animal()
    print(animal_abstrato)
except TypeError as e:
    print(f"Erro gerado: {e}")



# -----------------------------------------------------

# 3. Múltiplos métodos abstratos

class FormaGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
        
    def perimetro(self):
        return 2 * (self.base + self.altura)

print("\n--- 3. Múltiplos Métodos (Retangulo) ---")
meu_retangulo = Retangulo(10, 5)

print(f"Retângulo com Base=10 e Altura=5:")
print(f"Área: {meu_retangulo.area()}")
print(f"Perímetro: {meu_retangulo.perimetro()}")

# -----------------------------------------------------

# 4. Herança parcial

class Transporte(ABC):
    
    @abstractmethod
    def mover(self):
        pass
        
    @abstractmethod
    def parar(self):
        pass

print("\n--- 4. Herança Parcial ---")

class CarroParcial(Transporte):
    def mover(self):
        print("O carro está andando.")
    

try:
    meu_carro_parcial = CarroParcial()
except TypeError as e:
    print(f"Erro gerado: {e}")



