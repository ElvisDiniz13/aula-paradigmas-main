def soma(a,b):
    return a + b

# print(soma(3,4))
# print(soma(3,4))

def aplicar_duas_vezes(func, valor):
    # output = func(valor)
    # output = func(output)
    return func(func(valor))

def incrementar(x):
    return x + 1

# print(incrementar(6))

def elevar_ao_quadrado(x):
    return x ** 2

def dividir_por_dois(x):
    return x ** 2

# print(aplicar_duas_vezes(elevar_ao_quadrado, 6))

numeros = [1,2,3,4,5,6]

def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista]

numeros_quadrado = aplicar_transformacao(elevar_ao_quadrado, numeros)

print(numeros_quadrado)