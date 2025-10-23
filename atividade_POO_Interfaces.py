from abc import ABC, abstractmethod


class Pagamento(ABC):
    
    @abstractmethod
    def processar(self, valor):
        """Processa um pagamento de um determinado valor."""
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via Cartão de Crédito...")
        print("Pagamento aprovado.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via Boleto...")
        print("Boleto gerado. Aguardando pagamento.")

print("--- 1. Interface Pagamento ---")
meu_cartao = CartaoCredito()
meu_boleto = Boleto()

meu_cartao.processar(100.50)
print("-" * 20)
meu_boleto.processar(75.00)

# -----------------------------------------------------


class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Computador ligando... Sistema operacional iniciado.")
        else:
            print("O computador já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Computador desligando... Salvando arquivos...")
        else:
            print("O computador já está desligado.")


print("\n--- 2. Interface Múltipla (Computador) ---")
meu_pc = Computador()
meu_pc.desligar() 
meu_pc.ligar()    
meu_pc.ligar()    
meu_pc.desligar() 

# -----------------------------------------------------


class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def imprimir(self):
        print(f"Iniciando impressão do relatório:")
        print(f"[PÁGINA 1]\n{self.conteudo}\n[FIM DA IMPRESSÃO]")

    def exportar(self):
        print(f"Exportando relatório '{self.conteudo[:20]}...' para PDF...")
        print("Relatorio.pdf gerado com sucesso.")

print("\n--- 3. Herança Múltipla de Interfaces (Relatorio) ---")
relatorio_vendas = Relatorio("Dados de vendas do Q4: R$ 500.000")
relatorio_vendas.imprimir()
relatorio_vendas.exportar()

# -----------------------------------------------------


class Repositorio(ABC):
    
    @abstractmethod
    def salvar(self, objeto):
        pass
        
    @abstractmethod
    def buscar(self, id):
        pass

print("\n--- 4. Forçando Contrato (Implementação Parcial) ---")

class RepositorioMemoriaParcial(Repositorio):
    def __init__(self):
        self._dados = {}
        
    def salvar(self, objeto):

        self._dados[objeto.id] = objeto
        print(f"Objeto {objeto.id} salvo na memória.")
        

try:
    repo_parcial = RepositorioMemoriaParcial()
except TypeError as e:
    print(f"Erro gerado ao tentar instanciar: {e}")


