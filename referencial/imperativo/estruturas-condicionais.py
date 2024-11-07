# === Estruturas Condicionais ===

# Exemplo 1: Verificar se um número é par ou ímpar
numero = 7  # Definindo o número a ser verificado

# Verifica se o número é par (divisível por 2)
if numero % 2 == 0:
    print(f"{numero} é par.")  # Se for par, imprime que o número é par.
else:
    print(f"{numero} é ímpar.")  # Se não for par, imprime que o número é ímpar.  # Saída: 7 é ímpar.


# Exemplo 2: Substituir números negativos por zero em uma lista
numeros = [5, -3, 7, -1, 0, -6]  # Lista de números

# Percorre a lista para verificar cada elemento
for i in range(len(numeros)):
    # Se o número for negativo, substitui por zero
    if numeros[i] < 0:
        numeros[i] = 0

# Imprime a lista após a substituição
print(numeros)  # Saída: [5, 0, 7, 0, 0, 0]


# Exemplo 3: Verificar se uma pessoa pode votar com base na idade
idade = 16  # Definindo a idade da pessoa

# Verifica se a idade é suficiente para votar
if idade >= 16:
    print("A pessoa pode votar.")  # Se a idade for 16 ou mais, imprime que a pessoa pode votar.
else:
    print("A pessoa não pode votar.")  # Se a idade for menor que 16, imprime que a pessoa não pode votar.
