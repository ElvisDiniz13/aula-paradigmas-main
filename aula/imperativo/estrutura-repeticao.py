# SOMAR NÚMEROS ATÉ ATINGIR UM LIMITE

limite = 100
soma = 0
numero = 1

## ENQUANTO A SOMA FOR MENOR DO QUE O LIMITE, CONTINUE SOMANDO
# while soma < limite:
#     soma += numero
#     numero += 1
#     print(soma)
#     print(numero)

## ENCONTRAR O PRIMEIRO NÚMERO DIVISÍVEL POR 7 EM UM INTERVALO

# for numero in range(1, 100):
#     #print(numero)
#     if numero % 7 ==0:
#         print(numero)
#         break

# VERIFICAR SE TODOS OS ITENS DE UMA LISTA SÃO POSITIVOS

numeros = [1,2,3,8,9, -10]
todos_positivos = True

for numero in numeros:
    if numero < 0:
        print(numero)
        todos_positivos = False
        print("Número negativo encontrado")
        break

if todos_positivos:
    print("Todos os números são positivos")
    