# === Funções Anônimas (Lambda) ===

# Exemplo de função lambda: calcula o dobro de um número
dobro = lambda x: x * 2
# Testando a função lambda com o valor 4
print(dobro(4))  # Saída: 8
# Explicação: A função 'dobro' recebe 4 e retorna 8.

# Usando lambda em uma função de alta ordem
valores = [1, 2, 3, 4]
# Usa map para aplicar uma função lambda que dobra cada valor da lista
valores_dobrados = list(map(lambda x: x * 2, valores))
# Imprimindo a nova lista com os valores dobrados
print(valores_dobrados)  # Saída: [2, 4, 6, 8]
# Explicação: A função lambda é aplicada a cada elemento da lista 'valores', resultando em uma nova lista.

# === Exemplo Adicional: Filtrando Números Ímpares ===

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando lambda para filtrar números ímpares
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
# Imprimindo a lista de números ímpares
print(numeros_impares)  # Saída: [1, 3, 5, 7, 9]
# Explicação: A função lambda verifica se cada número é ímpar, retornando apenas os ímpares da lista original.
