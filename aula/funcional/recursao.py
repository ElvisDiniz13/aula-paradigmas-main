# RECUSÃO #

# ENTRADA -> FUNÇÃO -> SAÍDA (PRÓPRIA FUNÇÃO)

#FATORIAL DE 4: 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

# print(fatorial(8))

# FIBONACCI DE 6

# A SEQUÊNCIA: 0,1,1,2,3,5,8,13...

# CALCULAR O N-NÉSIMO NÚMERO DE FIBONACCI

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 2) + fibonacci(numero -1)

print(fibonacci(6))