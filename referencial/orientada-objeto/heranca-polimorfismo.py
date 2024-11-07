# === Herança ===

# Classe base (superclasse) que representa um animal genérico
class Animal:
    nome: str  # Atributo que armazena o nome do animal

    def __init__(self, nome: str):
        """Inicializa um objeto do tipo Animal com um nome específico.

        Args:
            nome (str): O nome do animal.
        """
        self.nome = nome  # Atribui o nome passado como parâmetro ao atributo nome

    def emitir_som(self):
        """Método abstrato que deve ser implementado pelas subclasses.
        
        Este método é um espaço reservado e não faz nada na classe base.
        """
        pass  # Método a ser implementado pelas subclasses (não faz nada na classe base)

# Subclasse que herda de Animal e representa um cachorro
class Cachorro(Animal):
    def emitir_som(self):
        """Implementa o método emitir_som para cachorros."""
        print(f"{self.nome} faz: Au au!")  # Imprime o som que o cachorro faz

# Subclasse que herda de Animal e representa um gato
class Gato(Animal):
    def emitir_som(self):
        """Implementa o método emitir_som para gatos."""
        print(f"{self.nome} faz: Miau!")  # Imprime o som que o gato faz

# Criando objetos das subclasses e chamando seus métodos
cachorro = Cachorro("Rex")  # Cria um objeto Cachorro com o nome "Rex"
gato = Gato("Mia")          # Cria um objeto Gato com o nome "Mia"

# Chamando o método emitir_som de cada objeto
cachorro.emitir_som()  # Saída: Rex faz: Au au!
gato.emitir_som()      # Saída: Mia faz: Miau!
