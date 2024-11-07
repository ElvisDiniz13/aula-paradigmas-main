# === Programação Orientada a Objetos (POO) + Paradigmas Imperativos ===
from typing import List

# Classe que representa um funcionário
class Funcionario:
    def __init__(self, nome: str, salario: float):
        """Inicializa um funcionário com nome e salário.

        Args:
            nome (str): Nome do funcionário.
            salario (float): Salário do funcionário.
        """
        self.nome = nome  # Atributo público que armazena o nome do funcionário
        self.__salario = salario  # Atributo privado que armazena o salário

    def get_salario(self):
        """Retorna o salário do funcionário."""
        return self.__salario  # Método getter para acessar o salário

    def aumentar_salario(self, percentual: float):
        """Aumenta o salário do funcionário de acordo com um percentual.

        Args:
            percentual (float): Percentual de aumento a ser aplicado.
        """
        if percentual > 0:
            aumento = self.__salario * (percentual / 100)  # Calcula o valor do aumento
            self.__salario += aumento  # Aplica o aumento
        else:
            print("O percentual deve ser positivo.")

# Função para calcular a média salarial de uma lista de funcionários
def calcular_media_salarial(funcionarios: List[Funcionario]):
    """Calcula a média salarial de uma lista de funcionários.

    Args:
        funcionarios (list): Lista de objetos do tipo Funcionario.

    Returns:
        float: Média salarial dos funcionários.
    """
    total_salarios = 0
    quantidade = len(funcionarios)  # Obtém a quantidade de funcionários

    for funcionario in funcionarios:
        total_salarios += funcionario.get_salario()  # Soma os salários

    media = total_salarios / quantidade if quantidade > 0 else 0  # Calcula a média
    return media

# Criando uma lista de funcionários
funcionarios = [
    Funcionario("Alice", 3000),
    Funcionario("Bob", 4000),
    Funcionario("Charlie", 5000)
]

# Exibindo os salários iniciais
for f in funcionarios:
    print(f"Salário inicial de {f.nome}: R$ {f.get_salario():.2f}")

# Aumentando o salário de Bob em 10%
funcionarios[1].aumentar_salario(10)  # Aumenta o salário de Bob

# Exibindo os salários após aumento
print("\nApós aumento de salário:")
for f in funcionarios:
    print(f"Salário de {f.nome}: R$ {f.get_salario():.2f}")

# Calculando e exibindo a média salarial
media = calcular_media_salarial(funcionarios)
print(f"\nMédia salarial: R$ {media:.2f}")
