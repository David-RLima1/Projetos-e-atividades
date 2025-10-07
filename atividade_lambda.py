from functools import reduce

print("1. Dobro dos números (map + lambda)")

numeros_1 = [1, 2, 3, 4, 5]
dobro_numeros = list(map(lambda x: x * 2, numeros_1))

print(f"Lista Original: {numeros_1}")
print(f"Resultado: {dobro_numeros}\n") 



print("2. Filtrar pares (filter + lambda)")

numeros_2 = [10, 15, 20, 25, 30]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros_2))

print(f"Lista Original: {numeros_2}")
print(f"Resultado: {numeros_pares}\n")



print("3. Soma dos números (reduce + lambda)")

numeros_3 = [1, 2, 3, 4, 5]
soma_total = reduce(lambda x, y: x + y, numeros_3)

print(f"Lista Original: {numeros_3}")
print(f"Resultado: {soma_total}\n")



print("4. Ordenação por comprimento da palavra (sorted + lambda)")
palavras_1 = ["uva", "banana", "maçã", "laranja"]

palavras_ordenadas_tamanho = sorted(palavras_1, key=lambda palavra: len(palavra))

print(f"Lista Original: {palavras_1}")
print(f"Resultado: {palavras_ordenadas_tamanho}\n")



print("5. Primeira letra maiúscula (map + lambda)")

nomes = ["ana", "pedro", "maria"]

nomes_capitalizados = list(map(lambda nome: nome.capitalize(), nomes))

print(f"Lista Original: {nomes}")
print(f"Resultado: {nomes_capitalizados}\n") 



print("6. Produto dos números (reduce + lambda)")

numeros_produto = [2, 3, 4, 5]

produto_total = reduce(lambda x, y: x * y, numeros_produto)

print(f"Lista Original: {numeros_produto}")
print(f"Resultado: {produto_total}\n") 



print("7. Ordenar por último caractere (sorted + lambda)")

palavras_2 = ["banana", "uva", "maçã", "laranja"]

palavras_ordenadas_ultimo_char = sorted(palavras_2, key=lambda palavra: palavra[-1])

print(f"Lista Original: {palavras_2}")
print(f"Resultado: {palavras_ordenadas_ultimo_char}\n")