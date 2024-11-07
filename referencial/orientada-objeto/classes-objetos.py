# === Classes e Objetos ===

# Definindo uma classe chamada `Carro`
class Carro:
    def __init__(self, marca, modelo, ano):
        """Inicializa um objeto Carro com marca, modelo e ano específicos.
        
        Args:
            marca (str): A marca do carro.
            modelo (str): O modelo do carro.
            ano (int): O ano de fabricação do carro.
        """
        self.marca = marca  # Atributo que armazena a marca do carro
        self.modelo = modelo  # Atributo que armazena o modelo do carro
        self.ano = ano  # Atributo que armazena o ano do carro

    def exibir_detalhes(self):
        """Exibe os detalhes do carro em uma string formatada."""
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

# Criando um objeto da classe `Carro`
meu_carro = Carro("Toyota", "Corolla", 2020)  # `meu_carro` é uma instância da classe Carro

# Chamando um método do objeto
meu_carro.exibir_detalhes()  # Saída: Carro: Toyota Corolla, Ano: 2020

# === Diferença entre Classe e Objeto ===

# Classe: é uma estrutura que define um tipo de objeto. 
# Ela contém atributos (variáveis) e métodos (funções) que descrevem o comportamento e as propriedades dos objetos.
# Exemplo: A classe `Carro` define como um carro deve se comportar e quais dados ele deve ter.

# Objeto: é uma instância da classe. Cada objeto possui seus próprios valores para os atributos definidos pela classe.
# Exemplo: `meu_carro` é um objeto da classe `Carro`, que possui a marca "Toyota", modelo "Corolla" e ano 2020.
