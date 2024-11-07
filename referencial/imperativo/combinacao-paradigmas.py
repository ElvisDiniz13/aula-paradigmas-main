# === Combinação de Paradigmas ===

# Função para aplicar um desconto a um preço
def aplicar_desconto(preco, desconto):
    return preco * (1 - desconto)  # Calcula o preço após aplicar o desconto

# Função para calcular o total com desconto em uma lista de preços
def calcular_total_com_desconto(precos, desconto):
    total = 0  # Inicializa o total em zero
    # Percorre cada preço na lista
    for preco in precos:
        total += aplicar_desconto(preco, desconto)  # Adiciona o preço com desconto ao total
    return total  # Retorna o total após aplicar todos os descontos

# Lista de preços
precos = [100, 200, 300, 400, 500]  # Preços de produtos
desconto = 0.1  # 10% de desconto

# Calculando o total com desconto
total = calcular_total_com_desconto(precos, desconto)
print(f"Total com desconto: R$ {total:.2f}")  # Saída esperada: Total com desconto: R$ 1350.00

# Exemplo adicional: Função para calcular o preço médio após aplicar o desconto
def calcular_preco_medio(precos, desconto):
    total = calcular_total_com_desconto(precos, desconto)  # Calcula o total com desconto
    media = total / len(precos)  # Calcula a média dividindo o total pelo número de preços
    return media  # Retorna o preço médio

# Calculando o preço médio após o desconto
preco_medio = calcular_preco_medio(precos, desconto)
print(f"Preço médio com desconto: R$ {preco_medio:.2f}")  # Saída esperada: Preço médio com desconto: R$ 270.00
