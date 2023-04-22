from conta import *

print("=-" * 12)
print("SISTEMA BANCÁRIO:")
#Criação das contas
conta01 = Conta("387", "23972")
conta02 = Conta("456", "53321")
conta03 = Conta("245", "97827")

#depósito na conta 01 de 3000 reais
conta01.deposito(3000)

#saque na conta 01 de 200 reais
conta01.saque(200)

#transferencia da conta 01 para a conta 02 no valor de 600 reais
conta01.transferir(conta02, 600)

#verificando o extrato da conta 01
conta01.extrato()

#verificar o saldo da conta 01
conta01.verificar_saldo()

#transferencia da conta 01 para a conta 03 no valor de 2201 reais (so pro valor ficar negativado e a função ENCERRAR A CONTA não dê certo)
conta01.transferir(conta03, 2201)

#verificando o extrato da conta 01
conta01.extrato()

#verificar o saldo da conta 01
conta01.verificar_saldo()

#tentando encerrar a conta 01
conta01.encerrar_conta()


#ALGUMAS MELHORIAS:
# - Solicitação de empréstimos e financiamentos.
# - Depósitos em contas correntes ou de poupança.
# - Transferencias por pix
# - parcelamento de produtos (objetos) no cartão de crédito
# - compra no débito do cartão da conta