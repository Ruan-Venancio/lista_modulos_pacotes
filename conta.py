class Conta:
    def __init__(self, agencia, numero):
        self.saldo = 0.00
        self.numero = numero
        self.agencia = agencia
        self.histo = []
        self.limite = 1000.00
        

#

    def saque(self, quantia):
        print("=-" * 10)
        print("SAQUE")
        if quantia > self.saldo + self.limite:
            print("saldo insuficiente.")
            return
        if quantia < 0:
            print("não é possível sacar valores negativos.")
            return
        self.saldo -= quantia
        self.histo.append(("Saque", quantia))


    def deposito(self, quantia):
        print("=-" * 10)
        print("DEPÓSITO")
        if quantia < 0:
            print('impossível depositar valores negativos.')
            return
        self.saldo += quantia
        self.histo.append(("Depósito", quantia))

    def verificar_saldo(self):
        print("=-" * 10)
        print("SALDO")
        print(f" R${self.saldo:}")




    def transferir(self, conta2, quantia):
        if self.saldo + self.limite < quantia:
            print('Saldo insuficiente.')
            return
        self.saldo -= quantia
        self.histo.append(f'Transferencia no valor de: R${quantia} para a conta {conta2.numero} realizada com sucesso')
        conta2.saldo += quantia


    def extrato(self):
        print("=-" * 10)
        print("EXTRATO")
        print(f'Agencia: {self.agencia}  -  Limite: R${self.limite}  -  Conta: {self.numero}  -  Saldo: R${self.saldo}')
        for operacao in self.histo:
            print(operacao)
    



    def encerrar_conta(self):
        print("=-" * 10)
        print("ENCERRAR CONTA")
        if self.saldo <= 0:
            print("Sua conta não está negativada. Não é possivel encerra-la.")
            print("Quite sua dívida")
            return
        else:
            print("Conta encerrada.")


