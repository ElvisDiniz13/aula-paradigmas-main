# === Estrutura de Repetição ===

# Exemplo 1: Somar números até atingir um limite
limite = 100  # Define o limite superior para a soma
soma = 0      # Inicializa a variável soma em zero
numero = 1    # Começa com o número 1

# Enquanto a soma for menor que o limite, continue somando
while soma < limite:
    soma += numero  # Adiciona o número atual à soma
    numero += 1     # Incrementa o número para o próximo valor

# Imprime o resultado da soma e o último número adicionado
print(f"A soma é {soma} e o último número adicionado foi {numero-1}")

# Exemplo 2: Encontrar o primeiro número divisível por 7 em um intervalo
# Percorre os números de 1 a 99
for numero in range(1, 100):
    if numero % 7 == 0:  # Verifica se o número é divisível por 7
        print(f"O primeiro número divisível por 7 é {numero}")  # Imprime o número encontrado
        break  # Encerra o loop após encontrar o primeiro número divisível

# Exemplo 3: Verificar se todos os elementos de uma lista são positivos
numeros = [1, 2, 3, 4, 5]  # Lista de números a ser verificada
todos_positivos = True      # Inicializa a variável como True

# Percorre cada número na lista para verificar se todos são positivos
for numero in numeros:
    if numero <= 0:  # Verifica se o número é menor ou igual a zero
        todos_positivos = False  # Se encontrar um número não positivo, altera a variável para False
        break  # Encerra o loop, pois não é necessário verificar mais

# Imprime se todos os números são positivos ou não
print("Todos os números são positivos?", todos_positivos)  # Saída: True
