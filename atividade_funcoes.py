# 1. Função de saudação
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()  


# 2. Função dobro
def dobro(numero):
    return numero * 2

print(dobro(5))
print(dobro(10))
print(dobro(3.5))


# 3. Função soma
def soma(a, b):
    return a + b

print(soma(10, 20))


# 4. Função mensagem
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

mensagem("Carlos")
mensagem()


# 5. Função operacoes
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

print(operacoes(10, 5))


# 6. Função média
def media(*numeros):
    return sum(numeros) / len(numeros)

print(media(2, 4, 6))
print(media(1, 2, 3, 4, 5))
print(media(10, 20, 30, 40, 50, 60, 70))


# 7. Função dados pessoais com kwargs
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife", profissão="Engenheira")


# 8. Função calculadora com funções internas
def calculadora(a, b, operacao):
    def somar(x, y): 
        return x + y
    def subtrair(x, y): 
        return x - y
    def multiplicar(x, y): 
        return x * y
    def dividir(x, y): 
        return x / y if y != 0 else "Divisão por zero não permitida."

    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtracao":
        return subtrair(a, b)
    elif operacao == "multiplicacao":
        return multiplicar(a, b)
    elif operacao == "divisao":
        return dividir(a, b)
    else:
        return "Operação inválida."

print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "divisao"))
print(calculadora(10, 5, "multiplicacao"))
print(calculadora(10, 5, "subtracao"))


# 9. Função aplicar_operacao
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def soma(a, b): 
    return a + b

def multiplicacao(a, b): 
    return a * b
def subtracao(a, b): 
    return a - b
def divisao(a, b): 
    return a / b if b != 0 else 'ERRO: Divisão por zero'

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicacao))
print(aplicar_operacao(3, 4, subtracao))
print(aplicar_operacao(3, 4, divisao))
