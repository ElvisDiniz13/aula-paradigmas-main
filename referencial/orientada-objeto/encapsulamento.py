# === Encapsulamento ===

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa uma conta bancária com um titular e um saldo inicial.

        Args:
            titular (str): Nome do titular da conta.
            saldo_inicial (float, optional): Saldo inicial da conta. Padrão é 0.
        """
        self.titular = titular  # Atributo público que armazena o nome do titular
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado) para armazenar o saldo

    # Método para obter o saldo (getter)
    def get_saldo(self):
        """Retorna o saldo atual da conta."""
        return self.__saldo  # Retorna o valor do saldo privado

    # Método para depositar um valor na conta
    def depositar(self, valor):
        """Deposita um valor na conta se o valor for positivo.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.__saldo += valor  # Adiciona o valor ao saldo
        else:
            print("O valor de depósito deve ser positivo.")  # Mensagem de erro para valor inválido

    # Método para sacar um valor da conta
    def sacar(self, valor):
        """Saca um valor da conta se houver saldo suficiente e o valor for válido.

        Args:
            valor (float): O valor a ser sacado.
        """
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor  # Deduz o valor do saldo
        else:
            print("Saldo insuficiente ou valor inválido.")  # Mensagem de erro para saldo insuficiente

# Criando uma conta e utilizando métodos de encapsulamento
conta = ContaBancaria("Maria", 500)  # Cria uma conta bancária para Maria com saldo inicial de 500
print(conta.get_saldo())  # Acessa o saldo de forma segura, usando o método getter

# Realizando operações na conta
conta.depositar(200)      # Deposita 200 na conta
conta.sacar(100)          # Saca 100 da conta
print(conta.get_saldo())   # Verifica o saldo atualizado

# Tentando acessar o saldo diretamente resultará em erro de acesso, pois é privado:
# print(conta.__saldo)  # Descomentar esta linha resultará em AttributeError: 'ContaBancaria' object has no attribute '__saldo'
