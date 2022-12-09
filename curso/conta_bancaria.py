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
    opcao = input(menu)

    if opcao == 1:
        print("Depósito")
        deposito = int(input())
        saldo  += deposito
    elif opcao == 2:
        print("Saque")
        saque = int(input())
        saque -= saldo
        if saque != saque:
            numero_saques += 1
        elif numero_saques == LIMITE_SAQUES or saque > 500:
            print("Voce atingiu o Limite de saques")    
    elif opcao == 3:
        print("Extrato")
    elif opcao == 4:
        print("Obrigado por usar nosso banco, volte logo!")
        break
    else:
        ("Opção inválida, tente novamente.")
