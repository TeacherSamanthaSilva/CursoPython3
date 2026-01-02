from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


class ContaBancaria(ABC):
    def __init__(self, numero: int, cliente: Cliente, saldo: float = 0.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo

    @abstractmethod
    def tipo_conta(self):
        pass

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    def transferir(self, valor: float, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def consultar_saldo(self):
        return self._saldo

    def __str__(self):
        return (
            f"{self.tipo_conta()} | "
            f"Conta: {self._numero} | "
            f"{self._cliente.nome} | "
            f"Saldo: R$ {self._saldo:.2f}"
        )


class ContaCorrente(ContaBancaria):
    def tipo_conta(self):
        return "Conta Corrente"


class ContaPoupanca(ContaBancaria):
    def tipo_conta(self):
        return "Conta Poupança"

    def render_juros(self, taxa: float):
        if taxa <= 0:
            raise ValueError("A taxa deve ser positiva.")
        self._saldo += self._saldo * taxa


class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def criar_conta_corrente(self, numero: int, cliente: Cliente):
        conta = ContaCorrente(numero, cliente)
        self.contas.append(conta)
        return conta

    def criar_conta_poupanca(self, numero: int, cliente: Cliente):
        conta = ContaPoupanca(numero, cliente)
        self.contas.append(conta)
        return conta

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

# Criando o banco
banco = Banco("Banco Python")

# Criando clientes
cliente1 = Cliente("Samantha", "123.456.789-00")
cliente2 = Cliente("Carlos", "987.654.321-00")

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

# Criando contas
conta1 = banco.criar_conta_corrente(1001, cliente1)
conta2 = banco.criar_conta_poupanca(2001, cliente2)

# Operações
conta1.depositar(1000)
conta1.transferir(200, conta2)
conta2.render_juros(0.05)

# Exibindo informações
banco.listar_contas()
