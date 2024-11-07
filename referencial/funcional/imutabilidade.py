# === Imutabilidade ===

# Neste exemplo, vamos explorar o conceito de imutabilidade usando tuplas.
# As tuplas são estruturas de dados que, uma vez criadas, não podem ser alteradas.

# Criando uma tupla inicial com três elementos
tupla = (1, 2, 3)

# Tentativa de modificar um elemento da tupla (descomentá-la geraria um erro)
# tupla[0] = 4  # Isso geraria um erro do tipo TypeError, pois tuplas são imutáveis.

# Em vez de tentar modificar a tupla original, podemos criar uma nova tupla.
# Aqui, adicionamos um novo elemento à tupla existente.
nova_tupla = tupla + (4,)  # O operador + concatena a tupla original com uma nova tupla

# Exibindo a nova tupla
print(f"Tupla original: {tupla}")  # Saída: Tupla original: (1, 2, 3)
print(f"Nova tupla: {nova_tupla}")  # Saída: Nova tupla: (1, 2, 3, 4)

# Resumo: A imutabilidade é uma característica importante das tuplas,
# que garante que seus dados não serão alterados acidentalmente.
# Se precisar adicionar ou modificar elementos, crie uma nova tupla a partir da original.
