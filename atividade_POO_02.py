print('''\n1) Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um 
getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)\n''')

class ContaBancaria:
    def __init__(self, titular, saldo = 0) -> None:
        self.__titular = titular
        self.__saldo = saldo


    def __str__(self) -> str:
        return f'Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}'
    

    def __repr__(self) -> str:
        return f'ContaBancaria(titular= {self.titular!r}, saldo= {self.saldo!r})'
    
    
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
    

    @saldo.setter
    def saldo(self, novo_saldo: float) -> None:

        if not isinstance(novo_saldo, (int, float)):
            return
       
        if novo_saldo < 0:
            return
    
        self.__saldo = novo_saldo

    
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


pessoa_01 = ContaBancaria('Sofia')

pessoa_01.depositar(1000)
pessoa_01.checar_saldo()
pessoa_01.saldo = 1
pessoa_01.checar_saldo()



print('''\n2) Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores\n''')


class Pessoa:
    def __init__(self, nome: str, data_de_nascimento: str, cpf: str, identidade: str):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__identidade = identidade 

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nData de Nascimento: {self.data_de_nascimento}\nCPF: {self.cpf}\nIdentidade: {self.identidade}"


    def __repr__(self) -> str:
        return f"Pessoa(nome = {self.nome}, data_de_nascimento = {self.data_de_nascimento}, cpf = {self.cpf}, identidade = {self.identidade})"
    
    
    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str) -> None:
        
        if len(novo_cpf) == 11:
            self.__cpf = novo_cpf
        else:
            raise ValueError("CPF inválido.")

    @property
    def identidade(self) -> str:
        return self.__identidade

    @identidade.setter
    def identidade(self, nova_identidade: str) -> None:
        
        if len(nova_identidade) == 7:
            self.__identidade = nova_identidade
            
        else:
            raise ValueError('Identidade inválida.')
        
        

            

pessoa_02 = Pessoa("João", "15/02/1999", "99999999999", "7777777")
print(pessoa_02)




