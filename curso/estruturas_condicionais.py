programas = int(input("Escolha qual programa deseja rodar [1]\n[2]\n[3]\n[4] "))


# CNH -----------------------------------------------------------------------
if programas == 1:
    MAIOR_IDADE_BRASIL = 18
    idade = int(input("Informe sua idade: "))

    tempo_restante = MAIOR_IDADE_BRASIL - idade

    if idade >= MAIOR_IDADE_BRASIL:
        print("Você esta apto a tirar sua CNH!")
    else:
        print(f"Infelizmente Você ainda não tem a idade minima para tirar a CNH, ainda faltam {tempo_restante} anos para você estar apto.")

#Banco simples --------------------------------------------------------------
elif programas == 2:
    opcao = int(input("Informe uma opção: [1] sacar \n[2] extrato "))

    if opcao == 1:
        valor = float(input("Informe o valor para saque: "))
    elif opcao == 2:
        print("Exibindo o extrato ... ")
    else:
        print("Opção inválida!!!")

# if aninhado ---------------------------------------------------------------
elif programas == 3:
    contas = int(input("Selecione uma opção de conta conta normal [1] \n conta universitaria [2] "))


    saldo = 10000
    saque = float(input("Informe o valor do saque: "))
    cheque_especial = 1000

    conta_normal = 1

    conta_universitaria = 0

    if contas == 1:
        if conta_normal == True:
            if saldo >= saque:
                print("Saque realizado com sucesso!")
            elif saque <= (saldo + cheque_especial):
                print("Saque realizado com uso do cheque especial")
            else:
                print("Saldo insuficiente!")
    elif contas == 2:
        if conta_universitaria == False:
            if saldo >= saque:
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente!")

# if ternario ---------------------------------------------------------------
elif programas == 4:
    saldo = 10000
    saque = float(input("Informe o valor do saque: "))
    
    status = "Sucesso" if saldo >= saque else "falha"

    print(f"{status} ao realizar o saque!")

else:
    print("Opção inválida!")