# === Map, Filter e Reduce ===

from functools import reduce

# Exemplo de map: dobrar todos os valores da lista
valores = [1, 2, 3, 4]
# Usa map para aplicar uma função lambda que dobra cada valor da lista
valores_dobrados = list(map(lambda x: x * 2, valores))
# Imprime a nova lista com os valores dobrados
print(valores_dobrados)  # Saída: [2, 4, 6, 8]

# Exemplo de filter: selecionar valores pares
# Usa filter para aplicar uma função lambda que verifica se cada valor é par
valores_pares = list(filter(lambda x: x % 2 == 0, valores))
# Imprime a lista filtrada com os valores pares
print(valores_pares)  # Saída: [2, 4]

# Exemplo de reduce: somar todos os valores
# Usa reduce para aplicar uma função lambda que soma dois valores
soma_total = reduce(lambda x, y: x + y, valores)
# Imprime a soma total dos valores
print(soma_total)  # Saída: 10

# === Usando Map, Filter e Reduce Juntos ===

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exemplo de uso conjunto:
# 1. Filtrar os números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# 2. Dobrar os números filtrados
numeros_dobrados = list(map(lambda x: x * 2, numeros_pares))
# 3. Somar os números dobrados
soma_dobrados = reduce(lambda x, y: x + y, numeros_dobrados)

# Imprimindo os resultados do exemplo adicional
print(numeros_pares)        # Saída: [2, 4, 6, 8, 10]
print(numeros_dobrados)     # Saída: [4, 8, 12, 16, 20]
print(soma_dobrados)        # Saída: 60
# Explicação: Filtramos os números pares, dobramos cada um deles e, em seguida, somamos os resultados.
