# === Abstração ===

from abc import ABC, abstractmethod  # Importa ABC e abstractmethod para criar classes abstratas

# Classe abstrata que define a interface para formas geométricas
class FormaGeometrica(ABC):
    
    @abstractmethod
    def calcular_area(self):
        """Método abstrato para calcular a área de uma forma geométrica.
        Deve ser implementado por subclasses."""
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

# Subclasse que representa um círculo e implementa a interface da classe abstrata
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        """Inicializa um círculo com um raio específico."""
        self.raio = raio

    def calcular_area(self):
        """Calcula e retorna a área do círculo usando a fórmula πr²."""
        return 3.14 * self.raio ** 2  # Usando 3.14 como uma aproximação de π

# Subclasse que representa um retângulo e implementa a interface da classe abstrata
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        """Inicializa um retângulo com largura e altura específicos."""
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        """Calcula e retorna a área do retângulo usando a fórmula largura * altura."""
        return self.largura * self.altura

# Instanciando as subclasses e calculando a área de cada forma
formas = [Circulo(5), Retangulo(3, 4)]  # Criando uma lista de formas geométricas

for forma in formas:
    # Para cada forma, chama o método calcular_area e imprime o resultado
    print(f"Área: {forma.calcular_area()}")  # Saída: Área: 78.5 para o círculo e Área: 12 para o retângulo

# === Composição ===

# Classe que representa um motor
class Motor:
    def __init__(self, potencia):
        """Inicializa o motor com uma potência específica (em CV)."""
        self.potencia = potencia

# Classe que representa um carro
class Carro:
    def __init__(self, marca: str, modelo: str, motor: Motor):
        """Inicializa um carro com marca, modelo e um objeto Motor.
        A composição é utilizada aqui, indicando que um carro 'tem um' motor."""
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # O carro tem uma instância da classe Motor

    def exibir_detalhes(self):
        """Exibe os detalhes do carro, incluindo a marca, modelo e potência do motor."""
        print(f"Carro: {self.marca} {self.modelo}, Motor: {self.motor.potencia}CV")

# Criando objetos para o motor e carro
motor = Motor(150)  # Cria um motor com 150CV de potência
carro = Carro("Honda", "Civic", motor)  # Cria um carro Honda Civic com o motor criado

# Exibe os detalhes do carro
carro.exibir_detalhes()  # Saída: Carro: Honda Civic, Motor: 150CV
