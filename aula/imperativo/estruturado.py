notas_aluno = [7,4,5,8,9,4]

# função para calcular média
def calcular_media(notas):
    soma = 0
    quantidade = 0
    for nota in notas:
        soma += nota
        quantidade += 1
    media = soma/quantidade
    return media

def classificar_aluno(notas):
    media = calcular_media(notas)

    if media >= 7:
        return "Aprovado"
    elif media>= 5:
        return "Recuperação"
    else:
        return "Reprovado"

resultado = classificar_aluno(notas_aluno)

print(resultado)