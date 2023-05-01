menu =("""
====================== Bem Vindo ao nosso Banco ======================

            Escolha uma ação
            [1] Depósito
            [2] Saque
            [3] Extrato
            [0] Sair
            

""")

saldo = 10000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")
        deposito = int(input())
        saldo  += deposito
    elif opcao == 2:
        print("Saque")
        saque = int(input())
        if saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            numero_saques += 1
            if numero_saques > LIMITE_SAQUES or saque > limite:
                print("Você atingiu o limite de saques!")
    elif opcao == 3:
        print("Extrato \n" + str(saldo))
        # Adicionar código para gerar o extrato
    elif opcao == 0:
        print("Obrigado por usar nosso banco, volte logo!")
        break
    else:
        print("Opção inválida, tente novamente.")
