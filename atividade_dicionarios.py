# 1 Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.

aluno = {'aluno':'Pedro', 'idade': 22, 'nota': 7.5}


# 2 Dado o dicionário:

# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}   

print(f'Nome do produto: {produto["nome"]}')
print(f'Quantidade em estoque: {produto["estoque"]}')


# 3 Dado o dicionário:

# pessoa = {"nome": "Carlos", "idade": 30}
# Adicione uma nova chave "cidade" com valor "São Paulo".

pessoa = {"nome": "Carlos", "idade": 30}

pessoa["cidade"] = "São Paulo"

print(pessoa)


# 4 Dado o dicionário:

# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

# 5 Verifique se a chave "telefone" existe no dicionário:

# contato = {"nome": "Ana", "email": "ana@email.com"}

contato = {"nome": "Ana", "email": "ana@email.com"}

print(contato.get("telefone", "A chave especificada não existe"))


#  6 Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contagem_de_palavras(lista_palavras):

    contagem = {}

    for fruta in palavras:
        contagem[fruta] = contagem.get(fruta, 0) + 1
    return contagem

resultado = contagem_de_palavras(palavras)
print(resultado)


# 7 Dado o dicionário:

# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.


d = {"a": 1, "b": 2, "c": 3}
d_inverso = {valor:chave for chave, valor in d.items()}
print(d_inverso)

# 8 Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. 
# Depois, imprima a média de cada aluno.

alunos = {
          "Ana": [7.5, 8, 6],
          "Maria": [6, 8.5, 5],
          "Douglas": [8, 9.5, 7]
          }


for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media:.1f}")

# 9 Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. 
# Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

frutas1 = {"maça":4, "laranja":5, "melancia":2}
frutas2 = {"melao":3, "limao":7, "maça":8}

def juntando_dicionarios(dicionario1, dicionario2):

    novo_dicionario = dicionario1.copy()
    novo_dicionario.update(dicionario2)
    return novo_dicionario


print(juntando_dicionarios(frutas1, frutas2))


# 10 Dado o dicionário:

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.


pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

pontuacoes_ordenada = sorted(pontuacoes.items(), key=lambda item:item[1], reverse=True)

for nome, pontuacao in pontuacoes_ordenada:
    print(f'{nome}: {pontuacao}')




