# === Funções puras ===

# Exemplo de uma função pura que soma dois números
def soma(a, b):
    return a + b  # Sempre retorna o mesmo resultado para as mesmas entradas

# Testando a função pura
print(soma(3, 4))  # Saída: 7
print(soma(3, 4))  # Saída: 7
# Observação: A função 'soma' é pura porque não tem efeitos colaterais e sempre produz o mesmo resultado.

# === Funções de alta ordem ===

# Exemplo de uma função de alta ordem que aplica uma função duas vezes a um valor
def aplicar_duas_vezes(func, valor):
    return func(func(valor))  # Chama a função 'func' duas vezes, passando o resultado da primeira chamada como entrada para a segunda

# Função que incrementa um número
def incrementar(x):
    return x + 1  # Retorna o número incrementado em 1

# Aplica a função 'incrementar' duas vezes ao valor 5
print(aplicar_duas_vezes(incrementar, 5))  # Saída: 7
# Explicação: O valor 5 é incrementado para 6 na primeira aplicação e para 7 na segunda.

# Função que aplica uma transformação a cada elemento de uma lista
def aplicar_transformacao(funcao, lista):
    # Utiliza compreensão de listas para aplicar 'funcao' a cada elemento de 'lista'
    return [funcao(x) for x in lista]  # Retorna uma nova lista com a transformação aplicada

# Função de transformação: eleva um número ao quadrado
def elevar_ao_quadrado(x):
    return x ** 2  # Retorna o quadrado do número

# Lista de números para transformação
numeros = [1, 2, 3, 4, 5]

# Aplicando a transformação que eleva cada número ao quadrado
numeros_quadrados = aplicar_transformacao(elevar_ao_quadrado, numeros)
print(numeros_quadrados)  # Saída: [1, 4, 9, 16, 25]
# Comentário: A função 'aplicar_transformacao' utiliza 'elevar_ao_quadrado' para transformar cada elemento da lista 'numeros'.
