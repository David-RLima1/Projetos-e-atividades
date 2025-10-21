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

# Uso
print("--- 1. Teste da Interface Pagamento ---")
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


print("\n--- 2. Teste de Interface Múltipla (Computador) ---")
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

print("\n--- 3. Teste de Herança Múltipla de Interfaces (Relatorio) ---")
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

print("\n--- 4. Teste Forçando Contrato (Implementação Parcial) ---")

class RepositorioMemoriaParcial(Repositorio):
    def __init__(self):
        self._dados = {}
        
    def salvar(self, objeto):
        # Supondo que o objeto tenha um 'id'
        self._dados[objeto.id] = objeto
        print(f"Objeto {objeto.id} salvo na memória.")
        
    # O método abstrato buscar(id) não foi implementado!

try:
    repo_parcial = RepositorioMemoriaParcial()
except TypeError as e:
    print(f"Erro gerado ao tentar instanciar: {e}")

print("\nO que acontece?")
print("Ocorre o erro 'TypeError: Can't instantiate abstract class RepositorioMemoriaParcial with abstract method buscar'.")
print("Isso confirma que, para instanciar uma classe, ela DEVE implementar TODOS os métodos abstratos que herdou de suas 'interfaces' (Classes Abstratas Base).")


print("\n--- Correção (Implementação Completa) ---")

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self._dados = {}
        
    def salvar(self, objeto):
        id_obj = getattr(objeto, 'id', hash(objeto))
        self._dados[id_obj] = objeto
        print(f"Objeto (ID: {id_obj}) salvo na memória.")
        return id_obj
        
    def buscar(self, id):
        print(f"Buscando ID {id} na memória...")
        return self._dados.get(id, None) 

repo_completo = RepositorioMemoria()

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __repr__(self):
        return f"Usuario(nome='{self.nome}')"

user1 = Usuario(1, "Ana")
id_salvo = repo_completo.salvar(user1)

print(f"Busca pelo ID {id_salvo}: {repo_completo.buscar(id_salvo)}")
print(f"Busca por ID 99 (inexistente): {repo_completo.buscar(99)}")
print("Instanciação do RepositorioMemoria (completo) bem-sucedida!")