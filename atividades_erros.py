# 1 Escreva um programa que peça ao usuário para digitar um número. 
# Trate o erro caso ele digite algo que não seja um número inteiro.
while True: 
    try: 
        numero = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('ERRO: Digite um número inteiro.')

# 2 Peça ao usuário dois números e tente multiplicá-los. Se o usuário 
# digitar algo inválido, exiba uma mensagem de erro.

print('=' * 100)

print('Multiplicador de números')
def checar_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print('ERRO: Digite um número.')
    
    

a = checar_numero('Digite o primeiro número: ')
b = checar_numero('Digite o segundo número: ')
print(f'{a} X {b} = {a*b}')

# 3  Crie um programa que peça ao usuário um número inteiro. Se a conversão for
# bem-sucedida, mostre uma mensagem usando o bloco else.


print('=' * 100)

while True:
    try: 
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('ERRO: Digite um número válido')
    else:
        print('Conversão realizada com sucesso!')
        break

# 4 Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

print('=' * 100)
try:
    with open('dados.txt', 'r') as arquivo:
        print(f'Conteúdo do arquivo: {arquivo.read()}')
        

except FileNotFoundError:
    print('O arquivo "dados.txt" não foi encontrado.')

finally:
    print('Encerrando programa.')


# 5 Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
# Caso contrário, retorne o resultado da divisão.

print('=' * 100)
print('Questão - 5')
while True:
    try:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('ERRO: Digite números.')

def dividir (a, b):
    if b == 0:
        raise ZeroDivisionError('ERRO: Divisão por zero.')
    else:
        return a/b
    
print(dividir(a, b))

# 6 Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError('ERRO: Idade inválida.')
    else:
        return idade

# 7 Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

# ValueError se o usuário digitar algo inválido

# ZeroDivisionError se tentar dividir por zero

print('=' * 100)

def dividir_com_tratamento_de_erro():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ValueError:
        print("Erro! Por favor, digite apenas números válidos.")
    except ZeroDivisionError:
        print("Erro! Não é possível dividir por zero.")

# 8 Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

# try para a conversão,

# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".

print('=' * 100)

try:
    numero = int(input("Digite um número inteiro para verificar se é par: "))
except ValueError:
    print("Erro! Entrada inválida.")
else:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
finally:
    print("Fim do programa.")


# 9 Crie uma função sacar(saldo, valor) que:

# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.

# Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.


print('=' * 100)
class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    if saldo < valor:
        raise SaldoInsuficienteError('Saldo insuficiente.')
    
    return f'R$ {saldo - valor:.2f}'

try:
    saldo = float(input('Digite o valor do saldo em conta: '))
    valor = float(input('Digite o valor que deseja sacar: '))
    
    print(f'Novo saldo: {sacar(saldo, valor)}')
except ValueError:
        print('ERRO: Digite os valores pedidos para realizar a operação.')


