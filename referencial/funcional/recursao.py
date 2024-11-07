# === Recursão ===

# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    # Caso base: o fatorial de 0 é 1
    if n == 0:
        return 1
    else:
        # Chamada recursiva: n multiplicado pelo fatorial de (n - 1)
        return n * fatorial(n - 1)

# Testando a função fatorial
print(fatorial(5))  # Saída: 120
# Explicação: 5! = 5 * 4 * 3 * 2 * 1 = 120

# === Exemplo Adicional: Cálculo de Fibonacci ===

# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    # Caso base: os dois primeiros números de Fibonacci são 0 e 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Chamada recursiva: soma dos dois números anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testando a função fibonacci
print(fibonacci(6))  # Saída: 8
# Explicação: A sequência de Fibonacci é 0, 1, 1, 2, 3, 5, 8, ... O 6º número (considerando 0 como o primeiro) é 8.
