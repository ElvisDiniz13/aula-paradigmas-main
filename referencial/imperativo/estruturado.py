# === Paradigma Estruturado ===

# Função para encontrar o maior e o menor número em uma lista
def encontrar_maior_menor(numeros):
    # Se a lista estiver vazia, retorna None para ambos os valores
    if not numeros:
        return None, None

    # Inicializa maior e menor como o primeiro elemento da lista
    maior = menor = numeros[0]
    
    # Percorre cada número na lista para verificar qual é o maior e o menor
    for numero in numeros:
        if numero > maior:          # Se o número atual for maior que o maior registrado, atualiza o maior
            maior = numero
        elif numero < menor:        # Se o número atual for menor que o menor registrado, atualiza o menor
            menor = numero
    
    return maior, menor  # Retorna o maior e o menor número encontrados

# Lista de números para teste
numeros = [3, 1, 7, 4, 2]
# Chama a função para encontrar o maior e o menor número e armazena os resultados
maior, menor = encontrar_maior_menor(numeros)

# Imprime os resultados
print(f"Maior: {maior}, Menor: {menor}")  # Saída esperada: Maior: 7, Menor: 1

# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    soma = 0            # Inicializa a soma das notas
    quantidade = 0      # Inicializa a quantidade de notas
    for nota in notas:  # Percorre cada nota na lista
        soma += nota    # Adiciona a nota atual à soma total
        quantidade += 1 # Incrementa a quantidade de notas

    media = soma / quantidade  # Calcula a média dividindo a soma pelo total de notas
    return media               # Retorna a média

# Função para classificar o aluno com base na média das notas
def classificar_aluno(notas):
    media = calcular_media(notas)  # Calcula a média usando a função auxiliar
    
    # Classifica o aluno de acordo com a média
    if media >= 7:
        return "Aprovado"       # Retorna "Aprovado" se a média for maior ou igual a 7
    elif media >= 5:
        return "Recuperação"    # Retorna "Recuperação" se a média estiver entre 5 e 6.9
    else:
        return "Reprovado"      # Retorna "Reprovado" se a média for inferior a 5

# Exemplo de uso
notas_aluno = [7, 6, 5, 8, 9]   # Lista de notas do aluno
# Chama a função para classificar o aluno e armazena o resultado
resultado = classificar_aluno(notas_aluno)
# Imprime o resultado da classificação
print(f"Resultado: {resultado}")  # Saída esperada: Aprovado