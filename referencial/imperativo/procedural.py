# === Paradigma Procedural ===

# Função para somar todos os números em uma lista
def somar_lista(numeros):
    soma = 0  # Inicializa a variável soma em zero
    # Percorre cada número na lista
    for numero in numeros:
        soma += numero  # Adiciona o número atual à soma total
    return soma  # Retorna a soma total dos números

# Lista de números a ser somada
numeros = [1, 2, 3, 4, 5]

# Chama a função e imprime o resultado da soma
print(somar_lista(numeros))  # Saída esperada: 15

# Função para gerar uma lista de números pares em um intervalo
def gerar_pares(inicio, fim):
    pares = []  # Inicializa uma lista vazia para armazenar os números pares
    # Percorre todos os números no intervalo de inicio a fim (incluindo o fim)
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:  # Verifica se o número é par
            pares.append(numero)  # Adiciona o número par à lista de pares
    return pares  # Retorna a lista de números pares

# Definindo o intervalo para geração dos números pares
inicio = 1
fim = 10

# Chama a função para gerar números pares e armazena o resultado
pares = gerar_pares(inicio, fim)
# Imprime a lista de números pares gerados
print(pares)  # Saída esperada: [2, 4, 6, 8, 10]

# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n < 0:
        return None  # Retorna None se o número for negativo (fatorial não definido)
    fatorial = 1  # Inicializa o fatorial em 1
    # Percorre todos os números de 1 até n
    for i in range(1, n + 1):
        fatorial *= i  # Multiplica o fatorial pelo número atual
    return fatorial  # Retorna o fatorial calculado

# Exemplo de uso da função calcular_fatorial
numero = 5
resultado_fatorial = calcular_fatorial(numero)

# Imprime o resultado do fatorial
print(f"Fatorial de {numero}: {resultado_fatorial}")  # Saída esperada: Fatorial de 5: 120
